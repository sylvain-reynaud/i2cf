FROM python:3.9


RUN pip install --no-cache-dir --upgrade flask neo4j

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]