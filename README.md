# cobweb
All-in-One project template for local development. You can startup with Docker Comopse.

1. [Database](#database) - PostgreSQL
2. [Server / Web Application for Admin](#server) - Django / Django REST framework
3. [Batch](#batch) - PySpark
4. [Mobile App](#app) - React Native / Expo

## DATABASE
### Overview
[PostgreSQL](https://www.postgresql.org). Manage minimum setting, such as database and roll in init.sql. The other DMLs are managed with Django.

### Quick Start
Startup PostgreSQL on `localhost:5432`.
```bash
cd database
docker-compose up -d
```

### Setting
| File | Propery | Descriptioon | Example |
| ---- | ---- | ---- | ---- |
| .env | `DOCKER_POSTGRES_VERSION` | [PostgreSQL docker image](https://hub.docker.com/_/postgres) version. | `latest` |
| .env | `PROFILE` | Used for select init.sql. | `local` |
| .env | `POSTGRES_USER` | Superuser role for initialize database. | `postgres` |
| .env | `POSTGRES_PASSWORD` | Superuser password for initialize database. | `password` |

### Requirements for Developer
- [psql](https://www.postgresql.org/docs/current/app-psql.html)

## SERVER
### Overview
[Django](https://docs.djangoproject.com) and [Django REST framework](https://www.django-rest-framework.org). Application server and web application for admin.

### Quick Start
Startup web application for admin on [http://localhost:8000/admin/](http://localhost:8000/admin/). Database must be setup before.
```bash
cd server
docker-compose up -d
```

For debug:
```bash
cd server
# create static directory and collect static files.
python manage.py collectstatic
# migrate DDL.
python manage.py migrate
# create super user.
python manage.py createsuperuser --noinput
# run server for debug.
python manage.py runserver
```

### Setting
| File | Propery | Descriptioon | Example |
| ---- | ---- | ---- | ---- |
| .env | `DOCKER_PYTHON_VERSION` | [Python docker image](https://hub.docker.com/_/python) version. | `3` |
| .env | `SECRET_KEY` | Secret key for Django. See [Django documentation](https://docs.djangoproject.com). | - |
| .env | `DEBUG` | Debug. See [Django documentation](https://docs.djangoproject.com). | `False` |
| .env | `ALLOWED_HOSTS` | Allowed host. Separate with comma. | `localhost,127.0.0.1,10.0.2.2` |
| .env | `DATABASE_NAME` | Accessing database name. | `cobweb` |
| .env | `DATABASE_USER` | Accessing database role. | `django` |
| .env | `DATABASE_PASSWORD` | Accessing database password. | `password` |
| .env | `DATABASE_HOST` | Database host. | `127.0.0.1` |
| .env | `DATABASE_PORT` | Database port. | `5432` |
| .env | `DJANGO_SUPERUSER_USERNAME` | First web application super user name. | `admin` |
| .env | `DJANGO_SUPERUSER_EMAIL` | First web application super user email. | `admin@cobweb.com` |
| .env | `DJANGO_SUPERUSER_PASSWORD` | First web application super user password. | `password` |

### Requirements for Developer
- [Python](https://www.python.org)

## BATCH
### Overview
[PySpark](https://spark.apache.org/docs/latest/api/python/index.html).

### Quick Start
Execute batch application. Batch status would be displayed on [http://localhost:8080](http://localhost:8080).
```bash
cd batch
docker-compose up -d
docker-compose exec master /bin/bash /opt/spark/work-dir/cobweb/bin/exec.sh ${APP_NAME}
```

### Setting
| File | Propery | Descriptioon | Example |
| ---- | ---- | ---- | ---- |
| .env | `DOCKER_SPARKPY_VERSION` | [PySpark docker image](https://hub.docker.com/r/apache/spark-py) version. | `latest` |
| .env | `DOCKER_WORKDIR` | Docker working directory. | `/opt/spark/work-dir` |
| .env | `DOCKER_JDBC_POSTGRES` | JDBC PostgreSQL jar file URL. Download in Dockerfile. | `https://jdbc.postgresql.org/download/postgresql-42.7.3.jar` |
| .env | `SPARK_DATABASE_URL` | Database URL for JDBC. | `jdbc:postgresql://host.docker.internal:5432/cobweb` |
| .env | `SPARK_DATABASE_USER` | Accessing database role. | `django` |
| .env | `SPARK_DATABASE_PASSWORD` | Accessing database password. | `passwords` |

### Requirements for Developer
- [Python](https://www.python.org)

## APP
### Overview
[React Native](https://reactnative.dev) with [Expo](https://expo.dev/).

### Quick Start
Startup expo server.
```bash
cd app
npm start
```

### Setting
See [Expo Docs](https://docs.expo.dev).

### Requirements for Developer
- [Node.js](https://nodejs.org/)
- [Expo Go](https://expo.dev/go)
- [Android Studio](https://developer.android.com/studio)
- [Xcode](https://developer.apple.com/xcode/)
- [Expo Account](https://expo.dev/signup)
- [Google Play Console Developer Account](https://play.google.com/console/signup)
- [Apple Developer Program](https://developer.apple.com/programs/)
