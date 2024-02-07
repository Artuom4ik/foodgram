# Foodgram
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

___

#### Вашему вниманию представляется иерфрхическая структура товаров. Программа имеет модели базы данных такие как: 
* `Product` - модель продукта
* `Section` - секции продукта
* `Group` - группа продукта
* `Subgroup` - поддгруппа продкта
* `Card` - карточка на котрую ссыдается продукт

##### База данных имеет 4 уровня вложенности `section-group-subgroup-card` 
___
### Содержание:
* [Запуск](https://github.com/Artuom4ik/foodgram?tab=readme-ov-file#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
* [Переменные окружения](https://github.com/Artuom4ik/foodgram?tab=readme-ov-file#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
* [Как добавить данные](https://github.com/Artuom4ik/foodgram?tab=readme-ov-file#%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5)
* [Эндпоинты и их функции](https://github.com/Artuom4ik/foodgram?tab=readme-ov-file#%D1%8D%D0%BD%D0%B4%D0%BF%D0%BE%D0%B8%D0%BD%D1%82%D1%8B-%D0%B8-%D0%B8%D1%85-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)
* [Цель проекта](https://github.com/Artuom4ik/foodgram?tab=readme-ov-file#%D1%86%D0%B5%D0%BB%D1%8C-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
___
### Запуск

Для запуска у вас уже должен быть установлен Python 3.9 или выше.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сервер командой `python3 manage.py runserver`
___
### Переменные окружения:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по умолчанию.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
___
### Как добавить данные

Можно использовать два способа, для добавления данных в `БД` - это через админку и напрямую через кансоль.

##### Добавление через админ панель

Для того чтобы добавить данные через админку, потребуется для начала добавить `секцию`, затем `группу`, `подруппу`, `карточку`, после же добавляем сам `продукт`.

* При добавлении записи о группе, подгруппе и тд. требуется указать к какому предыдущему объекту будет привязка.

##### Добавление через консоль

В `Django` существует встренная команда для добавления данных в базу. Достаточно написать в консоль команду:
```
python manage.py loaddata fixture_name
```
* Прежде чем писать данную команду, требуется создать файл `json` в котором буду написаны данные.

* Пример файла `json`:
![](picture/code.png)

* Подробнее о [loaddata](https://www.pythontutorial.net/django-tutorial/django-loaddata/)

___
### Эндпоинты и их функции
В файле `urls.py` папки `foodgram` имеется такой роут:

* `categories/` - данный роут имеет такие эндпоинты:

В файле `urls.py` папки `categories`:

* `''` - данный эндпоинт отвечает за получения списка котегорий. Вот как выгледет [функция](https://github.com/Artuom4ik/foodgram/blob/0a8b00fba0a82b106b8245f2dd6cc93d28e512b8/categories/views.py#L7-L17)

* `cards_list/section/<int:section_id>/group/<int:group_id>/subgroup/<int:subgroup_id>/` - данный эндпоинт отвечает за получение списка карточек определенной секции, группы, подгруппы. Нужно передать `id` секции, группы и подгруппы вместо `<int:section_id>`, `<int:group_id>`, `<int:subgroup_id>`. Вот как выгледет [функция](https://github.com/Artuom4ik/foodgram/blob/0a8b00fba0a82b106b8245f2dd6cc93d28e512b8/categories/views.py#L20-L36).

* `detail_information_card/<int:card_id>/` - данный эндпоинт отвечает за получение детальной информации о карточке товара. Нужно передать `id` карточки вместо `<int:card_id>`. Вот как выгледет [функция](https://github.com/Artuom4ik/foodgram/blob/0a8b00fba0a82b106b8245f2dd6cc93d28e512b8/categories/views.py#L39-L70).

* `products_list/<int:card_id>/` - даннный эндпоинт отвечает за получение списка продуктов по определенной карточке. Нужно передать `id` карточки вместо `<int:card_id>`. Вот как выгледет [функция](https://github.com/Artuom4ik/foodgram/blob/0a8b00fba0a82b106b8245f2dd6cc93d28e512b8/categories/views.py#L73-L89).

В результате перехода по этим эндпоинтам вы получаете данные в формате `json`.
___

### Цель проекта:
* Код написан в образовательных целях.
