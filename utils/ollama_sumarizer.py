from ollama import chat
from utils.basemodel_class.BasicInfo import BasicInfo
from utils.basemodel_class.Skills import Skills
from utils.basemodel_class.Responsibilities import Responsibilities

def resume_job_description(job_description_text):
    basic = extract(job_description_text, BasicInfo)
    skills = extract(job_description_text, Skills)
    resp = extract(job_description_text, Responsibilities)

    basic_skill_resp = {
        "BasicInfo": {
            "company_description" : basic.company_description,
            "min_salary" : basic.min_salary,
            "max_salary" : basic.max_salary,
            "min_years" : basic.min_years_experience,
            "education_level" : basic.education_level,
            "field_of_study" : basic.field_of_study,
        },
        "Skills":{
            "required_skills": skills.required_skills,
            "preferred_skills": skills.preferred_skills,
        },
        "Responsabilities":{
            "responsabilities": resp.responsibilities,
        }
    }

    return basic_skill_resp

def extract(job_description_text, baseModel):
    system_prompt = """
    Extract the relevant information from the job posting according to the supplied JSON schema.

    IMPORTANT RULES:

    1. Read the ENTIRE job posting before extracting any field.

    2. Use ONLY information explicitly stated in the posting.
       Never guess, infer, calculate, or assume.

    3. For company_description:
       - Search the entire posting for company information.
       - This includes "About", "General Information", "Our client", mission,
         product descriptions, and service descriptions.
       - Write a concise 1-2 sentence summary in your own words.

    4. Follow the field descriptions in the JSON schema.

    5. Return ONLY valid JSON.
    """

    response = chat(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", 'content': f"Extract relevant information from this description: {job_description_text}"},
        ],
        model='llama3.2',
        format=baseModel.model_json_schema(),
        options={
            "temperature": 0,
            "num_predict": 2048,
            "num_ctx": 8192
        },
    )

    return baseModel.model_validate_json(response.message.content)

