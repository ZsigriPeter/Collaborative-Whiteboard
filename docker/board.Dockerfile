FROM python:3.12

WORKDIR /app

COPY backend/board-service/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/board-service .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
