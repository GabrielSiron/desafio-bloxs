FROM python:3.8-slim-buster 

RUN mkdir app/

WORKDIR app/

COPY . .

RUN pip3 install PyMySQL

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]