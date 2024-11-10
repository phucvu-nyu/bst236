# Github Classroom 🏗️

<!-- Phil: Test and revise the following content. Especially for homework pull and push. -->

## What is Git?
Git is a powerful tool that helps developers track and manage changes to their code over time. Think of it like a time machine for your code - it keeps track of every version of your files, allowing you to see what changed, when it changed, and who changed it.

The key features that make Git useful are:
- Version history: Git saves a complete history of all changes, making it easy to go back to previous versions if needed
- Collaboration: Multiple developers can work on the same code without conflicts
- Branching: You can create separate branches to work on new features without affecting the main code
- Distributed: Every developer has a complete copy of the code and its history on their computer

Git was created by Linus Torvalds (who also created Linux) and has become the standard tool for version control in software development. To learn more about using Git, check out [A Guide to Git](https://missing.csail.mit.edu/2020/version-control/).




## Github Classroom

For this course, you'll use Git and Github Classroom as your version control system to manage and submit assignments. These tools will help you track changes to your code and share your work with course staff.

## Getting Started with Github Classroom

The first step is creating a Github account if you don't already have one. Once you have an account, you'll need to set up SSH authentication by adding a public/private key pair.

If you've previously set up SSH keys for Github, you can reuse them by copying your existing key pair to the `~/.ssh` directory. Otherwise, you'll need to generate new SSH keys by following these steps:

1. Launch your terminal
2. Run `ssh-keygen -t rsa` and follow the instructions
3. You have now created your ssh keys in the directory `~/.ssh`
4. Run `cat .ssh/id_rsa.pub` to display your public key
5. Copy your public key and enter it into Github under Settings > SSH Keys
## Working with Course Materials

At the beginning of the semester, you'll need to set up your course repository to access and work with the course materials. Here's what you'll do throughout the term:

- Get your own copy of the course code by cloning the repository
- Complete and submit assignments in your personal repository
- Download new course content when it becomes available

### How Repositories are Organized 

You'll work with two separate repositories:

1. The official course repository managed by instructors - you can download from this but not make changes
2. Your own personal repository where you'll complete and submit assignments

### Setting Up Your Repository

Follow these steps to get started:

1. Look for an email with the Github Classroom assignment invitation
2. Open the link and select "Accept this assignment" 
3. Wait for your repository to be created - you'll see a confirmation page
4. Find the repository URL by clicking the green "Code" button
5. In your terminal:
   ```bash
   # Create and enter directory
   mkdir ~/course
   cd ~/course
   
   # Configure git identity
   git config --global user.name "FIRST_NAME LAST_NAME"
   git config --global user.email "YOUR_EMAIL"
   
   # Clone the repo
   git clone REPO_URL
   ```

### Submitting Assignments

When starting and submitting assignments:

1. Tag the start:
   ```bash
   git tag assignment1-start
   ```

2. When ready to submit:
   ```bash 
   git tag assignment1-submit
   git push origin master --tags
   ```

Make sure to commit all changes before tagging and pushing.
