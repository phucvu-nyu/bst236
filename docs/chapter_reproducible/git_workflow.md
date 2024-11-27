## Workflow: Initialize Local Repository and Create GitHub Repository from Terminal

### Step 1: Initialize a Local Repository

1. **Navigate to your project directory**:
   ```bash
   cd /path/to/your/project
   ```

2. **Initialize the Git repository**:
   ```bash
   git init
   ```

### Step 2: Add and Commit Your Files

1. **Stage your files**:
   ```bash
   git add .
   ```

2. **Commit your changes**:
   ```bash
   git commit -m "Initial commit"
   ```

### Step 3: Create a Repository on GitHub from Terminal

1. **Create a new GitHub repository**:
   ```bash
   gh repo create username/repository --public --source=. --remote=origin
   ```

   - Replace `username` with your GitHub username and `repository` with your desired repository name.
   - Use `--private` instead of `--public` if you want a private repository.

### Step 4: Push Local Changes to GitHub

1. **Push your changes to GitHub**:
   ```bash
   git push -u origin main
   ```

### Notes

- Ensure you have set up SSH keys for authentication with GitHub.
- If your default branch is not `main`, replace `main` with your default branch name.
