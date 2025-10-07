from pydantic import BaseModel

class Classement(BaseModel):
    name: str
    total_Points: int
    avg_Points: int
    min_Points: int
    max_Points: int