FROM python:3.12

WORKDIR /app

COPY backend/realtime-service/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/realtime-service .

CMD ["daphne", "-b", "0.0.0.0", "-p", "8002", "realtime_service.asgi:application"]

