# Mock Interview Capstone Project Repository

# Quick navigation
[Background](#background)  
[Data](#data)  
[Models](#models)  
[Timeline](#timeline)  
[Repo Structure](#repo-structure)  
[Logistics](#project-logistics)  
[Resources](#resources)  
[Contact](#contact-info)

# Goal


# Background  


# Data


## Data security

As the project moves along, the readme will be updated with this info.

## Counts

As the project moves along, the readme will be updated with this info. (Describe the overall size of the dataset and the relative ratio of positive/negative examples for each of the response variables.)

# Models

As the project moves along, the readme will be updated with this info. (Identify each of the response variables of interest. Any additional desired analysis should also be described here.)

# Timeline

The creation of the dataset and initial steps towards formulating the architecture of the transformer will occur over Fall 2023.

# Repo Structure 

The repo is structured as follows: Notebooks are grouped according to their series (e.g., 10, 20, 30, etc) which reflects the general task to be performed in those notebooks.  Start with the *0 notebook in the series and add other investigations relevant to the task in the series (e.g., `11-cleaned-scraped.ipynb`).  If your notebook is extremely long, make sure you've utilized nbdev reuse capabilities and consider whether you can divide the notebook into two notebooks.

All files which appear in the repo should be able to run, and not contain error or blank cell lines, even if they are relatively midway in development of the proposed task. All notebooks relating to the analysis should have a numerical prefix (e.g., 31-) followed by the exploration (e.g. 31-text-labeling). Any utility notebooks should not be numbered, but be named according to their purpose. All notebooks should have lowercase and hyphenated titles (e.g., 10-process-data not 10-Process-Data). All notebooks should adhere to literate programming practices (i.e., markdown writing to describe problems, assumptions, conclusions) and provide adequate although not superfluous code comments.

# Project logistics

**Sprint planning**: 9:00 AM Fridays on Zoom

**Zoom link**: https://vanderbilt.zoom.us/j/94951906347?pwd=ZmdGWmFtNEFuNW4rcEFDVlRROUJkUT09&from=addon

**Demo**: 2:30 PM Fridays at the Data Science Institute, 2001 Grand Avenue (2nd Floor), Nashville, TN 37212

**Zoom link**: https://vanderbilt.zoom.us/j/95823039326?pwd=WFJWWWo1d2pQZWcyR1JHYmJjcVhUUT09&from=addon

**Data location**:  

**Slack channel**:  


# Resources 
* **Python usage**: Whirlwind Tour of Python, Jake VanderPlas ([Book](https://learning.oreilly.com/library/view/a-whirlwind-tour/9781492037859/), [Notebooks](https://github.com/jakevdp/WhirlwindTourOfPython))
* **Data science packages in Python**: [Python Data Science Handbook, Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/) 
* **HuggingFace**: [Website](https://huggingface.co/transformers/index.html), [Course/Training](https://huggingface.co/course/chapter1), [Inference using pipelines](https://huggingface.co/transformers/task_summary.html), [Fine tuning models](https://huggingface.co/transformers/training.html)
* **fast.ai**: [Course](https://course.fast.ai/), [Quick start](https://docs.fast.ai/quick_start.html)
* **nbdev**: [Overview](https://nbdev.fast.ai/), [Tutorial](https://nbdev.fast.ai/tutorial.html)
* **Git tutorials**: [Simple Guide](https://rogerdudler.github.io/git-guide/), [Learn Git Branching](https://learngitbranching.js.org/?locale=en_US)
* **ACCRE how-to guides**: [DSI How-tos](https://github.com/vanderbilt-data-science/how-tos)  

# Contact Info

Senior Data Scientist: 
Project Manager: 

Code Contributors:

Jiaying Liang, jiaying.liang@vanderbilt.edu

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

