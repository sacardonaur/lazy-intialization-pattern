# Lazy Intialization Pattern

## Qué es?
Consiste en posponer la creación de un objeto, el cálculo de un valor o cualquier otro proceso costoso, hasta que sea usado por primera vez.

## Ventajas
* Permite repartir las cargas de procesamiento y memoria de mi aplicación a lo largo de la ejecución, en lugar de acumularlas al inicio
* Startup más rápido.
* Tiempos de respuesta de la aplicación pueden ser mejorados notablemente

## Desventajas
* En aplicaciones multi-thread puede generar problemas graves
* El código se vuelve complicado
* Puede ser costoso de implementar y no generar muchos cambios evidentes de performance

## Conclusión
Solo usar lazy initialization cuando tenemos procesos muy pesados, no por simple atributos de clase o métodos básicos y tengo especificaciones de tiempo a cumplir o recursos limitados.

Buenos candidatos para lazy loading:
* Consultas a BD
* Procesos I/O
* Chequeos de archivos
* Carga pesada en memoria
* Cálculos fuertes (ej: Hasheo)
