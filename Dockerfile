FROM python:3.10-slim 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends\
        build-essential\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip\
    && pip install --no-cache-dir -r requirements.txt 

COPY app/ ./app
COPY src/ ./src 
COPY models/ ./models 

RUN useradd -m appuser  && chown - R appuser:appuser /app
USER appuser 

EXPOSE 8000

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]