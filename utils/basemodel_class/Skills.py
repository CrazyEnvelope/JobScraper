from pydantic import BaseModel,Field
from typing import Optional

class Skills(BaseModel):
    required_skills: list[str] = []
    preferred_skills: list[str] = []