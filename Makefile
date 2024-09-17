setup:
	virtualenv .venv -p python3.10
	./.venv/bin/pip install pip-tools

install:
	./.venv/bin/pip-compile ./requirements/requirements-core.txt \
							./requirements/requirements-dev.txt \
							./requirements/requirements-test.txt \
	 						--output-file ./requirements.txt -v
	./.venv/bin/pip-sync -v


collect-static:
	python manage.py collectstatic --noinput

migrate:
	python manage.py makemigrations
	python manage.py migrate

setup-dev-user:
	DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=password python manage.py createsuperuser --noinput

run:
	daphne -b 0.0.0.0 -p 8000 weops_lite.asgi:application

clean-migrate:
	cd apps &&\
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete &&\
	find . -path "*/migrations/*.pyc"  -delete

init-buckets:
	python manage.py initialize_buckets

celery:
	celery -A core worker -B --loglevel=info --pool threads

celery-inspect:
	celery -A core inspect scheduled

celery-flower:
	celery -A core flower

push:
	git add . && codegpt commit . && git push