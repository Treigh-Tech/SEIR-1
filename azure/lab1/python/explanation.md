# Azure Connectivity with Python and PowerShell

## Purpose

The purpose of this exercise is to demonstrate that **PowerShell and Python can perform many of the same Azure administration tasks**.

Earlier, we connected to Azure using PowerShell.

We used commands such as:

```powershell
Connect-AzAccount
Get-AzContext
Get-AzSubscription
Get-AzResourceGroup
```

The Python script performs essentially the same workflow.

The difference is the tool being used.

```text
PowerShell
    |
    +---- Az PowerShell Module
    |
    v
Azure APIs
```

and:

```text
Python
    |
    +---- Azure Python SDK
    |
    v
Azure APIs
```

Both ultimately communicate with Microsoft Azure.

---

# The Important Concept

PowerShell is **not Azure**.

Python is **not Azure**.

They are clients that communicate with Azure services.

Conceptually:

```text
                  Microsoft Azure
                        ^
                        |
                 Azure APIs / ARM
                        ^
                        |
             +----------+----------+
             |                     |
             |                     |
        PowerShell               Python
             |                     |
        Az Module             Azure SDK
```

This is why many administrative tasks can be performed using either language.

---

# PowerShell Version

Our PowerShell connectivity workflow looked like this:

```powershell
Connect-AzAccount

Get-AzContext

Get-AzSubscription

Get-AzResourceGroup
```

The process is:

```text
Start PowerShell
      |
      v
Load Az Module
      |
      v
Authenticate
      |
      v
Discover Subscription
      |
      v
Query Azure Resources
```

---

# Python Version

The Python script follows the same basic process:

```text
Start Python
      |
      v
Load Azure SDK
      |
      v
Authenticate
      |
      v
Discover Subscription
      |
      v
Query Azure Resources
```

The syntax is different.

The objective is the same.

---

# Gate 1 — Verify the Local Runtime

## PowerShell

In PowerShell, we checked the installed version:

```powershell
$PSVersionTable
```

This proves that PowerShell is actually running on the local computer.

---

## Python

The Python script performs a similar check:

```python
import sys

print(sys.version)
```

The script also verifies that an acceptable version of Python is being used:

```python
if sys.version_info < (3, 8):
    print("FAIL: Python 3.8 or newer is required.")
    sys.exit(1)
```

The concept is the same:

```text
Can this computer actually run the required language?
```

---

# Gate 2 — Verify Azure Tooling

PowerShell and Python require different Azure libraries.

## PowerShell

PowerShell uses the Azure `Az` module.

We checked for it using:

```powershell
Get-Module -ListAvailable Az.Accounts
```

If necessary, we installed it:

```powershell
Install-Module -Name Az -Repository PSGallery -Scope CurrentUser
```

---

## Python

Python uses Microsoft's Azure SDK packages.

For this lab, we use:

```text
azure-identity
azure-mgmt-resource
```

They can be installed using:

```bash
python -m pip install azure-identity azure-mgmt-resource
```

The Python script then attempts to import them:

```python
from azure.identity import InteractiveBrowserCredential

from azure.mgmt.resource import (
    ResourceManagementClient,
    SubscriptionClient,
)
```

If Python cannot import these modules, the Azure SDK is not properly installed.

---

# Comparison

```text
PowerShell
Get-Module Az.Accounts
        |
        v
Is the Az Module Installed?


Python
import azure.identity
        |
        v
Is the Azure SDK Installed?
```

Same concept.

Different implementation.

---

# Gate 3 — Authenticate to Azure

Authentication answers the question:

> **Who are you?**

Azure must know which identity is making the request.

---

## PowerShell

PowerShell uses:

```powershell
Connect-AzAccount
```

This launches the Microsoft authentication process.

After successful authentication, PowerShell obtains the credentials necessary to communicate with Azure.

---

## Python

Python uses:

```python
credential = InteractiveBrowserCredential()
```

The script then requests an Azure access token:

```python
credential.get_token(
    "https://management.azure.com/.default"
)
```

This causes Microsoft authentication to occur.

A browser window normally opens and asks the student to authenticate.

---

# Comparison

```text
PowerShell

Connect-AzAccount
        |
        v
Microsoft Login
        |
        v
Authentication Token
```

```text
Python

InteractiveBrowserCredential()
        |
        v
Microsoft Login
        |
        v
Authentication Token
```

Again, the syntax is different.

The authentication concept is the same.

---

# What Is an Access Token?

After authentication, Azure does not expect your password to be sent with every request.

