from models import Item

GREETING = 'Привет! Я помогу тебе найти информацию о лицензии. Введи номер или название отхода, чтобы получить информацию.'

WAIT_SEARCH = 'Подождите, идет поиск...'
ITEMS_NOT_FOUND = 'Не найдены подходящие отходы.'


def get_item_form(item: Item) -> str:
    works_str = ', '.join(item.allowed_works)
    return f'''
<b>Номер:</b> {item.key}
<b>Наименование:</b> {item.name}
<b>Код по ФККО:</b> {item.code}
<b>Класс опасности отхода:</b> {item.hazard}
<b>Виды работ:</b> {works_str}
<b>Адреса:</b> {item.address}
'''

