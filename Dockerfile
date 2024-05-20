FROM python:alpine
WORKDIR /opt/app
RUN pip3 install flask
COPY app.py .
ENV FLASK_APP=app.py
EXPOSE 3000
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
