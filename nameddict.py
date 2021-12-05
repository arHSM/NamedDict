__all__ = ("NamedDict",)

from typing import Any


class NamedDict(dict):
    """
    `NamedDict` is a subclass of `dict`, but it replaces 
    `__getattribute__` and `__setattr__`.

    Methods -
    - `__getattrinute__` tries to call `__getattribute__` and then calls 
    `__getitem__` on AttributeError. You may want to use the normal way 
    of `instance["items"]` because calling `instance.items` will return 
    the `items` method which is not what you want, hence be careful of 
    what keys you want to access and how you access them.
    - `__setattr__` same as `instance["key"] = "value"` but
    better, i.e `instance.key = "value"`.

    ```pycon
    >>> class Data(NamedDict):
    ...     __slots__ = ()  # you need to add this line to avoid the 
    ...                     # creation of `__dict__`
    ...     value_a: int
    ...     value_b: str
    ...
    >>> data = Data(value_a=1, value_b="hi!")
    >>> print(data)
    {"value_a": 1, "value_b": "hi!"}
    >>> data.value_a
    1
    >>> data.value_b
    "hi!"
    ```
    """
    __slots__ = ()

    def __getattribute__(self, __name: str) -> Any:
        try:
            return super().__getattribute__(__name)
        except AttributeError:
            return super().__getitem__(__name)

    __setattr__ = dict.__setitem__
