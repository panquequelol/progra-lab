# Laboratorio de Programación
Programa en Python sobre economía en Chile para Fundamentos de Computación y Programación

# APIs externas
Las apis que se usan son las siguientes:

https://mindicador.cl/ para los indices de economía

https://api-sismologia-chile.herokuapp.com/ para los últimos 15 sismos

https://free.currencyconverterapi.com/ para hacer conversión de divisas

# Manual de instalación de la aplicación:
No es necesario descargar ninguna dependicia extra para correr el código, pero asegúrese de tener descargado [Python](https://www.python.org/downloads/).

Las únicas funcionalidades extra se consiguen importando *json* y *requests*, pero estas ya se encuentran incluidas en el archivo y *OS* para escribir texto de color en la terminal.

1. Aprete el botón verde del repositorio que dice *Code*
2. Descarge el código haciendo click en *Download ZIP*
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
5. !Listo! se generó el archivo, podrá ver algo así en el archivo generado *(Ejemplo usando "CLP" como código ISO 4217)*
![3-ejemplo-plataforma-CLP](https://github.com/caceresrene/progra-lab/blob/main/screenshots/3-ejemplo-plataforma-CLP.png?raw=true)

**NOTA:** Si desea actualizar los precios mostrados puede hacerlo desde ```precios.txt``` escribiendo los nuevos valores a la izquierda del ítem despues de los ":"
