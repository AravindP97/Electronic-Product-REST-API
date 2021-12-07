import os
os.system("python manage.py makemigrations users") 
os.system("python manage.py makemigrations products") 
os.system("python manage.py migrate")
os.system("python manage.py runserver")