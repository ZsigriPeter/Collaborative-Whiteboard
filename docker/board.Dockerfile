FROM python:3.12

WORKDIR /app

COPY backend/board-service/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/board-service .

COPY backend/board-service/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
