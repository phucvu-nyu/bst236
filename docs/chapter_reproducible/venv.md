# Python Virtual Environments

!!! abstract "Learning Objectives"
    - Understand why virtual environments are crucial for reproducible research
    - Learn how to create and manage Python virtual environments
    - Master dependency management with requirements.txt
    - Develop best practices for environment management in scientific projects

## Why Virtual Environments?

Virtual environments solve several critical problems:

1. **Isolation**: Keep project dependencies separate
2. **Reproducibility**: Ensure consistent package versions across different machines
3. **Conflict Prevention**: Avoid package version conflicts between projects
4. **Clean Management**: Easy to create, delete, and recreate environments

## Virtual Environment Tools

### venv (Built-in)
Python's built-in solution, simple and lightweight:
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# On Unix/macOS:
source myenv/bin/activate
# On Windows:
myenv\Scripts\activate

# Deactivate
deactivate
```

### conda
Anaconda's solution, popular in data science:
```bash
# Create environment
conda create -n myenv python=3.9

# Activate environment
conda activate myenv

# Deactivate
conda deactivate
```

## Managing Dependencies

### pip Requirements

1. **Generate requirements.txt**:
```bash
# Manual: List all installed packages
pip freeze > requirements.txt

# Automated: Only list direct dependencies
pip-compile pyproject.toml

# Alternative: Use pigar to analyze imports
pigar generate
```

2. **Install from requirements.txt**:
```bash
pip install -r requirements.txt
```

### Modern Tools

1. **Poetry** (Recommended for new projects):
```bash
# Initialize new project
poetry init

# Add dependencies
poetry add pandas numpy

# Install dependencies
poetry install

# Generate lock file
poetry lock

# Export requirements
poetry export -f requirements.txt --output requirements.txt
```

2. **pipenv**:
```bash
# Install dependencies
pipenv install pandas numpy

# Generate lock file
pipenv lock

# Install from Pipfile
pipenv install
```

## Best Practices

### 1. Project Structure
```
project/
├── .gitignore
├── README.md
├── pyproject.toml  # or requirements.txt
├── .env            # for environment variables
├── src/
│   └── ...
├── tests/
│   └── ...
└── notebooks/
    └── ...
```

### 2. Version Control Integration

**.gitignore** for virtual environments:
```plaintext
# Virtual Environment
venv/
env/
.env/
.venv/

# Dependency Management
*.pyc
__pycache__/
.Python
pip-log.txt
```

### 3. Dependency Documentation

**pyproject.toml** (Poetry):
```toml
[tool.poetry]
name = "project-name"
version = "0.1.0"
description = ""

[tool.poetry.dependencies]
python = "^3.9"
pandas = "^1.4.0"
numpy = "^1.22.0"

[tool.poetry.dev-dependencies]
pytest = "^7.0.0"
black = "^22.0.0"
```

**requirements.txt**:
```plaintext
# Core dependencies
pandas==1.4.0
numpy==1.22.0

# Development dependencies
pytest==7.0.0
black==22.0.0
```

### 4. Automated Environment Setup

**Makefile** for environment management:
```makefile
.PHONY: env clean requirements

# Create virtual environment
env:
    python -m venv venv
    source venv/bin/activate && \
    pip install -r requirements.txt

# Update requirements
requirements:
    pip freeze > requirements.txt

# Clean environment
clean:
    rm -rf venv
    find . -type d -name __pycache__ -exec rm -r {} +
```

## Recommended Workflow

1. **Project Setup**:
```bash
# Initialize project with Poetry
poetry init
# or
# Create virtual environment
python -m venv venv
```

2. **Development Workflow**:
```bash
# 1. Activate environment
source venv/bin/activate  # or poetry shell

# 2. Install/update dependencies
pip install package_name  # or poetry add package_name
pip freeze > requirements.txt  # or poetry export

# 3. Code and test

# 4. Deactivate when done
deactivate  # or exit
```

3. **Collaboration Workflow**:
```bash
# 1. Clone repository
git clone project_url

# 2. Create environment
make env  # or poetry install

# 3. Activate environment
source venv/bin/activate  # or poetry shell

# 4. Work on project

# 5. Update dependencies if needed
make requirements  # or poetry export
```

4. **Deployment Workflow**:
```bash
# 1. Create fresh environment
python -m venv prod_env

# 2. Install only production dependencies
pip install -r requirements.txt --no-dev

# 3. Run tests
pytest

# 4. Deploy
```

## Common Issues and Solutions

1. **Package Conflicts**:
```bash
# Use pip-tools to resolve conflicts
pip-compile --upgrade
pip-sync
```

2. **Environment Activation Issues**:
```bash
# If activation fails, recreate environment
make clean
make env
```

3. **Different Python Versions**:
```bash
# Specify Python version in pyproject.toml
[tool.poetry.dependencies]
python = ">=3.8,<3.11"
```

## Resources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Poetry documentation](https://python-poetry.org/docs/)
- [pip-tools documentation](https://pip-tools.readthedocs.io/)
- [Conda documentation](https://docs.conda.io/)