Instead, the authentication system provides an **access token**.

Conceptually:

```text
Username + Authentication
          |
          v
Microsoft Identity Platform
          |
          v
Access Token
          |
          v
Azure API
```

The Python Azure SDK manages much of this process for us.

PowerShell's Az module does the same.

---

# Gate 4 — Discover Azure Subscriptions

After authentication, we need to know:

> **Which Azure subscription can this identity access?**

---

## PowerShell

We used:

```powershell
Get-AzSubscription
```

Example:

```text
Name                  Id
----                  --
SEIR Student Azure    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

## Python

Python creates a `SubscriptionClient`:

```python
subscription_client = SubscriptionClient(credential)
```

Then asks Azure for the available subscriptions:

```python
subscriptions = list(
    subscription_client.subscriptions.list()
)
```

The script can then examine information such as:

```python
subscription.display_name
subscription.subscription_id
subscription.state
```

---

# Comparison

PowerShell:

```powershell
Get-AzSubscription
```

Python:

```python
subscription_client.subscriptions.list()
```

Both are essentially asking Azure:

```text
Which subscriptions can this authenticated identity access?
```

---

# Gate 5 — Select a Subscription

An Azure account may have access to more than one subscription.

Therefore, before managing resources, we need to determine which subscription should be used.

---

## PowerShell

PowerShell allows us to set the active subscription:

```powershell
Set-AzContext -Subscription "<subscription-id>"
```

We can then verify it with:

```powershell
Get-AzContext
```

---

## Python

Python usually supplies the subscription ID directly when creating a management client:

```python
resource_client = ResourceManagementClient(
    credential,
    subscription_id
)
```

Notice the second argument:

```python
subscription_id
```

That tells the client:

> Perform resource operations against this Azure subscription.

---

# Comparison

PowerShell stores the selected subscription in the current Azure context:

```text
Set-AzContext
      |
      v
Current Subscription
```

Python passes the subscription explicitly to the management client:

```text
ResourceManagementClient
      |
      +---- credential
      |
      +---- subscription_id
```

This is an important difference in programming style.

The underlying requirement is still the same:

> Azure must know which subscription the request applies to.

---

# Gate 6 — Query Azure Resource Groups

Now we test whether the student can actually communicate with Azure Resource Manager.

---

## PowerShell

We used:

```powershell
Get-AzResourceGroup
```

This retrieves the resource groups available in the selected subscription.

---

## Python

Python creates an Azure Resource Management client:

```python
resource_client = ResourceManagementClient(
    credential,
    subscription_id
)
```

Then retrieves the resource groups:

```python
resource_groups = list(
    resource_client.resource_groups.list()
)
```

---

# Comparison

PowerShell:

```powershell
Get-AzResourceGroup
```

Python:

```python
resource_client.resource_groups.list()
```

Both result in a request similar to:

```text
Authenticated User
       |
       v
Azure Resource Manager
       |
       v
Subscription
       |
       v
Resource Groups
```

---

# PowerShell Commands vs Python Code

| Objective             | PowerShell               | Python                                         |
| --------------------- | ------------------------ | ---------------------------------------------- |
| Verify runtime        | `$PSVersionTable`        | `sys.version`                                  |
| Verify Azure tools    | `Get-Module Az.Accounts` | `import azure.identity`                        |
| Authenticate          | `Connect-AzAccount`      | `InteractiveBrowserCredential()`               |
| View subscriptions    | `Get-AzSubscription`     | `SubscriptionClient(...).subscriptions.list()` |
| Select subscription   | `Set-AzContext`          | Pass `subscription_id` to the client           |
| Query resource groups | `Get-AzResourceGroup`    | `resource_client.resource_groups.list()`       |

The syntax is different.

The workflow is almost identical.

---

# Cmdlets vs Objects

PowerShell often hides many implementation details behind convenient commands called **cmdlets**.

For example:

```powershell
Get-AzResourceGroup
```

This command performs several tasks internally.

Python normally requires us to be more explicit.

We first create a client:

```python
resource_client = ResourceManagementClient(
    credential,
    subscription_id
)
```

Then we call a method:

```python
resource_client.resource_groups.list()
```

Conceptually:

```text
PowerShell

Get-AzResourceGroup
```

is similar to:

```text
Python

ResourceManagementClient
        |
        v
resource_groups
        |
        v
