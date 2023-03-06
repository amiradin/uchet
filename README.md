# Документация по тестовому заданию
<hr>

## Стек:
> Python==3.10
>
> FastAPI==0.92.0

## Руководство:

* Клонировать репозиторий
```sh
git clone https://github.com/amiradin/uchet_test.git 
```

* Открыть папку проекта в редакторе


* Создать и активировать виртуальное окружение:
```sh
python -m venv venv
.\venv\Scripts\activate
``` 

* Установить зависимости
```sh
pip install -r requirements.txt
```

* Перейти в директорию **backend**
```sh
cd .\backend\
```

* Запустить команду:
```sh
python main.py
```

* Открыть браузер и перейти по следующему адресу:

`http://127.0.0.1:8081/upload_files`

* На странице выбрать файл для отправки (можете несколько, зажав на клавишу `Ctrl`) и отправить, кликнув на кнопку `Send!`

![image](/doc/page.jpg "Upload files page")

* Чекнуть логи в терминале для проверки созданных потоков

<hr>

## Через swagger:

* Открыть браузер и перейти по следующему адресу:

`http://127.0.0.1:8081/docs`

![image](/doc/swagger.jpg "Upload files page")

* Раскрыть метод `POST`, выбрать файл(-ы) затем кликнуть на `Execute`:

![image](/doc/swagger_post.jpg "Upload files page")

* Чекнуть логи в терминале для проверки созданных потоков