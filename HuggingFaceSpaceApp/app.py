## 0. Import packages

import gradio as gr

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from langchain.chains import ConversationChain
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
import os
from getpass import getpass

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage

import textract


## 1. Tab-API

# 1.1. define get_api to pass OpenAI API key for calling models
def get_api_key(openai_api_key):
    os.environ["OPENAI_API_KEY"] = openai_api_key

    return "Key Received!"
# 1.2 create gradio interface
api_tab = gr.Interface(
    fn = get_api_key,
    inputs = [gr.Textbox(label="OpenAI API Key*",
                         placeholder="Paste you OpenAI API key here ...", type="password")
    ],
    outputs = gr.Textbox(label="Message",
                         placeholder="""
Disclaimer: 
This platform uses Artificial Intelligence (AI). Please do not share private or sensitive information during interactions, as AI cannot ensure confidentiality. Exercise discretion for your security."
""")
)

## 2. Tab-Resume Review

# 2.1 set resume review template
resume_review_template = """
You are interviewing {company_name}, {role_title} role with a {interviewer_role}. 
This is your resume {resume}. Please review the resume, job description, and company information below. 
Give point by point feedback with rationale and suggested edits. Also, giving your examples based on your editing suggestions. 
(optional: Here is the job description: {role_description}) 
(optional: Here is a description of the company: {company_description})
No need to include feedback on formatting.
"""

# 2.2 define resume_review function
def resume_review(comp_name, job_title, interviewer_title,
                  comp_info="", job_des="", #interviewer_url="",
                  your_resume=""):

  #### Step 1: Create prompt ####
  # 1. Define variables in prompt
  input_var = ["interviewer_role", "company_name", "resume", "role_title", "role_description", "company_description"]

  # 2. Define prompt template
  template = resume_review_template

  # 3. Create prompt template
  prompt = PromptTemplate(
    input_variables = input_var,
    template = template
  )
  ###############################

  #### Step 2: Read resume PDF to text ####
  extracted_resume = textract.process(your_resume.name, method='pdfminer')
  #########################################

  #### Step 3: Format prompt with user input ####
  new_prompt = prompt.format(interviewer_role=interviewer_title,
                            company_name=comp_name,
                            resume=extracted_resume,
                            role_title=job_title,
                            role_description=job_des,
                            company_description=comp_info)
  ###############################################

  #### Step4: Use chat model to answer the prompt ####
  chat = ChatOpenAI(model_name = "gpt-4")
  result = chat([HumanMessage(content=new_prompt)])
  ####################################################

  return result.content

# 2.3 create gradio interface
resume_review_tab = gr.Interface(
    fn = resume_review,
    inputs = [gr.Textbox(label="Company Name*"),
              gr.Textbox(label="Job Title*",
                         placeholder="The job title you are going to apply goes here ..."),
              gr.Dropdown(["Job Recruiter", "HR Manager", "Hiring Manager", "Executives", "Potential Coworkers"],
                          label="Who do you want to interview with?*"),
              gr.Textbox(label="Company Info (Optional)",
                         placeholder="Sepcial information about this company you want to include"),
              gr.Textbox(label="Job Description (Optional)",
                         placeholder="Paste the job description here ..."),
              #gr.Textbox(label="Interviewer's LinkedIn URL (Optional)",
              #           placeholder="Paste the URL here ..."),
              gr.File(file_types=[".pdf"])
    ],
    outputs = gr.Textbox(label="Feedbacks", lines=50,
                         placeholder="""
**Introduction**:
This tab is designed for tailor your resume for specific role and company you are applying to. 

**Instruction**:
1. Reguired fields are: Company Name, Job Title, Who do you want to interview with, and your_resume (in .pdf version).
2. Company Info, Job Description and Interviewer's LinkedIn URL are optional.

**Disclaimer**: 
This platform uses Artificial Intelligence (AI). Please do not share private or sensitive information during interactions, as AI cannot ensure confidentiality. Exercise discretion for your security.
""")
)


