
# Azure PowerShell Connectivity Lab

## Purpose

The purpose of this lab is to verify that your local computer is capable of connecting to Microsoft Azure using PowerShell.

This is a **technical readiness lab**.

Before we begin creating users, groups, virtual machines, networks, or other Azure resources, we need to prove that your local workstation can:

1. Run PowerShell.
2. Run the Azure PowerShell modules.
3. Authenticate to Microsoft Azure.
4. Identify the correct Azure tenant and subscription.
5. Query Azure successfully from the command line.

> **Important**
>
> The objective of this lab is to verify your **local workstation environment**.
>
> Using Azure Cloud Shell in a browser does **not** satisfy this lab requirement.

---

# Gate 1 — Local PowerShell Readiness

## Objective

Prove that your computer can run PowerShell and the Azure PowerShell module.

You must complete this gate on the computer you intend to use for class.

---

## Windows Users

### Step 1 — Open PowerShell

Open PowerShell.

If PowerShell 7 is installed, you can start it by running:

```powershell
pwsh
```

Check your PowerShell version:

```powershell
$PSVersionTable
```

You should be able to identify the following:

```text
PSVersion
PSEdition
OS
Platform
```

---

### Step 2 — Install PowerShell 7 if Necessary

If PowerShell 7 is not installed and your system supports `winget`, you can install it with:

```powershell
winget install --id Microsoft.PowerShell --source winget
```

After installation, close and reopen your terminal.

Then run:

```powershell
pwsh
```

---

## macOS Users

macOS does not include PowerShell by default.

You will need to install PowerShell before continuing.

### Step 1 — Open Terminal

Open:

```text
Applications
    |
    +-- Utilities
            |
            +-- Terminal
```

Or use Spotlight:

```text
Command + Space
```

Search for:

```text
Terminal
```

---

### Step 2 — Start PowerShell

If PowerShell is already installed, run:

```bash
pwsh
```

Your prompt should change to something similar to:

```text
PS /Users/student>
```

Verify PowerShell:

```powershell
$PSVersionTable
```

---

### Step 3 — If PowerShell Is Not Installed

Install PowerShell 7 using the approved installation method for your Mac.

After installation, return to Terminal and run:

```bash
pwsh
```

Then verify:

```powershell
$PSVersionTable
```

---

# Important Device Requirement

This lab requires a computer capable of running a local PowerShell environment.

Examples of acceptable systems include:

* Windows laptop or desktop
* macOS laptop or desktop
* Supported Linux workstation

The following do **not** meet the objective of this lab:

* Browser-only device
* iPad used without a supported local PowerShell environment
* Chromebook used only through a browser
* Computer where you cannot install or execute the required tools
* Computer where organizational restrictions prevent the required commands from running

If your computer cannot complete Gate 1, **stop here and notify the instructor**.

Do not move to Gate 2.

---

# Verify the Azure PowerShell Module

Check whether the Azure PowerShell module is installed:

```powershell
Get-Module -ListAvailable Az.Accounts
```

If information about `Az.Accounts` appears, continue.

If nothing is returned, install the Azure PowerShell module:

```powershell
Install-Module -Name Az -Repository PSGallery -Scope CurrentUser -Force
```

Using:

```text
-Scope CurrentUser
```

installs the module for your user account.

After installation, verify again:

```powershell
Get-Module -ListAvailable Az.Accounts
```

---

# Gate 1 Verification

Run:

```powershell
$PSVersionTable

Get-Module -ListAvailable Az.Accounts
```

You have passed **Gate 1** when:

* [ ] PowerShell starts successfully.
* [ ] `$PSVersionTable` returns information.
* [ ] The `Az.Accounts` module is installed.
* [ ] PowerShell accepts Azure PowerShell commands.

---

# Gate 2 — Connect to Azure

## Objective

Prove that your local PowerShell session can authenticate to Microsoft Azure.

Run:

```powershell
Connect-AzAccount
```

A Microsoft authentication process should begin.

Sign in using the Azure account assigned to you for this course.

---

## Alternative Authentication Method

If the normal interactive login does not work, try:

```powershell
Connect-AzAccount -UseDeviceAuthentication
```

Follow the authentication instructions displayed in the terminal.

