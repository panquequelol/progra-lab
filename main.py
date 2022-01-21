from indicadores import indicadores  # ! modulos, importar funciones principales
from costoDeVida import costoDeVida
from sismos import sismosInformacion
import os
os.system('color')  # ! Importar colores para la terminal
print('\n\033[96m' + "Cargando" + '\033[m' + "...\n")


# ! Interfaz
print('##########################' +
      '\n \033[34m \033[21m Plataforma Chile \033[m \033[m' +
      '\n##########################' +
      '\nEste programa es capaz de consultar...' +
      '\n\033[96m Datos Diarios \033[m ' +
      '\n\033[96m Costo de Vida \033[m ' +
      '\n\033[96m Ultimos sismos \033[m ' +
      '\nY crea un archivo de texto \033[96m"plataforma.txt"\033[m con la informacion.\n')

codigoISO = input(
    '\033[34m¿En que moneda desea consultar el costos de vida en Chile?\033[m codigos ISO 4217 ej: CLP... ')

print('\n\033[96m' + "Cargando" + '\033[m' + "... \n")


def titulo(nombre):
    return ['##########################\n' +
            f'{nombre}'
            '\n##########################\n'
            ]


# ! Codigo Principal
if len(codigoISO) == 3:
    codigoISO = codigoISO.upper()  # por seguridad

    # ! Crear archivo de salida
    salida = open('plataforma.txt', 'w', encoding='utf-8')
    salida.writelines(titulo('Costo de vida en Chile'))
    salida.writelines(costoDeVida(codigoISO))
    salida.writelines('\n')
    salida.writelines(titulo('Indicadores economicos'))
    salida.writelines(indicadores())
    salida.writelines('\n')
    salida.writelines(titulo('Ultimos sismos en Chile'))
    salida.writelines(sismosInformacion())
    salida.close()

    print('¡Archivo generado con exito!')
else:
    print('Ingrese un codigo valido...\nEjecute el programa de nuevo.')
