# Git and GitHub

!!! abstract "Learning Objectives"
    - Understand why version control is essential for reproducible research
    - Learn basic Git commands and workflows
    - Learn how to collaborate using GitHub
    - Develop best practices for version control in scientific computing

## Why Version Control?

Version control is essential for:

1. **Tracking Changes**: Keep a complete history of your project
2. **Collaboration**: Work effectively with others
3. **Backup**: Never lose your work
4. **Reproducibility**: Return to any previous state of your project
5. **Documentation**: Understand why changes were made

## Git Basics

### Setting Up Git

First time setup:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Essential Git Commands

1. **Initialize a Repository**
```bash
git init
```

2. **Check Status**
```bash
git status
```

3. **Stage Changes**
```bash
git add filename     # Stage specific file
git add .           # Stage all changes
```

4. **Commit Changes**
```bash
git commit -m "Descriptive message about changes"
```

5. **View History**
```bash
git log             # View commit history
git diff            # View unstaged changes
```

### Best Practices for Commits

1. **Commit Often**: Make small, logical commits
2. **Write Clear Messages**: Use descriptive commit messages
3. **One Change Per Commit**: Each commit should represent one logical change
4. **Test Before Committing**: Ensure code works before committing

Example of a good commit message:
```bash
git commit -m "Add bootstrap confidence intervals to regression analysis"
```

## Working with GitHub

### Setting Up GitHub

1. Create a GitHub account at [github.com](https://github.com)
2. Set up SSH keys for secure authentication:
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```
3. [Add the public key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

### Basic GitHub Workflow

1. **Create a Repository on GitHub**
   - Click "New repository" on GitHub
   - Follow the setup instructions

2. **Clone a Repository**
```bash
git clone git@github.com:username/repository.git
```

3. **Connect Local to Remote**
```bash
git remote add origin git@github.com:username/repository.git
```

4. **Push Changes**
```bash
git push origin main
```

5. **Pull Changes**
```bash
git pull origin main
```

### Branching and Merging

1. **Create and Switch to a Branch**
```bash
git checkout -b feature-name
```

2. **Switch Between Branches**
```bash
git checkout main
```

3. **Merge Branches**
```bash
git checkout main
git merge feature-name
```

## Collaborative Workflows

### Pull Requests

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a feature branch
4. Make changes and push to your fork
5. Create a pull request on GitHub

### Best Practices for Collaboration

1. **Pull Before Push**: Always pull latest changes before pushing
2. **Use Branches**: Never work directly on main
3. **Review Code**: Use pull requests for code review
4. **Keep Commits Clean**: Use meaningful commit messages
5. **Document Changes**: Update documentation with code changes

## Common Issues and Solutions

### Resolving Merge Conflicts

1. **Identify Conflicts**
```bash
git status
```

2. **Resolve Conflicts**
   - Open conflicted files
   - Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Edit files to resolve conflicts
   - Stage and commit resolved files

### Undoing Changes

1. **Discard Unstaged Changes**
```bash
git restore filename
```

2. **Unstage Changes**
```bash
git restore --staged filename
```

3. **Undo Last Commit**
```bash
git reset --soft HEAD~1
```


### .gitignore

Create a `.gitignore` file to exclude:
- Large data files
- Sensitive information
- Generated files
- System files

Example `.gitignore`:
```plaintext
# Data files
*.csv
*.xlsx
data/

# Generated files
*.pdf
results/

# System files
.DS_Store
.Rhistory
```



## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Happy Git with R](https://happygitwithr.com/)
