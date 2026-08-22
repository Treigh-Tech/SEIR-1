# SEIR Azure Python Connectivity Runbook

## Purpose

This runbook is for students who need step-by-step instructions for running the Azure Python connectivity script.

The goal is simple:

1. Verify Python is installed.
2. Verify the Azure Python SDK is installed.
3. Run the script.
4. Authenticate to Azure.
5. Verify the script can read your Azure subscription and resource groups.

The script file should be named:

```text
azure_connectivity_test.py
```

---

# Step 1 — Confirm You Have the Script

Locate the file:

```text
azure_connectivity_test.py
```

It may be in:

* Downloads
* Documents
* Desktop
* A GitHub repository
* A class folder

Do not continue until you know where the file is located.

---

# Step 2 — Open a Terminal

## Windows

Open one of the following:

* PowerShell
* Windows Terminal
* Command Prompt

PowerShell or Windows Terminal is recommended.

You can press:

```text
Windows Key
```

Then type:

```text
PowerShell
```

or:

```text
Windows Terminal
```

and open the application.

---

## macOS

Open:

```text
Applications
    |
    +-- Utilities
            |
            +-- Terminal
```

You can also press:

```text
Command + Space
```

Then type:

```text
Terminal
```

and press **Enter**.

---

# Step 3 — Verify Python

Run:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

A successful result should look similar to:

```text
Python 3.12.4
```

If Python is not found, stop and install Python before continuing.

---

# Step 4 — Determine Which Python Command Works

Some computers use:

```bash
python
```

Other computers use:

```bash
python3
```

Use whichever command successfully displayed your Python version.

For the rest of this runbook, examples will use:

```bash
python
```

If your computer requires `python3`, replace `python` with `python3`.

Example:

```bash
python3 azure_connectivity_test.py
```

---

# Step 5 — Move Into the Folder Containing the Script

Your terminal must be in the same directory as:

```text
azure_connectivity_test.py
```

Use the `cd` command.

---

## Windows Example

If the script is in Downloads:

```powershell
cd $HOME\Downloads
```

If it is on the Desktop:

```powershell
cd $HOME\Desktop
```

If it is inside a class folder:

```powershell
cd $HOME\Documents\SEIR
```

---

## macOS Example

If the script is in Downloads:

```bash
cd ~/Downloads
```

If it is on the Desktop:

```bash
cd ~/Desktop
```

If it is inside a class folder:

```bash
cd ~/Documents/SEIR
```

---

# Step 6 — Verify the File Is Present

## Windows PowerShell

Run:

```powershell
Get-ChildItem
```

You should see:

```text
azure_connectivity_test.py
```

---

## macOS

Run:

```bash
ls
```

You should see:

```text
azure_connectivity_test.py
```

If you do not see the file, you are in the wrong directory.

Do not continue until the file appears.

---

# Step 7 — Install the Required Azure Python Packages

Run:

```bash
python -m pip install azure-identity azure-mgmt-resource
```

If your system uses `python3`, run:

```bash
python3 -m pip install azure-identity azure-mgmt-resource
```

Wait for the installation to complete.

---

# Step 8 — Verify the Packages Installed

Run:

```bash
python -m pip show azure-identity
```

Then:

```bash
python -m pip show azure-mgmt-resource
```

If both commands return package information, continue.

---

# Step 9 — Run the Script

Run:

```bash
python azure_connectivity_test.py
```

If your system uses `python3`, run:

```bash
python3 azure_connectivity_test.py
```

---

# Step 10 — Watch the Gates

The script will begin testing your environment.

You should see output similar to:

```text
============================================================
SEIR AZURE PYTHON CONNECTIVITY TEST
============================================================

[GATE 1] Checking Python...
PASS: Python is operational.

[GATE 2] Checking Azure Python SDK...
PASS: Azure Python SDK is installed.

[GATE 3] Connecting to Azure...
```

The script will stop if one of the gates fails.

---

# Step 11 — Authenticate to Azure

When the script reaches authentication, your web browser should open.

Sign in using the Azure account assigned to you for class.

Do not use another personal Microsoft account unless instructed to do so.

After successful authentication, return to the terminal.

The script should continue automatically.

---

# Step 12 — Select Your Azure Subscription

If your account has access to only one Azure subscription, the script may select it automatically.

If multiple subscriptions exist, the script will display something similar to:

```text
[1] SEIR Student Azure
[2] Personal Subscription
[3] Sandbox
```

You may then see:

```text
Select subscription [1-3]:
```

Enter the number corresponding to the subscription you are supposed to use.

Example:

```text
1
```

Then press **Enter**.

---

# Step 13 — Wait for the Resource Group Test

The script will attempt to query Azure Resource Manager.

