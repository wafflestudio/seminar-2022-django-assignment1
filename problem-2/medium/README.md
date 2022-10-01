# Medium Blog Posts API with DRF

## Prerequisite
- pyenv
- docker 

#
## API Docs
| method   | url             | description           |
|----------|-----------------|-----------------------|
| `GET`    | `/v1/posts/`    | list posts            |
| `POST`   | `/v1/posts/`    | create a post         |
| `GET`    | `/v1/posts/:id` | detail a post         |
| `PUT`    | `/v1/posts/:id` | update a post         |
| `PATCH`  | `/v1/posts/:id` | partial update a post |
| `DELETE` | `/v1/posts/:id` | delete a post         |

if you use `v1` -> `v2`, you can use api with function based view 
#
## Make VirtualEnv
```bash
pyenv virtualenv 3.8.11 medium
pyenv activate medium
pip install -r requirements.txt
```
#
## Init & Connect Postgres DB 
```bash
docker run --name postgresql \
    -e POSTGRES_USER=[username] \
    -e POSTGRES_PASSWORD=[password] \
    -p 5432:5432 \
    -v /data:/var/lib/postgresql/data \
    -d postgres
```
Edit `medium/settings.py`
```python
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': [username],
        'PASSWORD': [password],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
...
```
#
## Run Server
```bash
python manage.py makemigrations
python manage.py migrate
python mange.py runserver
```
localhost address : <https://127.0.0.1:8000/>
#
## Style Guide

Before commit, please lint & reformatting first
```bash
sh reformat.sh
```
