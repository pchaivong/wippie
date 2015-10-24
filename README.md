README
==============

Setting up project
--------------

```bash
# 1. Create working directory (Optional)
mkdir workspace
cd workspace
# 2. Checkout source code from github
git clone https://github.com/pchaivong/wippie.git
cd wippie

# 3. Create virtual environment
# Highly recommended using name 'env' because it's has been added to .gitignore file already
# If you use another name, ensure that you add that name to .gitignore as well.
virtualenv env

# 4. Activate using virtual environment (Windows)
.\env\Scripts\activate
# For Mac or Linux
source env/bin/activate

# 5. Download all mandatory library
pip install -r requirements.txt
```

Set up database
--------------

```bash
cd wippie
python manage.py makemigrations
python manage.py migrate
# There will be 'db.sqlite3' file created
```


Create Super User
--------------

```bash
python manage.py createsuperuser
#Put email(used as a username when login), password, and date of birth
```

Run Server
--------------
Test running server and using admin portal

```bash
python manage.py runserver 8080
# Launch chrome and browse to http://localhost:8080/admin
# Port number can be changed
```

Holiday Model (example)
--------------
Holiday model has been added. Also already implemented a serializer class and viewset
For demonstration purposes.

You can check it at

```bash
http://localhost:8080/api/holiday
```








