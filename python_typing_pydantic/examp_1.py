import time
import functools
from typing import Callable, TypeVar, ParamSpec

# 1. Задаем переменные для типов
P = ParamSpec("P")    # Для параметров (аргументов)
R = TypeVar("R")      # Для возвращаемого результата (Return)

def timer(func: Callable[P, R]) -> Callable[P, R]:
    """Декоратор, который печатает время выполнения функции."""
    
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(func.__name__)
        start_time = time.perf_counter()
        
        # Выполняем саму функцию
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        print(f"--- Функция '{func.__name__}' выполнилась за {end_time - start_time:.4f} сек. ---")
        
        return result
        
    return wrapper

# --- Применяем декоратор ---

@timer
def heavy_computation(x: int, name: str = "Robot") -> str:
    """Имитируем сложную работу."""
    time.sleep(1.5)
    return f"Результат для {name}: {x * 2}"

# Теперь проверь в своем редакторе:
# Наведи курсор на 'res' — он покажет тип 'str' (благодаря TypeVar R).
# Начни писать 'heavy_computation(' — он подскажет 'x' и 'name' (благодаря ParamSpec P).
res = heavy_computation(42, name="Alpha")
print(res)