## 3. Tab-Cover Letter

# 3.1 set cover letter template
cover_letter_template = """
As an experienced career coach, you help students improve their skills in
writing a cover letter to get job interviews.  Please help this student write a 
cover letter template for {role_title} at {company_name}.

Here is the student's resume:
{resume}

Here are the job description and company background that you might want to consider:
Job Description: {role_description}
Company Background: {company_description}

Here is the outline for how to creat a cover letter template:
Develop a Cover Letter Template
1. Create Adaptable Template
a. Basic Structure: Establish a clear and concise structure with an introduction, body, and conclusion.
b. Personalize the Opening: Prepare a flexible opening that can be customized to address the specific hiring manager or team.
c. Leave Space for Role-Specific Details: Design sections that can be easily modified to reflect the specific job and company.
2. Incorporate Key Skills and Experiences
a. Highlight Transferable Skills: Emphasize skills that are valuable across various roles and industries.
b. Include Achievements: Add sections to incorporate specific accomplishments relevant to the job.
c. Make It Result-Oriented: Focus on how your skills and experiences can benefit the potential employer.
3. Ensure Easy Customization for Specific Roles
a. Use Modifiable Sections: Create parts of the letter that can be easily changed for different job applications.
b. Align with Job Description: Set up placeholders to insert keywords and requirements from the job description.
c. Tailor to Company Culture: Prepare a segment to adapt based on the company’s culture and values as described on their website or social media.
"""

# 3.2 define cover_letter function
def cover_letter(comp_name, job_title, comp_info="", job_des="", your_resume=""):

  #### Step 1: Create prompt ####
  # 1. Define variables in prompt
  input_var = ["role_title", "company_name", "resume", "role_description",  "company_description"]

  # 2. Define prompt template
  template = cover_letter_template

  # 3. Create prompt template
  prompt = PromptTemplate(
    input_variables = input_var,
    template = template
  )
  ###############################

  #### Step 2: Read resume PDF to text ####
  extracted_resume = textract.process(your_resume.name, method='pdfminer')
  #########################################

  #### Step 3: Format prompt with user input ####
  new_prompt = prompt.format(role_title=job_title,
                             company_name=comp_name,
                             resume=extracted_resume,
                             role_description=job_des,
                             company_description=comp_info)                    
  ###############################################

  #### Step4: Use chat model to answer the prompt ####
  chat = ChatOpenAI(model_name = "gpt-4")
  result = chat([HumanMessage(content=new_prompt)])
  ####################################################

  return result.content

# 3.3 create gradio interface
cover_letter_tab = gr.Interface(
    fn = cover_letter,
    inputs = [gr.Textbox(label="Company Name*"),
              gr.Textbox(label="Job Title*",
                         placeholder="The job title you are going to apply goes here ..."),
              gr.Textbox(label="Company Info (Optional)",
                         placeholder="Sepcial information about this company you want to include"),
              gr.Textbox(label="Job Description (Optional)",
                         placeholder="Paste the job description here ..."),
              gr.File(file_types=[".pdf"])
    ],
    outputs = gr.Textbox(label="Feedbacks", lines=50,
                         placeholder="""
**Introduction**:
This tab is designed for helping users generate a cover letter that tailored for specific role and company the user is going to apply. 

**Instruction**:
1. Reguired fields are: Company Name, Job Title, and your_resume (in .pdf version).
2. Company Info and Job Description are optional.

**Disclaimer**: 
This platform uses Artificial Intelligence (AI). Please do not share private or sensitive information during interactions, as AI cannot ensure confidentiality. Exercise discretion for your security.
""")
)


## 4. Tab-Interveiw Question Generator

