# Mock Interview Capstone Project Demo

Use this template repository to practice GitHub Flow. 

## GH Flow Hands-On

**Goal**: The main task to be completed is to create a function `compute_area` in the `shape_attributes.py` file. The function computes and returns an area based on a radius `r`.
For reference:
* The area of a circle is $\pi r^2$
* The area of a sphere is $4 \pi r^2$

### Setup
One team member creates a private repo using this template and adds the second team member to the repo as a collaborator. 

### Merging via GitHub
Now both team members complete the assigned tasks using the following steps:

- Clone the repo from the command line using ```git clone <URL>``` OR Create a new project from version control
- Create a new branch with an appropriate title ```git checkout -b <branch_name>```
- Make changes to your code in the new branch and save them
- Add your changes to the staging area ``` git add shape_attributes.r```
- Commit your changes from the command line using ```git commit -m "your message here"```
- Push your changes to the remote branch using  ```git push -u origin <branch_name>```
- Create a pull request and assign it to member 2.

Team Member 1 reviews Team Member 2’s PR, merges, deletes branch, and closes the PR. 

Team Member 2 reviews Team Member 1’s PR, and UH OH! Conflict!! Team Member 2 fixes it on GitHub. Merge, delete branch, and close the PR.

### Merging locally
You'll be repeating the same exact steps above to the existing repo, except for 1) the changes to be made to the file, and 2) the resolution of the merge conflict. For 1, we'll be adding a new line below the function with a comment about what the function does. For 2, instead of merging via GitHub, we'll use the most recent version of main and merge this into the relevant branch. The steps are repeated below.

Now both team members complete the assigned tasks using the following steps:

- Create a new branch with an appropriate title ```git checkout -b <branch_name>```
- Make changes to your code in the new branch and save them
- Add your changes to the staging area ``` git add shape_attributes.r```
- Commit your changes from the command line using ```git commit -m "your message here"```
- Push your changes to the remote branch using  ```git push -u origin <branch_name>```
- Create a pull request and assign it to member 2.

Team Member 1 reviews Team Member 2’s PR, merges, deletes branch, and closes the PR. 

Team Member 2 reviews Team Member 1’s PR, and UH OH! Conflict!! Team Member 2 fixes it in R. Merge, delete branch, and close the PR.

