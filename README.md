# FlaskMicroservice

Система ищет выбранную пользователем электронику с помощью веб скрепинга. Полученную информацию можно фильтровать по цене и рейтингу. 

# Requirements
```
flask~=1.1
grpcio-tools~=1.30
Jinja2~=2.11
pytest~=5.4
MarkupSafe~=2.0.1
flask-wtf~=1.0.1
requests~=2.28.1
beautifulsoup4~=4.11.1

```
# Как запустить
_Версия питона - Python 3.8.3_
1. Установить виртуальное окружение командой `virtualenv имя окружения`
2. Запустить виртуальное окружение командой`source имя окружения/bin/activate`(выключение командой `deactivate`)
3. Установить библиотеки `python -m pip install -r requirements.txt`
4. Сгенерировать код Python из файлов proto `python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/имя_файла.proto` в каждую папку
5. (запуск в отдельной командной строке) Запустить виртуальное окружение командой`source имя окружения/bin/activate` и запустить файл скрепинга командой `python pleer_scraper.py`
6. (запуск в отдельной командной строке) Повторить пункт 5 и запустить файл скрепинга командой `python ya_scraper.py`
7. (запуск в отдельной командной строке) Повторить пункт 5 и запустить файл сервера командой `python server.py`
  
