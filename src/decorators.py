from functools import wraps
from typing import Optional, Callable, Any


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для фиксации запуска и выполнении функции без времени выполнения"""

    def decorator(func: Any) -> Callable:
        @wraps(func)
        def wrappers(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as f:
                        f.write(
                            f"Function {func.__name__} status: Ok\n"
                            f"Result: {result}\n"
                        )
                else:
                    print(
                        f"Function {func.__name__} status: Ok\n"
                        f"Result: {result}\n"
                    )
            except Exception as e:
                print(f"Function {func.__name__} error: {type(e).__name__}: {e} (args={args}, kwargs={kwargs})\n")
                raise
            return result

        return wrappers

    return decorator