FROM nginx:latest

LABEL ono-hiroshi <hiroshi_ono_1989@yahoo.co.jp>

COPY ./conf/default.conf /etc/nginx/conf.d/default.conf
COPY ./html/index.html /usr/share/nginx/html/index.html

EXPOSE 80

# docker build . -t nginx-sample
# docker run --name my-nginx -d -p 80:80 e5b93488721d
# docker stop my-nginx