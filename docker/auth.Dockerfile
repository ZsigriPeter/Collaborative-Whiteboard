FROM python:3.12

WORKDIR /app

COPY backend/auth-service/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/auth-service .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
