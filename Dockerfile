FROM python:3.13.1-slim
WORKDIR /usr/src/app
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser 
USER appuser
EXPOSE 8001
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "-k", "uvicorn.workers.UvicornWorker", "main:app"]