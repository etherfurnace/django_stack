FROM python:3.10
WORKDIR /apps

RUN apt-get update -y && \
    apt-get install -y vim &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD . .

RUN pip install pip-tools
RUN pip-compile ./requirements/requirements-core.txt \
                ./requirements/requirements-dev.txt \
                ./requirements/requirements-test.txt \
                --output-file ./requirements.txt -v\
RUN pip-sync -v

ENV SECRET_KEY django-insecure-wi*fg%43$^^bwbus!1+p2sud3wnpe@3$is$3h8$cdw6h+s!-ug
ENV DEBUG False

RUN python manage.py collectstatic --noinput