# 4.1 set interview question template
interview_question_template = """
As an experienced interviewer for {role_title} at {company_name}, what are the
likely {question_type} interview questions you would like to ask?

Here is the job description: {role_description}
Here is the company description: {company_description}

Here are definitions for different types of interview questions:
Understanding the differences between direct, behavioral, and technical interview questions is crucial for effective interview preparation. Each type serves a specific purpose in evaluating different aspects of a candidate's qualifications and suitability for a role.
1. Direct Interview Questions:
Purpose: These questions are straightforward and are designed to gather factual information about the candidate's background, qualifications, and work experience.
Characteristics: Direct questions are usually clear-cut and require specific, concise answers. They don't typically require candidates to elaborate on scenarios or demonstrate problem-solving skills.
2. Behavioral Interview Questions:
Purpose: These questions are aimed at understanding how a candidate has behaved in specific situations in the past, based on the belief that past behavior is a good predictor of future behavior.
Characteristics: Behavioral questions often start with phrases like "Tell me about a time when..." or "Give me an example of...". They require candidates to tell stories or anecdotes from their past experiences, demonstrating their skills, decision-making abilities, and how they handle work-related situations.
3. Technical Interview Questions:
Purpose: These questions assess the candidate's technical skills and knowledge pertinent to the specific role they are applying for. They are common in fields like IT, engineering, science, or any role that requires specific technical expertise.
Characteristics: Technical questions are often quite specific and can include problem-solving or even practical demonstrations of skills. They may involve scenarios, hypothetical problems, coding tests, or detailed discussions of technologies or methodologies.
Each type of question helps the interviewer gauge different aspects of a candidate's profile. Direct questions assess basic qualifications, behavioral questions evaluate soft skills and cultural fit, and technical questions measure job-specific skills and expertise.
"""

# 4.2 define interview_question function
def interview_question(comp_name, job_title, q_type, comp_info="", job_des=""):

  #### Step 1: Create prompt ####
  # 1. Define variables in prompt
  input_var = ["role_title", "company_name", "question_type", "role_description",  "company_description"]

  # 2. Define prompt template
  template = interview_question_template

  # 3. Create prompt template
  prompt = PromptTemplate(
    input_variables = input_var,
    template = template
  )
  ###############################

  #### Step 2: Read resume PDF to text ####
  #extracted_resume = textract.process(your_resume.name, method='pdfminer')
  #########################################

  #### Step 3: Format prompt with user input ####
  new_prompt = prompt.format(role_title=job_title,
                             company_name=comp_name,
                             question_type=q_type,
                             role_description=job_des,
                             company_description=comp_info)                    
  ###############################################

  #### Step4: Use chat model to answer the prompt ####
  chat = ChatOpenAI(model_name = "gpt-4")
  result = chat([HumanMessage(content=new_prompt)])
  ####################################################

  return result.content

# 4.3 create gradio interface
interview_question_tab = gr.Interface(
    fn = interview_question,
    inputs = [gr.Textbox(label="Company Name*"),
              gr.Textbox(label="Job Title*",
                         placeholder="The job title you are going to apply goes here ..."),
              gr.Dropdown(["Direct question", "Behavioral question", "Technical question"],
                          label="What type of interview questions you want to prepare?*"),
              gr.Textbox(label="Company Info (Optional)",
                         placeholder="Sepcial information about this company you want to include"),
              gr.Textbox(label="Job Description (Optional)",
                         placeholder="Paste the job description here ...")
    ],
    outputs = gr.Textbox(label="Feedbacks", lines=50,
                         placeholder="""
**Introduction**:
This tab is designed for generate the interview questions that interviewer might ask for the specific role and company the user applied. 

**Instruction**:
1. Reguired fields are: Company Name, Job Title, and the type of interview questions you want to prepare.
2. Company Info and Job Description are optional, but including those information will help you get more relevant questions about the role.

**Disclaimer**: 
This platform uses Artificial Intelligence (AI). Please do not share private or sensitive information during interactions, as AI cannot ensure confidentiality. Exercise discretion for your security.
""")
)

## 5. Tab-Answer Evaluation

