<h1>Electronic-Products-Rest-API MYSQL</h1>
<p>REST API using user managment in Django</p>
<ul>
    <li> 
        <p>1. Clone the git repo - git clone <code>https://github.com/AravindP97/Electronic-Product-REST-API.git </code></p>
    </li>
    <li>
        <p>2. Use database/script.sql file to crete a SQL table needed in your mysql server for this demo project</p>
    </li>
    <li>
        <p>3. Change database connection details in <code>main/settings.py</code> file's line #70</p>
    </li>
    <li>
        <code>
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': '<databasename>',
                    'USER': '<username>',
                    'PASSWORD': '<password>',
                    'HOST': 'localhost',
                    'PORT': 5432,
                    'OPTIONS': {
                       'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
                    }
                }
            }
        </code>
    </li>
    <li>
        <p>4. pip install -r requirements.txt</p>
    </li>
    <li>
        <p>5. python manage.py runserver</p>
    </li>
    <li>
        <p>Note: Product CRUD API calls alone require Api Auth key to be passed in the header of the api request. To generate an Api Auth key, you must login with your mail and password or sign up to the application & login.</p>
    </li>
    <li>
        <p>sign up json</p>
        <code>
            {
                "username": "",
                "email": "",
                "password": "",
            }
        </code>
        <p>Login Json</p>
        <code>
            {
                "email":"",
                "password":""
            }
        </code>
        <p>Product Json</p>
        <code>
            {
                "name": "ACER",
                "description": "Gaming Laptop",
                "category": "L",
                "processor": "i8",
                "ram":"16GB"
                "laptop": {
                    "hd_capacity": "FHD",
                },
                "mobile": {
                    "screen_size": "",
                    "color": ""
                }
            }
        </code>
    </li>
</ul>