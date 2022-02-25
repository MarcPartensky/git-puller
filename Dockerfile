FROM python:3.10.2-alpine

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-sSf", "localhost:8000" ]
ENTRYPOINT ["python", "__main__.py"]
