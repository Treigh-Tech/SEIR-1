# ---------------------------------------------------------
# BEFORE RUNNING THIS SCRIPT
# ---------------------------------------------------------
#
# Install the required Python packages:
#
# python -m pip install azure-identity azure-mgmt-resource
#
#
# Login to Azure using the Azure CLI:
#
# az login
#
#
# Verify that you are logged in:
#
# az account show
#
#
# Display all subscriptions available to your account:
#
# az account list -o table
#
#
# If you have multiple subscriptions, select the subscription
# you want Python to use:
#
# az account set --subscription "SUBSCRIPTION-ID"
#
#
# Verify the current/default Azure CLI context:
#
# az account show --query "{User:user.name,Tenant:tenantId,Subscription:name,SubscriptionId:id}" -o table
#
#
# The Python script uses:
#
#     AzureCliCredential()
#
# and therefore uses the credentials from the current
# Azure CLI login.
#
# The script does NOT hardcode:
#
#     - Tenant ID
#     - Subscription ID
#     - Azure CLI installation path
#
# ---------------------------------------------------------


"""
SEIR-1
Azure Python Connectivity Test

Purpose:
    Prove that the student's local computer can:

    1. Run Python.
    2. Import the Azure SDK.
    3. Authenticate to Azure using Azure CLI credentials.
    4. Identify the current Azure CLI subscription.
    5. Access the current Azure CLI subscription.
    6. Query Azure Resource Groups.

PowerShell equivalent:

    Connect-AzAccount
    Get-AzContext
    Get-AzSubscription
    Set-AzContext
    Get-AzResourceGroup
"""


import sys
import shutil
import subprocess


# ---------------------------------------------------------
# GATE 1
# Verify Python
# ---------------------------------------------------------

print("=" * 60)
print("SEIR AZURE PYTHON CONNECTIVITY TEST")
print("=" * 60)

print("\n[GATE 1] Checking Python...")

print(f"Python Version: {sys.version.split()[0]}")
print(f"Python Executable: {sys.executable}")

if sys.version_info < (3, 8):

    print("\nFAIL: Python 3.8 or newer is required.")
    sys.exit(1)

print("PASS: Python is operational.")


# ---------------------------------------------------------
# GATE 2
# Verify Azure Python SDK
# ---------------------------------------------------------

print("\n[GATE 2] Checking Azure Python SDK...")

try:

    from azure.identity import AzureCliCredential

    from azure.mgmt.resource.resources import (
        ResourceManagementClient,
    )

except ImportError as error:

    print("\nFAIL: Required Azure Python modules are not installed.")
    print()
    print("Run:")
    print()
    print(
        "python -m pip install "
        "azure-identity azure-mgmt-resource"
    )

    print(f"\nPython Error: {error}")

    sys.exit(1)

print("PASS: Azure Python SDK is installed.")


# ---------------------------------------------------------
# GATE 3
# Authenticate using Azure CLI credentials
# ---------------------------------------------------------

print("\n[GATE 3] Connecting to Azure...")

print(
    "\nUsing the credentials from your Azure CLI login."
)

print(
    "If you have not logged in yet, run:"
    "\n\n    az login"
)

