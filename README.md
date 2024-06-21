# join.to.it_test_task

## Instruction to start server
### 1. Create venv
- ```python3 -m venv venv```
- ```. venv/bin/activate```
### 2. Install requirements
- ```pip install --upgrade pip```
- ```pip install -r requirements.txt```
### 3. Create .env file and fill it with your data:
- SECRET_KEY =
- EMAIL_HOST_USER =
- EMAIL_HOST_PASSWORD =
### 4. Make migrations
- ```python server/manage.py makemigrations```
- ```python server/manage.py migrate```
### 5. Run server
- ```python server/manage.py runserver```

