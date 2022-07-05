# Quickstart

```
docker-compose up -d --build
docker-compose exec web python manage.py migrate

http://127.0.0.1:8000/
```

# API Reference

**/api/v1/auth/** — POST<br/>
**/api/v1/user/** — GET, POST<br/>
**/api/v1/user/<user_id>** — GET, PUT, PATCH, DELETE<br/>
**/api/v1/user/<user_id>/subordinates/** — GET, PUT<br/>
**/api/v1/user/<user_id>/supervisor/** — GET, PUT<br/>
**/api/v1/structure/** — GET<br/>

Use DRF web interface to see available fields.

# Manual install
```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata core/fixtures/auth_groups.json 
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000

# to add demo users
python3 manage.py loaddata core/fixtures/sample_users.json 
```

# Structure example

```
[
    {
        "id": 1,
        "username": "vitaly",
        "subordinates": []
    },
    {
        "id": 3,
        "username": "hr_user",
        "subordinates": []
    },
    {
        "id": 4,
        "username": "user_1",
        "subordinates": [
            {
                "id": 5,
                "username": "user_2",
                "subordinates": []
            },
            {
                "id": 6,
                "username": "user_3",
                "subordinates": [
                    {
                        "id": 7,
                        "username": "user_4",
                        "subordinates": [
                            {
                                "id": 8,
                                "username": "user_5",
                                "subordinates": []
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```