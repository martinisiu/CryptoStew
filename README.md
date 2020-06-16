# CryptoStew


To run the application
$ docker-compose up -d --build

The django page will run on:
http://localhost:1337/

To apply migrations and run other django commands
$ docker-compose exec web python manage.py migrate
