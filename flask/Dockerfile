FROM centos:latest

LABEL ono-hiroshi <hiroshi_ono_1989@yahoo.co.jp>

EXPOSE 5000

RUN dnf install -y python3

RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python3

RUN dnf install -y mysql
RUN dnf install -y python3-setuptools 
RUN dnf install -y mysql-devel

RUN pip install Flask
RUN pip install mysql-connector-python-rf

# 以下は単体で起動する場合
COPY ./module /opt/module/
ENV FLASK_APP /opt/module/sample.py
CMD ["flask", "run", "-h", "0.0.0.0"]
#docker run -p 5000:5000 imageID