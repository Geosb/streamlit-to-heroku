FROM python:3.7-slim-buster
COPY . /CancerPt
COPY . /breastCancer.dataTOp2.ipynb
COPY requirement.txt /requirement.txt
WORKDIR /CancerPt
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers-4 --bind 0.0.0.0:$PORT CancerPt:CancerPt
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
