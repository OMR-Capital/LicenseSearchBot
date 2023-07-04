from models import Item

GREETING = 'Привет! Я помогу тебе найти информацию о лицензии. Введи номер или название отхода, чтобы получить информацию.'

FIRST_SEARCH_MESSAGE = 'Нажмите, чтобы начать поиск.'
ASK_QUERY = 'Введите номер отхода или часть наименования:'
WAIT_SEARCH = 'Подождите, идет поиск...'
ITEMS_NOT_FOUND = 'Не найдены подходящие отходы.'
SEARCH_FINISHED = 'Поиск завершен.'


def get_item_form(item: Item) -> str:
    works = ', '.join(item.allowed_works)

    text = f'''
<b>Наименование:</b> <code>{item.name}</code>
<b>Код по ФККО:</b> <code>{item.code}</code>
<b>Класс опасности отхода:</b> <code>{item.hazard}</code>
<b>Виды работ:</b> <code>{works}</code>
'''
    if item.address:
        text += f'<b>Адреса:</b> <code>{item.address}</code>\n'

    text += f'<b>Организация:</b> <code>{item.company}</code>\n'
    return text


def get_items_form(items: list[Item]) -> str:
    return '\n'.join(get_item_form(item) for item in items)