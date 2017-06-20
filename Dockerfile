FROM python:3
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN mkdir /src
COPY . /src

CMD python /src/main.py


