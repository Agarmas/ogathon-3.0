from typing import List
from pydantic import BaseModel, Field, RootModel, field_validator

class QueryN(BaseModel):
    n: int = Field(..., gt=0)

class RecycleMatrix(RootModel[List[List[int]]]):
    root: List[List[int]] = Field(...)

    @field_validator('root', mode='after')
    @classmethod
    def check_3x3(cls, v: List[List[int]]) -> List[List[int]]:
        if len(v) != 3 or any(len(row) != 3 for row in v):
            raise ValueError('The matrix must be 3x3 integers')
        if not all(isinstance(item, int) for row in v for item in row):
            raise ValueError('All elements must be integers')
        return v