---

# Verify Your Azure Context

After authentication succeeds, run:

```powershell
Get-AzContext
```

Look for:

```text
Account
SubscriptionName
SubscriptionId
TenantId
Environment
```

Example:

```text
Account          : student@example.com
SubscriptionName : Azure Lab
SubscriptionId   : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
TenantId         : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment      : AzureCloud
```

Your values will be different.

---

# View Available Subscriptions

Run:

```powershell
Get-AzSubscription
```

You may see one or more Azure subscriptions.

Identify the subscription you are supposed to use for class.

---

# Set the Correct Subscription

If necessary, select your subscription:

```powershell
Set-AzContext -Subscription "<subscription-name-or-id>"
```

Example:

```powershell
Set-AzContext -Subscription "SEIR Student Azure"
```

Verify again:

```powershell
Get-AzContext
```

---

# Test Azure Resource Access

Run:

```powershell
Get-AzResourceGroup
```

This command asks Azure for the resource groups available in your current subscription.

The important part of this step is that Azure responds successfully.

Your subscription may contain many resource groups, one resource group, or possibly none.

---

# Gate 2 Verification

Run the complete sequence:

```powershell
Connect-AzAccount

Get-AzContext

Get-AzSubscription

Get-AzResourceGroup
```

You have passed **Gate 2** when:

* [ ] `Connect-AzAccount` completes successfully.
* [ ] `Get-AzContext` displays your Azure account.
* [ ] A Tenant ID is displayed.
* [ ] A Subscription ID is displayed.
* [ ] You can identify the subscription you are using.
* [ ] `Get-AzResourceGroup` completes without an authentication or connection error.

---

# Final Connectivity Test

Run:

```powershell
Write-Host "=== AZURE POWERSHELL CONNECTIVITY TEST ==="

Write-Host "`nPOWERSHELL VERSION:"
$PSVersionTable.PSVersion

Write-Host "`nAZURE CONTEXT:"
Get-AzContext

Write-Host "`nRESOURCE GROUP TEST:"
Get-AzResourceGroup

Write-Host "`n=== TEST COMPLETE ==="
```

---

# Submission

Paste the results of the connectivity test into the class chat.

You may submit:

```text
PowerShell Version
Account
Subscription Name
Environment
Successful Resource Group Query
```

Do **not** paste:

* Passwords
* Temporary passwords
* Authentication codes
* Access tokens
* Refresh tokens
* Client secrets
* Private keys

Example submission:

```text
=== AZURE POWERSHELL CONNECTIVITY TEST ===

PowerShell Version: 7.x

Account:
student@example.com

Subscription:
SEIR Student Azure

Environment:
AzureCloud

Resource Group Query:
SUCCESS

=== TEST COMPLETE ===
```

---

# If You Cannot Complete the Lab

If a command fails, do not simply write:

```text
It doesn't work.
```

Record:

1. Which gate failed.
2. Which command failed.
3. The error message.
4. Which operating system you are using.
5. Whether you are using your own computer or another computer.

Example:

```text
Gate: Gate 1

Operating System:
macOS

Command:
pwsh

Result:
command not found

Status:
PowerShell is not installed.
```

Another example:

```text
Gate: Gate 2

Operating System:
Windows 11

Command:
Connect-AzAccount

Result:
Authentication failed.

Status:
PowerShell works and Az is installed, but Azure authentication did not complete.
```

---

# Troubleshooting Philosophy

Do not troubleshoot everything at once.

Follow the gates.

```text
LOCAL COMPUTER
      |
      v
PowerShell Runs
      |
      v
Az Module Installed
      |
      v
Connect-AzAccount
      |
      v
Azure Authentication
      |
      v
Correct Tenant
      |
      v
Correct Subscription
      |
      v
Azure Resource Query
```

If one layer fails, stop and troubleshoot that layer before continuing.

---

# Success Criteria

At the end of this lab, you should be able to truthfully say:

> I have a computer capable of running PowerShell locally.

> I have the Azure PowerShell module installed.

> I can authenticate to Azure from PowerShell.

> I know which tenant and subscription my commands are using.

> I can query Azure resources from my local computer.

Once both gates are complete, you are ready for the next lab.
