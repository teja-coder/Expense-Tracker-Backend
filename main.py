from fastapi import FastAPI, HTTPException, status, Response
from datetime import date, datetime
from database import add_expense_db, get_expenses_db, get_categories_db, add_category_db
from models import Expense, Message_Expense, Message_Category, Category

app = FastAPI()

@app.post("/add-expense", response_model=Message_Expense)
def add_expense(expense: Expense):
    
    try:
        expense = expense.dict()

        if not expense['expense_date']:
            expense['expense_date'] = datetime.now()

        expense_added = add_expense_db(expense)

        if expense_added:

            response_content = Message_Expense(status = 1, message = "Expense Added successfully").json()
            return Response(content=response_content, status_code=status.HTTP_200_OK)
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error occurred while adding Expense")
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/expenses", response_model=Message_Expense)
def fetch_expense():

    try:
        expenses = get_expenses_db()
        if expenses or len(expenses) == 0:
            content = Message_Expense(status=1, message='Successfully loaded expenses', data=expenses).json()
            return Response(status_code=status.HTTP_200_OK, content=content, media_type='application/json') 

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error occurred while fetching expenses")

    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@app.get('/categories', response_model=Message_Category)
def get_categories():

    try:
        categories = get_categories_db()
        if categories or len(categories) == 0:
            content = Message_Category(status=1, message='Successfully loaded categories', data=categories).json()
            return Response(status_code=status.HTTP_200_OK, content=content, media_type='application/json')

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error occurred while fetching categories")

    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@app.post('/add-category', response_model=Message_Category)
def add_category(category: Category):
    try:
        category = category.dict()

        category_added = add_category_db(category)

        if category_added:

            response_content = Message_Category(status = 1, message = "Category Added successfully").json()
            return Response(content=response_content, status_code=status.HTTP_200_OK)
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error occurred while adding Category")
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    