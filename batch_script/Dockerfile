FROM python:3.7

ENV APP_HOME /script
WORKDIR $APP_HOME

ADD requirements.txt /script/
RUN pip3 install -r requirements.txt
ADD . /script
COPY . ./


RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]