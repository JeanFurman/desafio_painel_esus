FROM python:3.9

WORKDIR /app

COPY . /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
