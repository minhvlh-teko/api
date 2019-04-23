FROM python:3.7

EXPOSE 5000
WORKDIR /code
ADD requirements.txt /code/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /code/

RUN chmod +x wait-for-it.sh

CMD ["sh", "-c", "./wait-for-it.sh postgresql:5432 -t 0 -- flask db upgrade heads && flask run --host=0.0.0.0 --port=5000"]


