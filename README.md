# Проект YaCut
## Описание
Проект YaCut — это сервис укорачивания ссылок. 
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой,
которую предлагает сам пользователь или предоставляет сервис.

### Использованные технологии
* Python
* Flask
* SQLAlchemy

### Установка и использование
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:IlDezmond/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запустить сервис:
```
flask run
```
Открыть веб интерфейс:
```
http://127.0.0.1:5000
```

### Примеры запросов api
Получить оригинальную ссылку
```
GET http://127.0.0.1:5000/api/{short_id}/
```
Создать новую короткую ссылку
```
POST http://127.0.0.1:5000/api/id/
Content-Type: application/json

{
  "url": "original_url"
}
```