import json
import requests


#! Leer 'precios.txt' para conseguir datos
archivo = open("precios.txt", "r", encoding='utf-8')
items = []
precios = []
for linea in archivo:
    lineasSeparadas = linea.rstrip().split(':')
    items.append(lineasSeparadas[0])
    precios.append(float(lineasSeparadas[1]))


#! Conseguir respuesta de la api de cambio de moneda
def api(cambio, moneda='USD'):
    link = f'https://free.currconv.com/api/v7/convert?q={moneda}_{cambio},{cambio}_{moneda}&compact=ultra&apiKey=5fa6f376598dd9f55488'
    response = requests.get(link)
    data = json.loads(response.text)
    return int(data[f'{moneda}_{cambio}'])


#! Funcion a exportar
def costoDeVida(cambio):
    lista = []
    detalle = api(cambio)
    for index in range(len(items)):
        # item => precio
        lista.append(
            (f'{items[index]} => {round(precios[index] * detalle,2)} {cambio}\n'))
    return lista
