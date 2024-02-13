FROM python:3

WORKDIR /app

COPY requirments.txt /app/

RUN python -m pip install -r requirments.txt

COPY . /app/

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver