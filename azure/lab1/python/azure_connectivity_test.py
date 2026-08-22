# you need this first
# python -m pip install azure-identity azure-mgmt-resource azure-mgmt-resource-subscriptions


"""
SEIR-1
Azure Python Connectivity Test

Purpose:
    Prove that the student's local computer can:

    1. Run Python.
    2. Import the Azure SDK.
    3. Authenticate to Azure.
    4. Discover Azure subscriptions.
    5. Select an Azure subscription.
    6. Query Azure Resource Groups.

PowerShell equivalent:

    Connect-AzAccount
    Get-AzContext
    Get-AzSubscription
    Set-AzContext
    Get-AzResourceGroup
"""

import sys


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

if sys.version_info < (3, 9):
    print("\nFAIL: Python 3.9 or newer is required.")
    sys.exit(1)

print("PASS: Python is operational.")


# ---------------------------------------------------------
# GATE 2
# Verify Azure Python SDK
# ---------------------------------------------------------

print("\n[GATE 2] Checking Azure Python SDK...")

try:
    from azure.identity import InteractiveBrowserCredential
    from azure.mgmt.resource.resources import ResourceManagementClient
    from azure.mgmt.resource.subscriptions import SubscriptionClient

except ImportError as error:

    print("\nFAIL: Required Azure Python modules are not installed.")
    print()
    print("Run:")
    print()
    print(
        "python -m pip install "
        "azure-identity azure-mgmt-resource "
        "azure-mgmt-resource-subscriptions"
    )

    print(f"\nPython Error: {error}")

    sys.exit(1)

print("PASS: Azure Python SDK is installed.")


# ---------------------------------------------------------
# GATE 3
# Authenticate to Azure
# ---------------------------------------------------------

print("\n[GATE 3] Connecting to Azure...")

print(
    "\nA browser window should open.\n"
    "Sign in using the Azure account assigned to you."
)

try:

    credential = InteractiveBrowserCredential()

    # Requesting a token forces authentication to occur now.
    credential.get_token(
        "https://management.azure.com/.default"
    )

except Exception as error:

    print("\nFAIL: Azure authentication failed.")
    print(f"\nError:\n{error}")

    sys.exit(1)

print("\nPASS: Azure authentication successful.")


# ---------------------------------------------------------
# GATE 4
# Discover subscriptions
# ---------------------------------------------------------

print("\n[GATE 4] Discovering Azure subscriptions...")

try:

    subscription_client = SubscriptionClient(credential)

    subscriptions = list(
        subscription_client.subscriptions.list()
    )

except Exception as error:

    print("\nFAIL: Could not query Azure subscriptions.")
    print(f"\nError:\n{error}")

    sys.exit(1)


if not subscriptions:

    print("\nFAIL: No Azure subscriptions were found.")
    sys.exit(1)


print(
    f"PASS: Found {len(subscriptions)} "
    f"Azure subscription(s).\n"
)


# ---------------------------------------------------------
# Display subscriptions
# ---------------------------------------------------------

for number, subscription in enumerate(subscriptions, start=1):

    print(f"[{number}] {subscription.display_name}")
    print(f"    Subscription ID: {subscription.subscription_id}")
    print(f"    State: {subscription.state}")

    tenant_id = getattr(subscription, "tenant_id", None)

    if tenant_id:
        print(f"    Tenant ID: {tenant_id}")

    print()


# ---------------------------------------------------------
# GATE 5
# Select subscription
# ---------------------------------------------------------

print("[GATE 5] Selecting Azure subscription...")


if len(subscriptions) == 1:

    selected_subscription = subscriptions[0]

    print(
        "Only one subscription is available. "
        "Selecting it automatically."
    )

else:

    while True:

        try:

            selection = int(
                input(
                    f"Select subscription "
                    f"[1-{len(subscriptions)}]: "
                )
            )

            if 1 <= selection <= len(subscriptions):

                selected_subscription = subscriptions[
                    selection - 1
                ]

                break

            print("Invalid selection.")

        except ValueError:

            print("Enter a number.")


subscription_id = selected_subscription.subscription_id


print("\nSelected Subscription:")
print(f"Name: {selected_subscription.display_name}")
print(f"ID:   {subscription_id}")

tenant_id = getattr(
    selected_subscription,
    "tenant_id",
    None,
)

if tenant_id:
    print(f"Tenant ID: {tenant_id}")

print("\nPASS: Azure subscription selected.")


# ---------------------------------------------------------
# GATE 6
# Query Resource Groups
# ---------------------------------------------------------

print("\n[GATE 6] Testing Azure Resource Manager access...")

try:

    resource_client = ResourceManagementClient(
        credential,
        subscription_id,
    )

    resource_groups = list(
        resource_client.resource_groups.list()
    )

except Exception as error:

    print("\nFAIL: Azure Resource Manager query failed.")
    print(f"\nError:\n{error}")

    sys.exit(1)


print("PASS: Azure Resource Manager responded successfully.")


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
    f"Subscription: "
    f"{selected_subscription.display_name}"
)

print(
    f"Subscription ID: "
    f"{subscription_id}"
)

if tenant_id:

    print(
        f"Tenant ID: "
        f"{tenant_id}"
    )

print(
    f"Resource Groups: "
    f"{len(resource_groups)}"
)

print()
print("=== TEST COMPLETE ===")
