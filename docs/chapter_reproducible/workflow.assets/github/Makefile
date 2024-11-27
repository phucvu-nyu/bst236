# Makefile for initializing a Git repository and pushing to GitHub
# Variables
REPO_NAME = your-repo-name
GITHUB_USER = your-github-username
BRANCH = main

# Default target
all: init commit create push

# Initialize a local Git repository
init:
	git init

# Add and commit files
commit:
	git add .
	git commit -m "Initial commit"

# Create a GitHub repository
create:
	gh repo create $(GITHUB_USER)/$(REPO_NAME) --public --source=. --remote=origin

# Push changes to GitHub
push:
	git push -u origin $(BRANCH)

# Clean up (optional)
clean:
	rm -rf .git

# Usage instructions
help:
	@echo "Usage:"
	@echo "  make all        - Initialize, commit, create GitHub repo, and push"
	@echo "  make init       - Initialize a local Git repository"
	@echo "  make commit     - Add and commit all files"
	@echo "  make create     - Create a GitHub repository"
	@echo "  make push       - Push changes to GitHub"
	@echo "  make clean      - Remove the .git directory"
	@echo "  make help       - Show this help message"
