# Installation Guide for Course

!!! warning "Important"
    Phil: Please edit the following content.





## Operating System

Most of the materials in this course are platform-independent. However, most of the instructions are based on Linux or macOS. If you are using Windows, you can either find the corresponding Windows instructions online or use WSL2 to set up a Linux virtual machine. See a tutorial [here](https://learn.microsoft.com/en-us/windows/wsl/install).

## Install IDE

For your local Integrated Development Environment (IDE), we suggest using Visual Studio Code (VS Code) - a lightweight, open-source editor. Head to the [VS Code official website](https://code.visualstudio.com/) to download and install the version that matches your operating system.

VS Code features a robust marketplace of extensions that enables coding and debugging in virtually any programming language. Take Python for example - by installing the "Python Extension Pack", you gain full debugging capabilities for Python code. The figure below demonstrates how to install extensions.

### Github Copilot

We recommend using the AI assistant Github Copilot or other similar tools.
If you are a student, you can apply for a free license of Github Copilot [here](https://github.com/features/copilot).

To install Github Copilot in VS Code, you can search for `Github Copilot` in the VS Code extension marketplace and install it.
Alternatively, you can refer to the [official tutorial](https://docs.github.com/en/copilot/quickstart).

### Cursor

Cursor is a new generation AI-powered IDE that can help you write code faster and more efficiently. All the basic features of Cursor is same as VS Code. 
You can download Cursor from the [official website](https://www.cursor.sh/) and install it. 

## Install language environments

### Python

  We suggest using pyenv to install python for better version management. 

1. Install pyenv:
   - On macOS: `brew install pyenv`
   - On Linux: `curl https://pyenv.run | bash`
   

2. Add pyenv to your shell configuration:
   - For bash, add to `~/.bashrc`:
     ```bash
     export PYENV_ROOT="$HOME/.pyenv"
     export PATH="$PYENV_ROOT/bin:$PATH"
     eval "$(pyenv init -)"
     ```
   - For zsh, add to `~/.zshrc`:
     ```bash
     export PYENV_ROOT="$HOME/.pyenv"
     export PATH="$PYENV_ROOT/bin:$PATH"
     eval "$(pyenv init -)"
     ```
   - Source the file to apply the changes:
     ```bash
     source ~/.bashrc  # For bash
     source ~/.zshrc   # For zsh
     ```

3. Install Python using pyenv:
   ```bash
   pyenv install 3.10.0  # Install Python 3.10.0
   pyenv global 3.10.0   # Set as default Python version
   ```

4. Verify the installation:
   ```bash
   python --version  # Should show Python 3.10.0
   ```

#### Conda

We also suggest installing mini-conda for data analysis projects. To install Miniconda on macOS, follow these steps:

1. **Download the Miniconda Installer:**
   - Visit the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
   - Choose the installer that matches your macOS architecture:
     - For Apple Silicon (M1, M2, etc.): Select the "Miniconda3 macOS Apple M1 64-bit pkg" installer.
     - For Intel-based Macs: Select the "Miniconda3 macOS Intel x86 64-bit pkg" installer.

2. **Install Miniconda:**
   - Locate the downloaded `.pkg` file in your `Downloads` folder.
   - Double-click the installer to launch it.
   - Follow the on-screen instructions:
     - Read and agree to the license agreement.
     - Choose the installation type:
       - **Install for all users of this computer (Recommended):** Installs Miniconda into `/opt/miniconda3` for all users.
       - **Install just for me:** Installs Miniconda into your home directory.
     - Click "Install" to proceed.

3. **Initialize Miniconda:**
   - After installation, open the Terminal application.
   - Run the following command to initialize conda:
     ```bash
     conda init
     ```
   - Close and reopen the Terminal to apply the changes.

4. **Verify the Installation:**
   - In the Terminal, check the conda version by running:
     ```bash
     conda --version
     ```
   - A successful installation will display the conda version number.

For more detailed information, refer to the [official Miniconda installation documentation](https://docs.anaconda.com/miniconda/install/). 

### R 

You can use other R IDEs like RStudio, but we suggest using VS Code with the R extension to better integrate with AI copilot. You can find the tutorial of VS Code R extension [here](https://code.visualstudio.com/docs/languages/r).
To set up R in Visual Studio Code, follow these steps:

**1. Install R**

Ensure that R (version 3.4.0 or higher) is installed on your system:

- **macOS**: Download the installer from [CRAN](https://cran.r-project.org/bin/macosx/) and follow the installation prompts.
- **Linux**: Use your package manager to install R. For example, on Ubuntu:

  ```bash
  sudo apt-get update
  sudo apt-get install r-base
  ```





**2. Install radian**

With Python installed, install radian using pip:

```bash
pip install -U radian
```

This command installs radian globally.

**3. Install Required R Packages**

Open your R console and install the following packages:

```r
install.packages("languageserver")
install.packages("httpgd")
```

- `languageserver`: Provides language support for R in VS Code.
- `httpgd`: Enables an interactive plot viewer in VS Code.

**4. Install the R Extension in VS Code**

In VS Code:

- Click on the Extensions view icon on the Sidebar or press `Ctrl+Shift+X`.
- Search for "R" and install the extension by Yuki Ueda.

**5. Configure VS Code Settings**

To integrate radian with VS Code:

- Open VS Code settings:
  - Click on the gear icon in the lower-left corner and select "Settings," or press `Ctrl+,`.
- In the search bar, type `r.rterm`.
- Set the path to radian:
  - **macOS/Linux**: Set `r.rterm.mac` or `r.rterm.linux` to the output of `which radian` (e.g., `/usr/local/bin/radian`).
- Enable bracketed paste mode:
  - Search for `r.bracketedPaste` and ensure it's checked.
  - Search for `r.plot.useHttpgd` and enable it to use the httpgd plot viewer.

**6. Verify the Setup**

To confirm everything is set up correctly:

- Open a new terminal in VS Code:
  - Click on "Terminal" in the top menu and select "New Terminal."
- Type `radian` and press Enter.
- The radian console should start, displaying syntax highlighting and auto-completion features.

You can now write and execute R code within VS Code using the radian console, benefiting from enhanced features like syntax highlighting and auto-completion.

For a visual walkthrough, consider watching the following tutorial:

# Cluster

The cluster computing of the class is supported by Harvard Academic Technologies Group similar to the [FAS-RC cluster](https://rc.fas.harvard.edu/). Check the Academic Technologies Group [official website](https://atg.fas.harvard.edu/) for more information.


