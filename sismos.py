import json
import requests

# ! Conseguir ultimos 15 sismos desde API


def api(url="https://api-sismologia-chile.herokuapp.com/"):
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    pretty_json = json.dumps(data, indent=2)
    return data

# ! Funcion a exportar


def sismosInformacion(data=api()):
    lista = []
    for sismo in (data):
        # Existe un dato que corresponde a 'sismologia.cl' entre los sismos de la api
        if sismo['mapa'] != 'http://sismologia.cl':
            lista.append(
                # Magnitud: magnitud a lugar en fecha
                f'Magnitud: {sismo["magnitud"]} a {sismo["referencia"]} el {sismo["horaLocal"][9:]} \n Imagen de referencia: {sismo["mapa"]}\n')
    return lista
