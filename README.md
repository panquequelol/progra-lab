# Laboratorio de Programacion
Programa en Python sobre economia en Chile para Fundamentos de Computación y Programación

# APIs externas
Las apis que se usan son las siguientes:

https://mindicador.cl/ para los indices de economia

https://api-sismologia-chile.herokuapp.com/ para los ultimos 15 sismos

https://free.currencyconverterapi.com/ para hacer conversion de divisas

# Manual de instalación de la aplicación:
No es necesario descargar ninguna dependicia extra para correr el codigo, pero asegurese de tener descargado [Python](https://www.python.org/downloads/).

Las unicas funcionalidades extra se consiguen importando *json* y *requests*, pero estas ya se encuentran incluidas en el archivo y *OS* para escribir texto de color en la terminal.

1. Aprete el boton verde del repositorio que dice *Code*
2. Descarge el codigo haciendo click en *Download ZIP*
3. Descomprima el archivo haciendo click *derecho > descomprimir*

# Manual de uso de la aplicación:
1. Desde la carpeta descomprimida ejecute ```main.py```
2. Se va encontrar con una terminal con la siguente interfaz:
![1-interfaz](https://github.com/caceresrene/progra-lab/blob/main/screenshots/1-interfaz.png?raw=true)
3. Ingrese en formato [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) la moneda en la cual desea consultar los costos de vida en Chile, en su teclado aprete la tecla *enter* o *intro*
4. Espere a que se genere el archivo de texto ```plataforma.txt```, cuando se haya generado deberia ver el siguente mensaje en la terminal:
```
¡Archivo generado con éxito!
```
5. !Listo! se genero el archivo, podra ver algo asi en el archivo generado *(Ejemplo usando "CLP" como codigo ISO 4217)*
![3-ejemplo-plataforma-CLP](https://github.com/caceresrene/progra-lab/blob/main/screenshots/3-ejemplo-plataforma-CLP.png?raw=true)

**NOTA:** Si desea actualizar los precios mostrados puede hacerlo desde ```precios.txt``` escribiendo los nuevos valores a la izquierda del item despues de los ":"
