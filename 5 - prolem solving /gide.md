# How to Submit Your Code to GitHub

Welcome to the GitHub submission guide! Follow these steps to submit your code to GitHub for assessment.

## Step 1: Create a Repository

1. Go to the GitHub website and log in to your account.
2. Navigate to the organization page where you've been invited.
3. Click on the "Repositories" tab.
4. Click on the green "New" button.
5. Enter a name for your repository (e.g., `assignment-submission`).
6. Optionally, add a description for your repository.
7. Choose the visibility of your repository (public or private).
8. Click on the "Create repository" button.

## Step 2: Set Up Git Locally

1. Install Git on your local machine if you haven't already. You can download Git from [here](https://git-scm.com/downloads) and follow the installation instructions for your operating system.
2. Open a terminal or command prompt.
3. Configure Git with your name and email using the following commands:

   ```
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## Step 3: Clone the Repository

1. Go to your repository on GitHub.
2. Click on the green "Code" button.
3. Copy the URL provided (e.g., `https://github.com/Intermediate-Python-Class/python-class/`).
4. Open a terminal or command prompt.
5. Navigate to the directory where you want to clone the repository.
6. Run the following command to clone the repository to your local machine:

   ```
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the URL you copied from GitHub.

## Step 4: Add Your Code to the Repository

1. Copy your code files or project folders into the cloned repository directory on your local machine.
2. Open a terminal or command prompt.
3. Navigate to the cloned repository directory.
4. Run the following commands to add your files to the staging area and commit them:

   ```
   git add .
   git commit -m "Initial commit"
   ```

   Replace `"Initial commit"` with an appropriate commit message describing your changes.

## Step 5: Push Your Code to GitHub

1. Run the following command to push your code to GitHub:

   ```
   git push origin main
   ```

   This command pushes your committed changes to the `main` branch of your repository on GitHub.

## Step 6: Verify Your Submission

1. Go to your repository on GitHub.
2. Refresh the page to see your pushed changes.
3. Verify that all your code files and folders are present in the repository.

Congratulations! You have successfully submitted your code to GitHub. Your instructor will review your submission and provide feedback as necessary.