You should see:

```text
[GATE 6] Testing Azure Resource Manager access...

PASS: Azure Resource Manager responded successfully.
```

It may also list resource groups.

Example:

```text
RESOURCE GROUPS
------------------------------------------------------------
seir-lab-rg                         eastus
network-rg                          centralus
```

If your subscription contains no resource groups, that is acceptable.

The important result is:

```text
PASS: Azure Resource Manager responded successfully.
```

---

# Step 14 — Verify the Final Report

A successful script should end with something similar to:

```text
============================================================
AZURE CONNECTIVITY REPORT
============================================================

Python:               PASS
Azure SDK:            PASS
Azure Authentication: PASS
Subscription Query:   PASS
ARM Resource Query:   PASS

Subscription: SEIR Student Azure
Subscription ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Resource Groups: 2

=== TEST COMPLETE ===
```

If you see all `PASS` results, the lab is complete.

---

# Step 15 — Submit Your Results

Paste the final connectivity report into the class chat.

Do not paste:

* Passwords
* Authentication codes
* Access tokens
* Refresh tokens
* Client secrets
* Private keys

You may paste:

```text
Python Version
Azure Authentication: PASS
Subscription Query: PASS
ARM Resource Query: PASS
Subscription Name
Resource Group Count
```

---

# If the Script Does Not Run

## Error: Python Is Not Found

Example:

```text
python is not recognized
```

or:

```text
command not found: python
```

Try:

```bash
python3 --version
```

If that also fails, Python is probably not installed.

---

## Error: File Not Found

Example:

```text
can't open file 'azure_connectivity_test.py'
```

You are probably in the wrong directory.

Verify your current folder.

### Windows

```powershell
Get-Location
```

Then:

```powershell
Get-ChildItem
```

### macOS

```bash
pwd
```

Then:

```bash
ls
```

Make sure `azure_connectivity_test.py` appears.

---

# Error: Azure Module Is Missing

Example:

```text
ModuleNotFoundError: No module named 'azure'
```

Install the required packages:

```bash
python -m pip install azure-identity azure-mgmt-resource
```

Then run the script again.

---

# Error: Authentication Failed

If the browser opens but authentication fails:

1. Verify you are using the correct Microsoft account.
2. Verify the account has access to the assigned Azure tenant.
3. Verify the account has access to an Azure subscription.
4. Copy the exact error message.
5. Send the error message to the instructor.

Do not send your password.

---

# Error: No Subscriptions Found

If the script reports:

```text
FAIL: No Azure subscriptions were found.
```

The Azure account authenticated successfully, but the account may not have access to a subscription.

Verify that you signed in with the correct account.

---

# Error: Resource Manager Query Failed

If authentication succeeds but the Resource Manager test fails, record:

```text
Gate:
Gate 6

Result:
Azure authentication succeeded.

Failure:
Azure Resource Manager query failed.

Error:
<copy exact error here>
```

This helps distinguish an authentication problem from a permissions or subscription problem.

---

# Basic Troubleshooting Rule

Always identify the **first failed gate**.

```text
Gate 1
Python
   |
   v
Gate 2
Azure SDK
   |
   v
Gate 3
Authentication
   |
   v
Gate 4
Subscription Discovery
   |
   v
Gate 5
Subscription Selection
   |
   v
Gate 6
Azure Resource Manager
```

Do not troubleshoot Gate 6 if Gate 2 is failing.

Fix the first failed layer.

---

# Quick Start Version

For students who already understand terminals, the entire process is:

```bash
python --version
```

```bash
cd <folder-containing-script>
```

```bash
python -m pip install azure-identity azure-mgmt-resource
```

```bash
python azure_connectivity_test.py
```

Then:

```text
Authenticate
    |
    v
Select Subscription
    |
    v
Verify PASS Results
    |
    v
Submit Final Report
```

---

# Final Checklist

* [ ] I am using a computer capable of running Python locally.
* [ ] Python runs successfully.
* [ ] I located `azure_connectivity_test.py`.
* [ ] My terminal is in the correct directory.
* [ ] `azure-identity` is installed.
* [ ] `azure-mgmt-resource` is installed.
* [ ] The Python script starts successfully.
* [ ] Azure authentication succeeds.
* [ ] My Azure subscription is visible.
* [ ] Azure Resource Manager responds successfully.
* [ ] The final report displays `PASS`.
* [ ] I submitted only non-sensitive verification information.

---

# Remember

If the script fails, do not report:

```text
It doesn't work.
```

Report:

```text
Operating System:
Windows / macOS / Linux

Gate:
<failed gate>

Command:
<command used>

Error:
<exact error message>
```

The exact error message is part of the troubleshooting process.