# 5.1 set answer evaluation template
answer_evaluation_template = """
As an experienced career coach, you help students improve their skills for
answering behavioral interview questions.  Please help this student improve the
answer to the behavioral interview question {interview_questions} during the
interview of {role_title} at {company_name}.

The student’s answer: {question_answers}

First, give the student's answer a score, and point by point feedback with rationale.
Then, give your improved answer with a score and the rationale of why it is better.

Here are job description and company backgroound that you might want to consider:
Job Description: {role_description}
Company Background: {company_description}

Here are aspects that how interviewers should answer a behavioral interview question:
When answering behavioral interview questions, it's essential to present your qualifications effectively by incorporating specific aspects that highlight your skills, experiences, and personal attributes. These aspects are crucial in demonstrating your suitability for the role and how well you align with the organization's values and culture. Here are key aspects to include:
1.        Specific Examples: Use concrete examples from your past experiences to illustrate how you've handled situations relevant to the question. This provides tangible evidence of your skills and abilities.
2.        STAR Method: Structure your response using the STAR method – Situation, Task, Action, and Result. This helps in organizing your answer clearly and concisely:
•        Situation: Describe the context or background of the example you're using.
•        Task: Explain the task or challenge you were facing.
•        Action: Detail the specific actions you took to address the task or challenge.
•        Result: Share the outcomes of your actions, highlighting your contributions and any lessons learned.
3.        Relevance to the Role: Tailor your examples to demonstrate skills and attributes that are directly relevant to the job you're applying for. Show how your past experiences have prepared you for this specific role.
4.        Problem-Solving Skills: Highlight your ability to identify problems, think critically, and implement effective solutions. Employers value candidates who can tackle challenges proactively.
5.        Teamwork and Collaboration: Discuss how you work with others, emphasizing teamwork, communication, and interpersonal skills, especially if the role involves working closely with a team.
6.        Adaptability and Flexibility: Show your ability to adapt to new situations, learn from experiences, and remain flexible in the face of change or uncertainty.
7.        Leadership and Initiative: For roles that require leadership, illustrate your ability to lead, inspire, and motivate others. Even for non-leadership roles, showing initiative and the ability to take charge in appropriate situations can be beneficial.
8.        Results and Impact: Focus on the results and impact of your actions. Quantify your achievements where possible, as this adds credibility and a sense of scale to your accomplishments.
9.        Personal Development: Reflect on what you learned from the experience and how it contributed to your personal and professional growth.
10.        Cultural Fit: Convey how your values, work ethic, and personality align with the company's culture. Show that you not only have the skills for the job but also would thrive in the organization's environment.
Including these aspects in your behavioral interview responses can significantly strengthen your answers, showcasing your qualifications, experiences, and fit for the role.

Here are aspects that companies hope to get from your answer of a behavioral question:
Companies conduct behavioral interviews to assess various aspects of a candidate's past behavior, skills, and performance to predict their future behavior and suitability for the role in their organization. Here are some key elements that companies typically look for during behavioral interviews:
1.        Past Performance as an Indicator of Future Behavior: Companies believe that past behavior is a good predictor of future behavior. By understanding how you handled situations in the past, they can gauge how you might perform in similar situations in their organization.
2.        Problem-Solving and Decision-Making Skills: Employers look for candidates who can demonstrate effective problem-solving and decision-making skills. They are interested in how you approach challenges, analyze problems, and arrive at solutions.
3.        Teamwork and Collaboration: Since most roles require some level of teamwork, companies want to see how well you work with others. Your ability to collaborate, communicate effectively, and contribute to a team is crucial.
4.        Adaptability and Flexibility: With the fast pace of change in the workplace, companies seek candidates who can adapt to new situations and challenges quickly and effectively.
5.        Leadership Qualities: For roles that involve leading others, employers look for leadership potential. This includes your ability to motivate, guide, and influence others, even if the role is not a traditional leadership position.
6.        Work Ethic and Professionalism: Your approach to work, commitment to quality, and professional conduct are important to employers. They want to ensure you have a strong work ethic and can represent the company positively.
7.        Cultural Fit: Companies are keen on finding candidates who will fit well with their organizational culture. This includes sharing similar values, work styles, and the ability to thrive in the company’s work environment.
8.        Resilience and Stress Management: Employers may look for signs of resilience and your ability to handle stress or failure. They want employees who can remain productive and positive, even in challenging situations.
9.        Communication Skills: Effective communication is key in any role. Companies assess your ability to articulate ideas clearly, listen to others, and communicate in a way that is effective and appropriate for the workplace.
10.        Initiative and Self-motivation: Demonstrating that you are a self-starter who takes initiative is highly valued. Companies prefer candidates who show they can work independently and are motivated to achieve.
In summary, behavioral interviews are designed to evaluate a candidate's suitability not only in terms of skills and experience but also in terms of their personality, work habits, and potential fit within the company's culture and team dynamics.
"""

