# `NamedDict`s aka `NamedTuple`s but dictionaries

## How does it work?

\- No magic involved here, `nameddict.NamedDict` is a just subclass of dict,
only the `__getattribute__` and `__setattr__` have been replaced, and thats
where the *magic* happens.

## How to create a `NamedDict`?

Well its as simple as this -

```pycon
>>> import nameddict.NamedDict as NamedDict
>>>
>>>
>>> class Data(NamedDict):
...     __slots__ = ()  # you need this line to avoid the creation of 
...                     # `__dict__`
...     value_a: int
...     value_b: str
...
>>> # initialise it just like you would do with `dict()`
>>> data = Data(value_a=1, value_b="hi!")
>>> print(data)
Data {"value_a": 1, "value_b": "hi!"}
>>> print(data.value_a)
1
>>> print(data.value_b)
"hi!"
```

Points to note:

1. Attributes that conflict with the methods in `dict` object such as `items`, `keys`, `values`, etc... cannot be accessed by `instance.items` instead you need to do `instance["items"]`.

2. You need to add `__slots__ = ()` to prevent the creation of `__dict__` (Which you don't need and want, *trust me*).

> **NOTE**: These type hints mean nothing!

## Extending `NamedDict`s

With the new `NamedDictMeta` you can extend your NamedDicts.

```pycon
>>> form nameddict import NamedDict, NamedDictMeta
>>>
>>>
>>> class Data(NamedDict, metaclass=NamedDictMeta):
...     val_1: str
...     val_2 = 5
...     val_3: bool = False
...
>>> data = Data()
>>> data
Data {"val_1": None, "val_3": False}
>>> data.val_2 = 5
# Simplified error
AttributeError: Data has no attribute val_2.
>>> data.val_3
True
>>> data.val_2
# Simplified error
KeyError: 'val_2'
```

Points to note:

1. Type hints still don't mean anything, you can always pass in a different type of object.

2. Attribute without an annotation will be ignored if there are attributes with annotations present (look into the implementation for better understanding).

3. Default values is `None` unless explicitly set.

4. You do not need to add the `__slots__` line, because the metaclass handles that.

Why use `(NamedDict, metaclass=NamedDictMeta)`, instead of handling it in the meta class?

- Long story short, it's mainly for type-checkers to stop being annoying.

## How to install?

Well simply download the [`nameddict.py`](https://raw.githubusercontent.com/arHSM/NamedDict/master/nameddict.py) file and put it in your project folder, then import it like just any other file!
