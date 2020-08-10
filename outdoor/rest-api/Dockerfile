FROM python:3-onbuild
COPY ./src/ /app/
COPY ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "/app/gardenServer.py"]