list()
```

---

# The Azure SDK Uses Objects

Consider:

```python
selected_subscription.display_name
```

and:

```python
selected_subscription.subscription_id
```

`selected_subscription` is not simply a line of text.

It is a Python object containing information about an Azure subscription.

PowerShell also works heavily with objects.

For example:

```powershell
$subscription = Get-AzSubscription
```

Then:

```powershell
$subscription.Name
$subscription.Id
```

This means both languages support an important automation pattern:

```text
REQUEST OBJECT
     |
     v
STORE OBJECT
     |
     v
READ PROPERTIES
     |
     v
USE PROPERTIES IN ANOTHER OPERATION
```

---

# Error Handling

The Python script also introduces explicit error handling.

Example:

```python
try:

    credential = InteractiveBrowserCredential()

    credential.get_token(
        "https://management.azure.com/.default"
    )

except Exception as error:

    print("FAIL: Azure authentication failed.")
    print(error)

    sys.exit(1)
```

The structure is:

```text
TRY OPERATION
     |
     +---- SUCCESS ----> Continue
     |
     +---- FAILURE ----> Report Error
                           |
                           v
                        Stop Script
```

This is useful for automation because the script can determine exactly which gate failed.

---

# Why the Script Uses Gates

The script deliberately separates the test into gates.

```text
Gate 1
Python Works
     |
     v
Gate 2
Azure SDK Works
     |
     v
Gate 3
Authentication Works
     |
     v
Gate 4
Subscription Discovery Works
     |
     v
Gate 5
Subscription Selected
     |
     v
Gate 6
Azure Resource Manager Works
```

If Gate 2 fails, there is little reason to troubleshoot Azure authentication.

If Gate 3 fails, there is little reason to troubleshoot resource groups.

We troubleshoot the **first failed layer**.

---

# Diagnostic Comparison

Running both the PowerShell and Python tests gives us useful information.

## Scenario 1

```text
PowerShell: FAIL
Python:     FAIL
```

Likely areas to investigate:

```text
Computer
Operating System
Network
Authentication
Azure Account
Permissions
```

---

## Scenario 2

```text
PowerShell: PASS
Python:     FAIL
```

Azure connectivity probably works.

Investigate:

```text
Python
pip
Virtual Environment
Azure Python SDK
Python Configuration
```

---

## Scenario 3

```text
PowerShell: FAIL
Python:     PASS
```

Azure connectivity is demonstrably working.

Investigate:

```text
PowerShell
Az Module
PowerShell Version
PowerShell Configuration
```

---

## Scenario 4

```text
PowerShell: PASS
Python:     PASS
```

Excellent.

Both local administration environments can communicate with Azure.

---

# Architecture

The most important architecture from this lab is:

```text
                     Microsoft Azure
                           |
                           |
                  Azure Resource Manager
                           |
                     Azure REST APIs
                           |
              +------------+------------+
              |                         |
              |                         |
        Az PowerShell              Azure Python SDK
              |                         |
              |                         |
         PowerShell                   Python
              |                         |
              +------------+------------+
                           |
                           v
                  Student Workstation
```

The student is not learning two completely unrelated technologies.

The student is learning **two ways to control the same cloud platform**.

---

# Why Learn Both?

PowerShell is extremely useful for:

```text
Interactive Administration
Microsoft Environments
Identity Administration
Azure Administration
Quick Operational Tasks
```

Python is extremely useful for:

```text
Automation
Applications
APIs
Cloud Engineering
Data Processing
AI
Agentic Systems
Larger Software Projects
```

A cloud engineer should understand that the underlying platform remains the same regardless of the client language.

---

# Final Comparison

PowerShell:

```powershell
Connect-AzAccount

Get-AzSubscription

Set-AzContext -Subscription "<subscription>"

Get-AzResourceGroup
```

Python:

```python
credential = InteractiveBrowserCredential()

subscription_client = SubscriptionClient(
    credential
)

subscriptions = subscription_client.subscriptions.list()

resource_client = ResourceManagementClient(
    credential,
    subscription_id
)

resource_groups = resource_client.resource_groups.list()
```

Different syntax.

Same general workflow:

```text
AUTHENTICATE
      |
      v
IDENTIFY SUBSCRIPTION
      |
      v
CREATE MANAGEMENT CONTEXT
      |
      v
QUERY AZURE
```

---

# Key Concept

Do not think:

> PowerShell manages Azure.

or:

> Python manages Azure.

Instead, think:

> PowerShell and Python are tools that allow us to communicate with Azure services and APIs.

Once you understand the underlying workflow, changing languages becomes much easier.

The syntax changes.

The cloud architecture does not.
