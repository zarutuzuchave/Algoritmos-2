# 7 - Análise de Turbulência em Voo: Os sensores de um avião registram a altitude a cada
# minuto (lista de números). Uma turbulência severa é caracterizada por uma queda de
# altitude maior que 500 metros em um único minuto.
# Retorno exigido: True ou False se houve turbulência severa, e a maior queda
# registrada em um minuto durante todo o voo.


altitude = [10000,9500,9700,8500,8200,7500 ]

def turbulencia(altitude):
    seTurbulencia = False
    quedaMaior = 0

    for i in range(len(altitude) - 1):
        queda = altitude[i] - altitude[i+1]
        if queda > quedaMaior:
            quedaMaior = queda

        if queda > 500:
            seTurbulencia = True
    return seTurbulencia, quedaMaior

teve_turbulencia, max_queda = turbulencia(altitude)

print(f"Houve turbulência severa? {teve_turbulencia}")
print(f"Maior queda registrada em um minuto: {max_queda} metros")