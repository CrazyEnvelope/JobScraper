from pydantic import BaseModel,Field
from typing import Optional

class Responsibilities(BaseModel):
    responsibilities: list[str] = []
