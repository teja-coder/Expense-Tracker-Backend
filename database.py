from pymongo import MongoClient
from models import Expense, Category
from typing import List, Optional
from datetime import datetime

from pymongo.server_api import ServerApi
uri = "mongodb+srv://divyateja:Teja_2002@atlascluster.lpgz4rh.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.expense_tracker

collection_exp = db['expenses']
collection_cat = db['categories']

def serialize_expenses(expenses: List[dict]) -> List[dict]:
    serialized_expenses = []
    for expense in expenses:
        expense["expense_id"] = str(expense["_id"])
        expense['expense_date'] = expense['expense_date'].strftime("%Y-%m-%d %H:%M:%S")
        serialized_expenses.append(expense)
    return serialized_expenses

def serialize_categories(categories: List[dict]) -> List[dict]:
    serialized_cat = []
    for cat in categories:
        cat['category_id'] = str(cat['_id'])
        serialized_cat.append(cat)
    return serialized_cat

def add_expense_db(expense: Expense):

    try:
        exp = collection_exp.insert_one(expense)
        return exp
    
    except Exception as e:
        raise Exception(e)

def get_expenses_db():

    try:
        expenses = list(collection_exp.find())
        expenses = serialize_expenses(expenses)
        return expenses
        
    except Exception as e:
        raise Exception(e)
    
def add_category_db(category: Category):

    try:
        cat = collection_cat.insert_one(category)
        return cat
    except Exception as e:
        raise Exception(e)
    
def get_categories_db():

    try:
        categories = list(collection_cat.find())
        categories = serialize_categories(categories)
        return categories
    except Exception as e:
        raise Exception(e)
