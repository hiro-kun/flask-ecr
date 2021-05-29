FROM centos:latest

LABEL ono-hiroshi <hiroshi_ono_1989@yahoo.co.jp>

RUN yum install -y python3

RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python3

RUN pip install Flask
RUN yum install -y mysql