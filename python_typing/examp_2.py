from typing import Annotated, Literal

s_list = ['sss', 'ssdf', 'dfvbg']

# Ограничиваем выбор только конкретными строками
Mode = Literal['sss', 'ssdf', 'dfvbg']

# Добавляем метаданные (например, для БД или валидатора)
ID = Annotated[int, "must_be_positive", "primary_key"]

def set_permission(user_id: ID, access: Mode):
    print(f"User {user_id} now has {access} access")

set_permission(10, "ssdf") # OK
set_permission(10, "ssdee") # OK
