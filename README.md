# join.to.it_test_task

## Instruction to start server
### 1. Create venv
- ```python -m venv venv```
- ```. venv/bin/activate```
### 2. Install requirements
- ```pip install --upgrade pip```
- ```pip install -r requirements.txt```
### 3. Create .env file and fill it with your data (example in .env_tmp)
### 4. Make migrations
- ```python manage.py makemigrations```
- ```python manage.py migrate```
### 5. Run server
- ```python manage.py runserver```

