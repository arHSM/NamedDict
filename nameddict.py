__all__ = ("NamedDict", "NamedDictMeta")

from typing import (
    Annotated,
    Any,
    Dict,
    NamedTuple,
    Optional,
    Union,
    get_origin
)


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
    __slots__ = {}
    __mapping__: Dict[str, Any]

    def __init__(self, **kwargs):
        try:
            for name, default in self.__mapping__.items():
                value = kwargs.get(name, default)
                self.__setattr__(name, value)
        except AttributeError:
            super().__init__(**kwargs)

    def __getattribute__(self, __name: str) -> Any:
        try:
            return super().__getattribute__(__name)
        except AttributeError:
            try:
                if __name in self.__mapping__:
                    return super().__getitem__(__name)
                else:
                    raise AttributeError(
                        f"{self.__class__.__name__} has no attribute {__name}."
                    )
            except AttributeError:
                return super().__getitem__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        try:
            if __name in self.__mapping__:
                return super().__setitem__(__name, __value)
            else:
                raise AttributeError(
                    f"{self.__class__.__name__} has no attribute {__name}."
                )
        except AttributeError:
            return super().__setitem__(__name, __value)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__} {super().__repr__()}"


class NamedDictMeta(type):
    
    def __new__(cls, name: str, bases: tuple, namespace: dict) -> NamedDict:

        namespace["__slots__"] = set()
        namespace["__mapping__"] = {}

        try:
            temp_ns = namespace["__annotations__"].copy()
        except KeyError:
            return type.__new__(cls, name, bases, namespace)

        for attribute in temp_ns:
            default = None
            if attribute in namespace:
                default = namespace.pop(attribute)
            
            namespace["__mapping__"][attribute] = default

        nd_dict = type.__new__(NamedDictMeta, name, bases, namespace)

        return nd_dict
