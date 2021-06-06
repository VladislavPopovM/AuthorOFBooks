# AuthorOFBooks

## Как запустить на локальном компьютере?

#### Загрузите код 
##### Код тестировался на python 3.7.4, Windows 10 
#### Рекомендую создать виртуальное окружение для python или сразу переходи к запуску Docker, но не забудь установить библиотеки!:
```
python3 -m venv venv
```

#### Активанция окружения Python/Django:

Если создавалось вирт.окружение
```
source ./venv/bin/activate 
```
```
pip install -m ./r.txt
```
#### Запустите Docker для БД 
Перейдите в папку database и там введите следующие команды:
```
docker build -t test-psql .
```
```
docker run -p 5405:5432 test-psql
```
#### Почти всё :)
Перейдите в папку app и введите следующие команды:
```
python  main.py init
```
```
python  main.py start
```

Активные ссылки: 
http://127.0.0.1:8000/
http://127.0.0.1:8000/writers/{writer_id}/
http://127.0.0.1:8000/writers_non_json/{writer_id}/

#### Пользуйтесь <3