try:

    # -----------------------------------------------------
    # Locate Azure CLI
    #
    # shutil.which() searches the operating system PATH.
    #
    # This avoids hardcoding an Azure CLI installation path
    # and makes the script portable.
    # -----------------------------------------------------

    az_command = shutil.which("az")

    if not az_command:

        print("\nFAIL: Azure CLI (az) was not found.")

        print(
            "\nMake sure Azure CLI is installed and "
            "available in your PATH."
        )

        print(
            "\nVerify with:"
            "\n\n    az --version"
        )

        sys.exit(1)


    # -----------------------------------------------------
    # Create an Azure CLI credential.
    #
    # This uses the credentials from:
    #
    #     az login
    #
    # It does NOT open a browser.
    # -----------------------------------------------------

    credential = AzureCliCredential()


    # -----------------------------------------------------
    # Get the current/default subscription from Azure CLI.
    #
    # This is the subscription selected by:
    #
    #     az account set --subscription ...
    # -----------------------------------------------------

    subscription_id = subprocess.check_output(
        [
            az_command,
            "account",
            "show",
            "--query",
            "id",
            "-o",
            "tsv",
        ],
        text=True,
    ).strip()


    if not subscription_id:

        print(
            "\nFAIL: Azure CLI does not have "
            "a current subscription."
        )

        print(
            "\nRun:"
            "\n    az login"
            "\n    az account list -o table"
            "\n    az account set --subscription \"SUBSCRIPTION-ID\""
        )

        sys.exit(1)


    # -----------------------------------------------------
    # Get the current/default tenant from Azure CLI.
    # -----------------------------------------------------

    tenant_id = subprocess.check_output(
        [
            az_command,
            "account",
            "show",
            "--query",
            "tenantId",
            "-o",
            "tsv",
        ],
        text=True,
    ).strip()


    # -----------------------------------------------------
    # Get the currently logged-in Azure account.
    # -----------------------------------------------------

    account_name = subprocess.check_output(
        [
            az_command,
            "account",
            "show",
            "--query",
            "user.name",
            "-o",
            "tsv",
        ],
        text=True,
    ).strip()


    # -----------------------------------------------------
    # Request an Azure management token.
    #
    # This forces AzureCliCredential to authenticate now
    # instead of waiting until the first ARM API call.
    # -----------------------------------------------------

    credential.get_token(
        "https://management.azure.com/.default"
    )


except FileNotFoundError:

    print(
        "\nFAIL: Azure CLI (az) could not be executed."
    )

    print(
        "\nVerify Azure CLI installation with:"
        "\n\n    az --version"
    )

    sys.exit(1)


except subprocess.CalledProcessError as error:

    print(
        "\nFAIL: Could not read the Azure CLI account."
    )

    print(
        "\nMake sure you have run:"
        "\n\n    az login"
    )

    print(f"\nError:\n{error}")

    sys.exit(1)


except Exception as error:

    print("\nFAIL: Azure authentication failed.")
    print(f"\nError:\n{error}")

    sys.exit(1)


print("\nPASS: Azure authentication successful.")


# ---------------------------------------------------------
# GATE 4
# Verify current Azure CLI subscription
# ---------------------------------------------------------

print("\n[GATE 4] Checking Azure subscription...")

try:

    # -----------------------------------------------------
    # Create a Resource Management client using the
    # subscription selected in the Azure CLI.
    # -----------------------------------------------------

    resource_client = ResourceManagementClient(
        credential,
        subscription_id,
    )


    # -----------------------------------------------------
    # Query Resource Groups.
    #
    # This verifies that the authenticated identity actually
    # has access to the selected subscription.
    # -----------------------------------------------------

    resource_groups = list(
        resource_client.resource_groups.list()
    )


except Exception as error:

    print(
        "\nFAIL: Could not access Azure subscription."
    )

    print(f"\nError:\n{error}")

    sys.exit(1)


print(
    "PASS: Azure subscription is accessible."
)


# ---------------------------------------------------------
# GATE 5
# Select current Azure CLI subscription
# ---------------------------------------------------------

print("\n[GATE 5] Selecting Azure subscription...")

selected_subscription_id = subscription_id

print(
    f"PASS: Using Azure CLI default subscription:"
    f"\n      {selected_subscription_id}"
)


# ---------------------------------------------------------
# Display Resource Groups
# ---------------------------------------------------------

print("\nRESOURCE GROUPS")
print("-" * 60)

if not resource_groups:

    print(
        "No resource groups currently exist "
        "in this subscription."
    )

else:

    for resource_group in resource_groups:

        print(
            f"{resource_group.name:<35} "
            f"{resource_group.location}"
        )


# ---------------------------------------------------------
# Final Report
# ---------------------------------------------------------

print("\n")
print("=" * 60)
print("AZURE CONNECTIVITY REPORT")
print("=" * 60)

print("Python:               PASS")
print("Azure SDK:            PASS")
print("Azure Authentication: PASS")
print("Subscription Query:   PASS")
print("ARM Resource Query:   PASS")

print()

print(
    f"Azure Account:        {account_name}"
)

print(
    f"Subscription ID:      {selected_subscription_id}"
)

print(
    f"Tenant ID:            {tenant_id}"
)

print(
    f"Resource Groups:      {len(resource_groups)}"
)

print()
print("=== TEST COMPLETE ===")
