from models import Item

GREETING = 'Привет! Я помогу тебе найти информацию о лицензии. Введи номер или название отхода, чтобы получить информацию.'

FIRST_SEARCH_MESSAGE = 'Нажмите, чтобы начать поиск.'
ASK_QUERY = 'Введите номер отхода или часть наименования:'
WAIT_SEARCH = 'Подождите, идет поиск...'
ITEMS_NOT_FOUND = 'Не найдены подходящие отходы.'
SEARCH_FINISHED = 'Поиск завершен.'


def get_item_form(item: Item) -> str:
    works_str = ', '.join(item.allowed_works)
    return f'''
<b>Номер:</b> <code>{item.key}</code>
<b>Наименование:</b> <code>{item.name}</code>
<b>Код по ФККО:</b> <code>{item.code}</code>
<b>Класс опасности отхода:</b> <code>{item.hazard}</code>
<b>Виды работ:</b> <code>{works_str}</code>
<b>Адреса:</b> <code>{item.address}</code>
'''


def get_items_form(items: list[Item]) -> str:
    return '\n'.join(get_item_form(item) for item in items)