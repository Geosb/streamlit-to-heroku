FROM python:3.11
COPY . /CancerPt
WORKDIR /CancerPt
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers-4 --bind 0.0.0.0:$PORT CancerPt:CancerPt