# 5.2 define answer_evaluation function
def answer_evaluation(comp_name, job_title, inter_q, q_a, comp_info="", job_des=""):

  #### Step 1: Create prompt ####
  # 1. Define variables in prompt
  input_var = ["interview_questions", "role_title", "company_name", "question_answers", "role_description",  "company_description"]

  # 2. Define prompt template
  template = answer_evaluation_template

  # 3. Create prompt template
  prompt = PromptTemplate(
    input_variables = input_var,
    template = template
  )
  ###############################

  #### Step 2: Read resume PDF to text ####
  #extracted_resume = textract.process(your_resume.name, method='pdfminer')
  #########################################

  #### Step 3: Format prompt with user input ####
  new_prompt = prompt.format(interview_questions=inter_q,
                             role_title=job_title,
                             company_name=comp_name,
                             question_answers=q_a,
                             role_description=job_des,
                             company_description=comp_info
      )                    
  ###############################################

  #### Step4: Use chat model to answer the prompt ####
  chat = ChatOpenAI(model_name = "gpt-4")
  result = chat([HumanMessage(content=new_prompt)])
  ####################################################

  return result.content

# 5.3 create gradio interface
answer_evaluation_tab = gr.Interface(
    fn = answer_evaluation,
    inputs = [gr.Textbox(label="Company Name*"),
              gr.Textbox(label="Job Title*",
                         placeholder="The job title you are going to apply goes here ..."),
              gr.Textbox(label="Interview Question*",
                         placeholder="Paste the question you want to prepare here ..."),
              gr.Textbox(label="Your Answer*",
                          placeholder="Type your answer for the interview question here ..."),
              gr.Textbox(label="Company Info (Optional)",
                         placeholder="Sepcial information about this company you want to include"),
              gr.Textbox(label="Job Description (Optional)",
                         placeholder="Paste the job description here ...")
    ],
    outputs = gr.Textbox(label="Feedbacks", lines=50,
                         placeholder="""
**Introduction**:
This tab is designed for improve uers' answers for certain interview question. 

**Instruction**:
1. Reguired fields are: Company Name, Job Title, Interview Question, and Your Answer.
2. Company Info and Job Description are optional, but including those information will help you get more relevant answer for the interview question about the role.

**Disclaimer**: 
This platform uses Artificial Intelligence (AI). Please do not share private or sensitive information during interactions, as AI cannot ensure confidentiality. Exercise discretion for your security.
""")
)





## 6. Output gradio

demo = gr.TabbedInterface([api_tab, 
                           resume_review_tab,
                           cover_letter_tab,
                           interview_question_tab,
                           answer_evaluation_tab], 
                            ["OpenAI API Login", 
                             "Resume Review",
                             "Cover Letter",
                             "Interview Questions Generator",
                             "Improve Interview Answer"]
                          )

if __name__ == "__main__":
    demo.launch(debug=True)



