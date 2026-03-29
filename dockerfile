FROM python:3.12

WORKDIR /cicd-pipeline
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "server.py"]