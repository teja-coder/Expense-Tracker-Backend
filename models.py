from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class Expense(BaseModel):
    expense_name: str
    expense_category: str
    expense_date: Optional[datetime] = None
    expense_amount: float

class Category(BaseModel):
    category: str

class Message_Expense(BaseModel):
    status: int
    message: str
    data: Optional[List[Expense]] = None

class Message_Category(BaseModel):
    status: int
    message: str
    data: Optional[List[Category]] = None