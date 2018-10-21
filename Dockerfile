FROM python:3.7-alpine
EXPOSE 8080
CMD ["python","/app/src/main.py", "8080"]
WORKDIR /app
COPY setup.py setup.py
COPY src /app/src
RUN pip install -e .
