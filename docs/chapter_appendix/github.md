# Setup GitHub and Git
## Create a GitHub account

You can register an account [here](https://github.com/signup)

## Installing Git

### MacOS User


1. You may already have git preinstalled, please run 
```bash
git --version
```
 to verify. If it return a version, then you are good to go. If not please continue.
2. To install Git, we will use brew. You should check if you already have brew before installing it.
```bash
brew --version
```
3. If you already have brew installed jump to step 5
Copy and paste the following into the terminal, then hit return(enter)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
4. Brew will then gives instructions for you to run 3 lines in the terminal. Run it! Below is an example but my 3 lines will be different from yours
    ![git3](./git.assets/brew.jpg)
5. Use brew to install git by running in the terminal
```bash
brew install git
```
6. Test if your git is ready
```bash
git --version
```
### Window User

1. Test if git is installed by first run
```bash
git --version
```
to verify. If it return a version, then you are good to go. If not please continue.
2. Go to [Git for Windows](https://git-scm.com/downloads/win) and click download (in the picture below)
    ![git2](./git.assets/window_git_1.jpg)
4. Install the git by click into the downloaded file, then a bunch of "Next","Install", and "Finish"
5. Test if git is successfully installed by close and reopen Command Prompt. Then run:
```bash
git --version
```
