FROM python:3.12

WORKDIR /app

# Install deps
COPY backend/board-service/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy app code
COPY backend/board-service .

# Copy entrypoint script into the container
COPY backend/board-service/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use entrypoint instead of CMD
ENTRYPOINT ["/entrypoint.sh"]
