FROM python:3.12

WORKDIR /app

COPY backend/auth-service/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/auth-service .

COPY backend/auth-service/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]