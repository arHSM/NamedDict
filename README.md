# `NamedDict`s aka `NamedTuple`s but dictionaries

## How does it work?

\- No magic involved here, `nameddict.NamedDict` is a subclass of dict.
only the `__getattribute__` and `__setattr__`have been replaced, and thats
where the *magic* happens.

## How to create a `NamedDict`?

Well its as imple as this -

```pycon
>>> import namedtuple.NamedDict as NamedDict
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
