>>> class MyMetaClass(type):
...     @property
...     def my_data(cls):
...         if getattr(cls, '_MY_DATA', None) is None:
...             print("costly database call executing")
...             my_data = 'bar'
...             cls._MY_DATA = my_data
...         return cls._MY_DATA
... 
>>> class MyClass(metaclass=MyMetaClass):
...     pass
... 
>>> MyClass.my_data
costly database call executing
'bar'
>>> MyClass.my_data
'bar'
