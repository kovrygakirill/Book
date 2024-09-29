# Requirements

1. python 3.10.7

# How to start?

1. Activate virtual environment
2. Add environment variables to environment or create `.env` file
3. pip install pipenv
4. pipenv install --dev
5. python manage.py migrate
6. python manage.py runserver 0.0.0.0:8000

# or from docker

1. docker-compose -f docker-compose.yml up --build -d
