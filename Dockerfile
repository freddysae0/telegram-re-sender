FROM python:3.13.0rc1-alpine3.20

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY ./resender.py ./

CMD [ "python" , "resender.py" ]
