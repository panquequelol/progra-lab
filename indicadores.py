import json
import requests


# ! API
# fecha especifica: https://mindicador.cl/api/{tipo_indicador}/{dd-mm-yyyy}
# ultimos: https://mindicador.cl/api
def api(url="https://mindicador.cl/api"):
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    pretty_json = json.dumps(data, indent=2)
    return data
# devuelve codigo, nombre, unidad_medida, fecha, valor


# ! VARIABLES
yearNow = int(api()['fecha'][0:4])
year10ago = yearNow - 5


# ! Datos extraidos de API
def antes(indicador):  # hace 5 años
    consulta = api(f'https://mindicador.cl/api/{indicador}/{year10ago}')
    nombre = consulta['nombre']
    unidad = consulta['unidad_medida']
    valor = consulta['serie'][0]['valor']
    fecha = consulta['serie'][0]['fecha'][0:10]  # año/mes/dia
    return f'{nombre}: {valor} {unidad} ({fecha})'


def ahora(indicador):  # hoy
    consulta = api()[indicador]
    nombre = consulta['nombre']
    unidad = consulta['unidad_medida']
    valor = consulta['valor']
    fecha = consulta['fecha'][0:10]  # año/mes/dia
    return f'{nombre}: {valor} {unidad} ({fecha})'


fechaEspecifica = api(f'https://mindicador.cl/api/dolar/{year10ago}')
fechaAhora = api()['fecha'][0:10]
fechaAntes = fechaEspecifica['serie'][0]['fecha'][0:10]

#! Funcion a exportar


def indicadores():
    return ['Ultimos datos registrados:\n' +
            f'{ ahora("dolar") }\n' +
            f'{ ahora("euro") }\n' +
            f'{ ahora("bitcoin") }\n' +
            f'{ ahora("uf") }\n' +
            f'{ ahora("libra_cobre") }\n' +
            f'{ ahora("tasa_desempleo") }\n' +
            '\nHace 5 años:\n' +
            f'{ antes("dolar") }\n' +
            f'{ antes("euro") }\n' +
            f'{ antes("bitcoin")}\n' +
            f'{ antes("uf") }\n' +
            f'{ antes("libra_cobre") }\n' +
            f'{ antes("tasa_desempleo") }\n'
            ]
