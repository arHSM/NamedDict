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
{"value_a": 1, "value_b": "hi!"}
>>> print(data.value_a)
1
>>> print(data.value_b)
"hi!"
```

> NOTE: These type hints currently mean nothing!\
> defining certain keys doesn't mean that you cannot have "anonymous" keys.
> I do have plans on releasing an extention that provides some utilities for
> `NamedDict`s but not now.

## How to install?

Well simply download the [`nameddict.py`](https://raw.githubusercontent.com/arHSM/NamedDict/master/nameddict.py) file and put it in your project folder, then import it like just any other file!
