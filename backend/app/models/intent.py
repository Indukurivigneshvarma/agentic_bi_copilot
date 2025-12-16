from pydantic import BaseModel
from typing import Optional

class Intent(BaseModel):
    chart_type: str
    metric: str
    column: Optional[str]
    student_name: Optional[str]
    student_id: Optional[str]
