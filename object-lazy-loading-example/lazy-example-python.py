>>> class PrinterService(type):
...     @property
...     def available_printers(cls):
...         if getattr(cls, '_AVAILABLE_PRINTERS', None) is None:
...             print("costly check of printer availability with I/O processes")
...             available_printers = 'bar'
...             cls._AVAILABLE_PRINTERS = available_printers
...         return cls._AVAILABLE_PRINTERS
... 
>>> class PrinterService(metaclass=PrinterService):
...     pass
... 
>>> MyClass.available_printers
costly database call executing
'bar'
>>> MyClass.available_printers
'bar'
