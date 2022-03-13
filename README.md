#### Iniciar migraciones

```sh
$ > alembic init migrations
$ > alembic revision --autogenerate -m "Initial migration"
```

#### Correr la ultima migracion

```sh
$ > alembic upgrade head
```

#### Correr el servidor
```sh
$ > uvicorn main:app --reload
```