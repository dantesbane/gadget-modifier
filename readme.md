# Steps to run 
1. docker compose build
2. docker compose up  -- this will start django and postgres server
3. docker compose run --rm app sh -c "python manage.py createsuperuser"    --this will create your user account
