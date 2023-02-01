# Pool_search_assistant
Сервис API для получения рекомендованных бассейнов.

Ссылка на документацию по API: https://miheev.su/pool/api/v1/docs

В директории docs находится более подробная пояснительная записка к проекту

![](https://img.shields.io/badge/-Python-386e9d?style=flat&logo=Python&logoColor=ffd241) 
![](https://img.shields.io/badge/FastAPI-109989?style=flat&logo=fastapi&logoColor=white) 
![](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat&logo=Postgresql) 
![](https://img.shields.io/badge/redis-%23DD0031.svg?&style=flat&logo=redis&logoColor=white) 
![](https://img.shields.io/badge/-sqlalchemy-4479A7?style=flat&&logoColor=ffffff) 
![](https://img.shields.io/badge/-Docker-46a2f1?style=flat&logo=docker&logoColor=white) 
![](https://img.shields.io/badge/-Nginx-009639?style=flat&logo=nginx)
## Функционал:
- Авторизация пользователей через сессии
- Сохранение информации о понравившихся бассейнах пользователя
- Выдача рекомендованных бассейнов, на основе понравившихся.
- Обновление данных датасета в полу-автоматическом режиме

### Обновление датасета:
Через cli команду, запускается скрипт, который ходит в API с открытыми данными города Москва.
### Выдача рекомендаций:
Рекомендация основана на алоритме нахождения косинусного растояния между двумя векторами
### Сессии пользователей:
При авторизации (перед этим нужно зарегестрироваться) выдается id сессии(uuid), информация о сессии хранится в Redis в виде jwt токена.

## Основные кейсы:
- Регистрация
![](docs/register.png)
- Авторизация
![](docs/authorise.png)
- Получение рекомендаций
![](docs/recomended.png)

## Архитектура:
Монолит (Clean Arhitecture).

### Разделение слоев, и направления зависимостей.
![](docs/clean%20arhitecture.png)

### ER-диаграмма базы данных PostgreSQL в нотации Мартина.

<img src="docs/er%20%D0%B4%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0.png"  width="300">

### Обощенная диаграмма классов.
![](docs/uml.png)
