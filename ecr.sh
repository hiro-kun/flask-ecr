# ログイン
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 761343251450.dkr.ecr.ap-northeast-1.amazonaws.com

# app push
docker tag flask-ecr_app 761343251450.dkr.ecr.ap-northeast-1.amazonaws.com/flask-ecr_app:latest
docker push 761343251450.dkr.ecr.ap-northeast-1.amazonaws.com/flask-ecr_app:latest

# db push
docker tag flask-ecr_db 761343251450.dkr.ecr.ap-northeast-1.amazonaws.com/flask-ecr_db:latest
docker push 761343251450.dkr.ecr.ap-northeast-1.amazonaws.com/flask-ecr_db:latest