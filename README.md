# Personal Career Coach
[Hugging Face Space: MockInterviewApp](https://huggingface.co/spaces/jiaying2022/MockInterviewApp)  
[Video Recording: Overview](https://github.com/Liang-Jiaying/mock-interview-capstone-project/assets/111295386/c96fdb11-1b9c-46db-9713-735a346069bd)  

### Overview
Have you ever found yourself in the midst of job hunting season, overwhelmed with tasks on your to-do list, yet unsure where to start or how to make that first step? Our Personal Career Coach understands your struggles and offers personalized assistance to guide you.    

Objectives of the Personal Career Coach Project:
1. **Resume Review**: We review your resume and provide feedback tailored to the job and company you are applying to.
2. **Cover Letter Crafting**: Generate a custom cover letter for each job application, ensuring it's tailored to both the job and the company.
3. **Interview Question Generator**: Supply commonly asked interview questions, helping you prepare for various interviewing scenarios.
4. **Interview Response Enhancement**: Coach you on improving your answers to interview questions, ensuring they are engaging and relevant.

Rationale Behind These Goals:
1. **Resume Review**: A standout resume is your first step towards securing an interview. Our review process helps you customize your resume for specific jobs and companies, increasing the alignment of your qualifications.
2. **Cover Letter Crafting**: Crafting individual cover letters for each application is time-consuming. Recruiters often prefer applications that include a cover letter. Our tool helps you create specific, personalized cover letters efficiently, saving you from repeatedly editing the same template.
3. **Interview Question Generator**: Interviews often feature similar questions framed in the context of the company. Our generator provides a range of questions, including direct, behavioral, and technical, to help you anticipate and prepare for what you might be asked.
4. **Interview Response Enhancement**: Crafting responses to interview questions requires effort, from selecting appropriate examples to structuring your story in an engaging manner. Despite thorough preparation, it's challenging to gauge the effectiveness of your answers. Our tool offers insights on enhancing your responses and provides examples of improved answers based on your initial attempts.
 
In conclusion, our Personal Career Coach is more than a mere tool; it is a pathway to empowering individuals with the confidence and preparedness necessary to excel in their interviews.

# Quick navigation
[Goal](#goal)  
[Background](#background)    
[Data](#data)     
[Models](#models)    
[Demo](#demo)    
[Critical Analysis](#critical-analysis)  
[Logistics](#project-logistics)     
[References](#references)    
[Resources](#resources)    
[Contact](#contact-info)    
[Timeline](#timeline)   

# Goal
**The application aims to resolve the following issues**:   
a.	Limited appointment slots available with CMC's career coaches for mock interviews.  
b.	Restricted time frames for practicing with CMC's career coaches.  
c.	Uncertainty about what to articulate during a mock interview.   
d.	Potential discomfort or embarrassment due to lack of preparation before the mock interview session.  
These obstacles can hinder students' interview preparation, but the proposed application seeks to mitigate these issues by offering flexible and round-the-clock practice sessions without the need for appointments and facilitating more focused feedback from career coaches.  

**Having this proposed application, students are able to benefit from following cases**:  
a.	Practice their interview skills anytime and anywhere. They do not need to stress out about the upcoming interviews that they have not got a slot for practice with CMC’s career coaches;  
b.	Practice as many times as they want. They can practice interview skills 24/7;  
c.	No longer need to worry about not prepare before doing mock interview with CMC’s career coaches;  
d.	This application can also help CMC’s career coaches to better help those students who prepared well and want some professional feedbacks before going to company interviews.  

# Background  

Through daily observations and conversations with my peers, I've witnessed the widespread challenges of job hunting, particularly among non-native speakers. As someone who empathizes with these struggles, the importance of early and effective preparation became clear to me. This sentiment was reinforced at the start of the semester when Dr. Spencer-Smith introduced this project. I was immediately drawn to the idea of developing a tool that could not only assist my cohorts in the Data Science Institute but also potentially benefit students across Vanderbilt University.

While there are numerous online applications like [Leetcode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/), [Jobscan](https://www.jobscan.co/), [Pramp](https://www.pramp.com/#/), [rocketblocks](https://www.rocketblocks.me/), and so on, focusing on enhancing interview skills, none provide an all-encompassing solution for the entire job application process. Our Personal Career Coach application fills this gap. It guides users from the outset of their job search, helping to tailor resumes and cover letters for specific roles and companies, thereby increasing their chances of securing interviews. Post-interview preparation is also covered, with tailored questions and practice sessions to boost confidence and readiness.

The overarching aim of this application is to alleviate the stress associated with job hunting while balancing academic responsibilities. To extend its reach, I decided on a web-based platform, allowing easy access and user-friendly interaction. My experience in the 2023 AI Summer program, particularly with Gradio and Hugging Face Space, inspired me to utilize these platforms for hosting the initial version of the application, facilitating self-exploration and wider accessibility.

# Data

In the initial planning stages of our project, we considered creating a data store to house commonly asked interview questions. However, as we delved deeper into the project, it became evident that GPT-4's capabilities were sufficient to generate high-quality content without the need for additional data. The cornerstone of our project's success lies in effective prompt engineering. To facilitate this, we have organized and stored these carefully crafted prompts as text files in a designated data folder. This approach allows us to harness the full potential of GPT-4 while maintaining a streamlined and efficient data structure.

## Data security  
***Disclaimer**: This platform uses Artificial Intelligence (AI). Please do not share private or sensitive information during interactions, as AI cannot ensure confidentiality. Exercise discretion for your security.

# Models

In the development of our project, we exclusively utilized GPT-4, accessed via the OpenAI API. Initially, our plan involved fine-tune a pre-trained model tailored for interview preparation. However, upon exploring GPT-4's capabilities, we quickly realized that it not only met but exceeded our expectations in performance and functionality. GPT-4's advanced features and adaptability rendered the need to train a separate model unnecessary for our current objectives. Looking ahead, should the need arise for more specialized functions within our app, we may revisit the idea of training a dedicated model to meet those specific requirements.

# Demo
## Code Demo
[Google Colab Notebook: Example Notebook](https://colab.research.google.com/drive/1JEvxRR8YF1UcsJkYZdgVZ9pyfa2JA9Pl?usp=sharing)
<img width="1435" alt="Screenshot 2023-11-25 at 5 22 55 PM" src="https://github.com/Liang-Jiaying/mock-interview-capstone-project/assets/111295386/e9e2dde9-66b8-40c6-834c-81f9becdc244">  
<img width="1436" alt="Screenshot 2023-11-25 at 5 28 13 PM" src="https://github.com/Liang-Jiaying/mock-interview-capstone-project/assets/111295386/23e030ae-eb90-4f02-8add-2cfae5af2999">

## Gradio Demo
[HuggingFace Space: jiaying2022/MockInterviewApp](https://huggingface.co/spaces/jiaying2022/MockInterviewApp)  

<img width="1427" alt="Screenshot 2023-11-24 at 7 24 41 AM" src="https://github.com/Liang-Jiaying/mock-interview-capstone-project/assets/111295386/ff3f2427-b8ef-487e-ab05-f3c4cc3215d3">


# Critical Analysis

{CRITICAL ANALYSIS GOES HERE}

# Project logistics
**Project planning**: By appointment with three faculties in the contact.  
**Sprint planning**: 10:00 AM Fridays at the Data Science Institute, 2001 Grand Avenue (2nd Floor), Nashville, TN 37212  

# References
1. Lee, H., Phatale, S., Mansoor, H., Lu, K., Mesnard, T., Bishop, C., ... & Rastogi, A. (2023). Rlaif: Scaling reinforcement learning from human feedback with ai feedback. arXiv preprint arXiv:2309.00267.

2. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., ... & Lowe, R. (2022). Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems, 35, 27730-27744.

# Resources 
**Tutorials**:  
* **2023 AI Summer**: [Recording](https://www.youtube.com/watch?v=AXRDiHQMmBo&list=PL6KxUvysa-7yV8T4qcoLaDH3ZzUFwYx8u)
* **Prompt Engineering for ChatGPT**: [Coursera](https://www.coursera.org/programs/coursera-for-vanderbilt-0fcd8/learn/prompt-engineering?authProvider=vanderbilt)  

**Main Resources**:  
* **OpenAI API setup**: OpenAI API [Documentation](https://platform.openai.com/docs/api-reference)
* **Google Colab notebook**: [Website](https://colab.google/)
* **HuggingFace**: [Website](https://huggingface.co/transformers/index.html), [Course/Training](https://huggingface.co/course/chapter1), [Inference using pipelines](https://huggingface.co/transformers/task_summary.html), [Fine tuning models](https://huggingface.co/transformers/training.html)
* **LangChain**: [Get started](https://python.langchain.com/docs/get_started), [Documentation](https://docs.langchain.com/docs/)
* **Gradio**: [Quickstart](https://www.gradio.app/guides/quickstart)

**Minor Resources**:
* **Python usage**: Whirlwind Tour of Python, Jake VanderPlas ([Book](https://learning.oreilly.com/library/view/a-whirlwind-tour/9781492037859/), [Notebooks](https://github.com/jakevdp/WhirlwindTourOfPython))
* **Data science packages in Python**: [Python Data Science Handbook, Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/) 
* **fast.ai**: [Course](https://course.fast.ai/), [Quick start](https://docs.fast.ai/quick_start.html)
* **nbdev**: [Overview](https://nbdev.fast.ai/), [Tutorial](https://nbdev.fast.ai/tutorial.html)
* **Git tutorials**: [Simple Guide](https://rogerdudler.github.io/git-guide/), [Learn Git Branching](https://learngitbranching.js.org/?locale=en_US)
* **ACCRE how-to guides**: [DSI How-tos](https://github.com/vanderbilt-data-science/how-tos)  

# Contact Info
Project Supervisor: Dr. Jesse Spencer-Smith, jesse.spencer-smith@vanderbilt.edu  
DSI Faculty: Dr. Jesse Blocher, jesse.blocher@vanderbilt.edu  
CMC Faculty: Brook Meissner, brook.meissner@vanderbilt.edu  

Project Manager & Code Contributors: Jiaying Liang, jiaying.liang@vanderbilt.edu

# Timeline
[Nov.27.2023 - Nov.30.2023]: [PLAN FOR THE WEEK AFTER]
* Prepare AI Showcase (Issue #) ()
* Total work time: about 5h

[Nov.20.2023 - Nov.26.2023]:  THANKSGIVING BREAK
* Meet with Brook (giving update, getting feedback, discussing future plan) (Issue #53) (11.20, 2h)
* Create gradio draft to combine resume_review + cover_letter + interview_question_answer (Issue #62) (11.20, 4h)
* Meet with Dr. Blocher (giving update, getting feedback, discussing future plan) (11.21, 2h)
* Improve the gradio by Dr. Blocher's feedback (11.22-11.23, 1.5h)
* Presentaion Preparation (11.24, 3h)
* Total work time: about 12.5h

[Nov.13.2023 - Nov.19.2023]: [This week To-Do]
* 1 prompt for generate different types of interview question by the request (11.19, 5h)
* Answer evaluation prompt (Issue #45) (11.13-11.17, 5h)
* Cover letter prompt (Issue #46) (11.18-11.19, 3h)
* Total work time: about 13h

[Nov.6.2023 - Nov.12.2023]:  
* Interview question prompt (Issue #41) (11.6-11.12, 5 h)
* Total work time: about 5h 

[Oct.30.2023 - Nov.5.2023]:  
* Prompt Engineering for ChatGPT Week 4 + notes (Issue #23) (10.24, 2.5 h)
* Prompt Engineering for ChatGPT Week 4 + notes (Issue #24) (10.26, 2.5 h)
* Prompt Engineering for ChatGPT Week 4 + notes (Issue #25) (10.26-10.29, 3 h)
* Total work time: about 8h 

[Oct.23.2023 - Oct.29.2023]:  
* AI Summer Week4 Session 2 (Issue #32) (10.24, 2.5 h)
* AI Summer Week4 Session 3 (Issue #33) (10.26, 2.5 h)
* Create a gradio draft (Issue #42) (10.26-10.29, 6 h)
* Total work time: about 11h 

[Oct.18.2023 - Oct.22.2023]:  FALL BREAK

[Oct.9.2023 - Oct.17.2023]:  
* AI Summer Week3 Session 2 (Issue #13) + notes (10.9, 2.5 h)
* Learning & analyze recommended prompt (Issue #35) (10.15, 1.5 h)
* AI Summer Week3 Session 3 (Issue #30) (10.16, 2.5 h)
* AI Summer Week4 Session 1 (Issue #31) (10.17, 2.5 h)
* Total work time: about 9h 

[Oct.2.2023 - Oct.8.2023]:  
* Use LangChain in Google Colab Notebook come up with a info template, and prompt template (Issue #11, #15)
* Use prompt engineering ideas to get better prompt
* Total work time: about 6h (Does not include learning time.)

[Sep.18.2023 - Oct.1.2023]:  
* File the notes for the conversation with Dr. Blocher (Issue #20) (9.18, 30 min)
* File the notes for the conversation with Brook (Issue #19) (9.21, 30 min)
* File the notes for the conversation Dr. Spencer-Smith (Issue #21) (9.21, 30 min)
* Customer interviewed 3 cohorts (Issue #18) (9.21, 1 h; 9.25, 40 min)
* Take notes for all 6 customer interviews, and come up develope ideas (Issue #18) (9.26-9.28, 4 h)
* Updated my overall plan for this project (Issue #6) (9.28, 40 min)
* Total work time: about 7h, 50min (Does not include learning time.)

[Sep.8.2023 - Sep.17.2023]:  
* Talked with Dr. Blocher, get dieas of what will be my next step (ect. customer interview (Issue #18), try the baseline (Issue #17), ...) (Issue #20) (9.11, 45 min)
* Talked with Brook, get ideas of how he evaluate students' interview (Issue #19) (9.15, 50 min)
* Talked with Dr. Spencer-Smith, get ideas of *Resume Review Prompt* (Issue #21) (9.15, 35 min)
* Customer interviewed 3 cohorts (Issue #18) (9.13, 45 min; 9.17, 1 h)
* Total work time: about 3h, 55min (Does not include learning time.)

[Sep.1.2023 - Sep.7.2023]:  
* Talked with project director briefly about project idea, took this project (9.1, 20 min);
* Did some prompt exploration, got feedback from project director about the next step and things to improve (9.6, 60 min);
* Get done OpenAI API setup (Issue#7) (30 min);
* Come up a detail plan for approching this project (at least 2 h);
* Total work time: about 3h, 50min (Does not include learning time.)

[Before Sep.1.2023]
* Talked with CMC director about petential data he had, his concerns, and suggestions for the next step. (20 min)
