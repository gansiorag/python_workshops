from pydantic import RootModel, ValidationError, Field
from typing import Annotated, Literal

s_list = ['sss', 'ssdf', 'dfvbg']

# Ограничиваем выбор только конкретными строками
Mode = Literal['sss', 'ssdf', 'dfvbg']

# Добавляем метаданные (например, для БД или валидатора)
ID = Annotated[int, "must_be_positive", "primary_key"]

def set_permission(user_id: int, access: Mode):
    # Пытаемся провалидировать входные данные через Pydantic
    try:
        # В новых версиях Pydantic можно использовать TypeAdapter или RootModel
        from pydantic import TypeAdapter
        TypeAdapter(Mode).validate_python(access)
        print(f"User {user_id} now has {access} access")
    except ValidationError:
        print(f"ОШИБКА: '{access}' — это недопустимый режим!")


set_permission(10, "ssdf") # OK
set_permission(10, "ssdee") # ОШИБКА:
