## Note for macOS Users — Install PowerShell First

macOS does not include PowerShell by default.

You do **not** need a special PowerShell application. PowerShell can be installed on macOS and then launched from the standard macOS **Terminal** application.

### Step 1 — Open Terminal

Open:

**Applications → Utilities → Terminal**

You can also press `Command + Space`, type `Terminal`, and press **Enter**.

### Step 2 — Check for Homebrew

Run:

```bash
brew --version
```

If Homebrew is already installed, continue to Step 3.

If the `brew` command is not found, install Homebrew before continuing.

### Step 3 — Install PowerShell

Using Homebrew, install the current stable version of PowerShell:

```bash
brew install --cask powershell
```

### Step 4 — Start PowerShell

After installation, start PowerShell by running:

```bash
pwsh
```

Your command prompt should change to something similar to:

```text
PS /Users/yourname>
```

You are now running **PowerShell**, even though you are using a Mac.

### Step 5 — Verify the PowerShell Version

Run:

```powershell
$PSVersionTable
```

Look for the `PSVersion` entry.

### Optional — Visual Studio Code

Students who prefer a graphical editor may also use **Visual Studio Code** with Microsoft's **PowerShell extension**.

However, Visual Studio Code is **not required** for this lab. The macOS Terminal application and the `pwsh` command are sufficient.

---

> **Mac users:** Once `pwsh` is running, the Azure PowerShell commands used in the remainder of this lab are essentially the same as those used by Windows users.

You may now continue to **Gate 1 — Verify the Azure PowerShell Module**.
