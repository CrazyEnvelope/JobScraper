from pydantic import BaseModel,Field
from typing import Optional

class BasicInfo(BaseModel):
    company_description: Optional[str] = Field(
        "N/A",
        description=(
            "A 1-2 sentence summary of what the company does, written in your own words. "
            "Base this on ANY relevant context in the posting — mission statements, 'About' "
            "sections, phrases like 'our client is...', or descriptions of their product/platform. "
            "Synthesize a summary rather than copying a sentence verbatim. "
            "Only leave this null if there is truly no information anywhere about what the company does."
        )
    )
    min_salary: str = Field(
        "N/A",
        description=(
            "Extract the minimum number of years of professional work experience "
            "explicitly required by the job posting. "
            "Look for the exact phrase 'years of experience' or similar wording. "
            "For example, if the posting says '5+ years of professional software "
            "engineering experience', return '5 years'. "
            "If it says '3-5 years of experience', return '3 years'. "
            "If no explicit years of professional experience are stated, return 'N/A'."
        )
    )
    max_salary: Optional[str] = Field(
        "N/A",
        description=(
            "The HIGHEST salary amount explicitly stated in the job posting. "
            "If a salary range is stated, extract the higher number. "
            "Include the currency, for example '$120,000', '€100,000', '£90,000', "
            "or '120000 USD'. Do not calculate or convert currencies. "
            "If no salary is explicitly stated, return 'N/A'."
        )
    )
    min_years_experience: Optional[str] = Field(
        "N/A",
        description=(
            "Search for the years of experience in the description and try harder to extract it."
            "If no explicit number of years is present, return 'N/A'."
        )
    )
    education_level: Optional[str] = Field(
        "N/A",
        description=(
            "The degree level required or preferred, e.g. 'Bachelor's degree', 'Master's degree', "
            "'PhD'. Do not include the field of study here. Leave null if not stated."
            "If no explicit education_level is present, return 'N/A'."
        )
    )

    field_of_study: Optional[str] = Field(
        "N/A",
        description=(
            "The academic subject or major only, e.g. 'Computer Science', 'Engineering'. "
            "Do NOT include industry experience, tools, or preferred qualifications here. "
            "Leave null if not stated."
        )
    )