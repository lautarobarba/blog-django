# blog-django
Personal blog made with Django Web Framework

## Start virtualenv
After cloning the project source the virtualenv

```bash
$ git clone https://github.com/lautarobarba/blog-django.git
$ cd blog-django
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ #Update pip if needed
(venv) $ python3 -m pip install --upgrade pip
```

## Start postgreSQL
### Install postgreSQL
For Arch Linux:
```bash
    $ sudo pacman -S postgresql
    $ postgres --version
    postgres (PostgreSQL) 12.3
```

### Enable and Start the service
```bash
    $ sudo systemctl start postgresql
    $ systemctl status postgresql
    $ sudo systemctl enable postgresql
```

### Change postgres user's password
```bash
    $ sudo passwd postgres
```

### Login with postgres user
```bash
    $ sudo su postgres
    [postgres]$ id
```

### Create new user and database for the project
```bash
    [postgres]$ psql
    postgres=# \l
    postgres=# CREATE USER blog_user WITH SUPERUSER CREATEDB;
    postgres=# \du
    postgres=# \dg
    postgres=# \password blog_user
    postgres=# CREATE DATABASE blog_database OWNER blog_user;
    postgres=# \c blog_database blog_user
    blog_database=# \conninfo
    blog_database=# \q
```

### PostgreSQL is ready to work with this data
```bash
    Database: blog_database
    User: blog_user
    Password: ******
```

### Export data as Environment Variables
Add inside .xinitrc or .xprofile
```bash
    export DJANGO_DBNAME=blog_database
    export DJANGO_DBUSER=blog_user
    export DJANGO_DBPASSWORD=****** (use real password)
```

### Notes
Check database data with DBeaver or pgAdmin4

## Start blog
```bash
(venv) $ cd src
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py runserver
```

Dews!
