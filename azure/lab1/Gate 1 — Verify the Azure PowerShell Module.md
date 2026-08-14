# Azure PowerShell Initial Connectivity Lab

## Objective

In this lab, you will establish an initial connection to Microsoft Azure using PowerShell.

You will:

1. Verify that the Azure PowerShell module is installed.
2. Authenticate to Azure.
3. Verify your Azure account context.
4. Identify your available Azure subscriptions.
5. Select the correct subscription.
6. Verify that you can access Azure resources.

---

## Gate 1 — Verify the Azure PowerShell Module

Check whether the Azure PowerShell `Az` module is installed.

```powershell
Get-Module -ListAvailable Az.Accounts
```

If the Azure PowerShell module is not installed, install it from the PowerShell Gallery:

```powershell
Install-Module -Name Az -Repository PSGallery -Force
```

---

## Gate 2 — Connect to Azure

Authenticate to Azure using your user account:

```powershell
Connect-AzAccount
```

A Microsoft authentication window should appear.

Sign in using the account associated with your Azure environment.

### Alternative: Device Authentication

If interactive browser authentication is unavailable, use device authentication:

```powershell
Connect-AzAccount -UseDeviceAuthentication
```

Follow the instructions displayed in the PowerShell terminal.

---

## Gate 3 — Verify Your Azure Context

After authentication, determine which Azure identity, tenant, and subscription PowerShell is currently using:

```powershell
Get-AzContext
```

Review the following information:

- Account
- Subscription Name
- Subscription ID
- Tenant ID
- Azure Environment

> **Important:** Successfully authenticating to Azure does not necessarily mean you are connected to the correct subscription.

---

## Gate 4 — View Available Subscriptions

Display the Azure subscriptions available to your account:

```powershell
Get-AzSubscription
```

Identify the subscription that you will use for this lab.

---

## Gate 5 — Select the Correct Subscription

Set your PowerShell session to use the appropriate Azure subscription:

```powershell
Set-AzContext -Subscription "<subscription-name-or-id>"
```

Example:

```powershell
Set-AzContext -Subscription "Azure Lab Subscription"
```

Verify the context again:

```powershell
Get-AzContext
```

Confirm that the expected subscription is now active.

---

## Gate 6 — Verify Access to Azure Resources

List the resource groups available in the selected subscription:

```powershell
Get-AzResourceGroup
```

If resource groups are returned, you have successfully:

- Authenticated to Azure
- Connected to an Azure tenant
- Selected a subscription
- Accessed Azure resources through PowerShell

---

# Connectivity Workflow

The initial Azure PowerShell connectivity workflow is:

```text
PowerShell
    |
    v
Az PowerShell Module
    |
    v
Azure Authentication
    |
    v
Azure Tenant
    |
    v
Azure Subscription
    |
    v
Azure Resources
```

---

# Final Verification

Run the following commands:

```powershell
Connect-AzAccount

Get-AzContext

Get-AzSubscription

Set-AzContext -Subscription "<your-subscription>"

Get-AzContext

Get-AzResourceGroup
```

## Success Criteria

You have completed the lab when:

- [ ] The Azure PowerShell `Az` module is installed.
- [ ] `Connect-AzAccount` completes successfully.
- [ ] `Get-AzContext` displays your Azure account.
- [ ] You can identify your Azure tenant.
- [ ] You can identify your Azure subscription.
- [ ] The correct subscription is selected.
- [ ] `Get-AzResourceGroup` successfully queries Azure.

---

## Key Concept

Before administering Azure through PowerShell, always know:

> **Which identity am I using, which tenant am I connected to, and which subscription am I operating against?**

Authentication tells Azure **who you are**.

Your Azure context determines **where your commands will execute**.
