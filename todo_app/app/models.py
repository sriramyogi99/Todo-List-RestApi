from typing import List, Optional
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
