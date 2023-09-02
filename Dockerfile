FROM gitlab.pollche.com:5050/devops-pub/python-image/django-base-image:python3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#ENV HTTP_PROXY="socks5://10.10.0.1:9070"
#ENV HTTPS_PROXY="socks5://10.10.0.1:9070"
#ENV NO_PROXY="10.10.0.1/16,localhost,127.0.0.1"

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN --mount=type=cache,target=/home/gitlab-runner/.cache \
    pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app

USER appuser
#EXPOSE 8000
