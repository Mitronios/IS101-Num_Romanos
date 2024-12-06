#Iniciaremos creando funciones que nos ayuden a generar números romanos siguiendo las reglas.

#Creamos nuestros números con valores de "quiebre"

numeros_romanos = { 
    #Siguiendo la regla de mayor a menor.
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

#Ahora creamos un conversor que me toma un número entero y me devuelve romano(str)
def convierte_a_romanos(valor: int) -> str:
    """
    Conversor que recibe un número entero y me devuelve su valor
    equivalente convertido a número romano
    """
    #Inicio el valor
    romano = ""

    #Itero por el diccionario
    for key, value in numeros_romanos.items():
        #Mientras el valor sea mayor o igual a algún valor de value 
        while valor >= value:
            #Guardo la clave que corresponde en romano
            romano = romano + key
            #Resto el valor restante para conocer el siguiente valor
            valor -= value # 58 cabe una vez en L, 58 - 50 sobran 8, 5 cabe  en V quedan 3 y esos 3 caben en III

    #Devuelvo el romano
    return romano



assert convierte_a_romanos(1) == 'I', "Conversión incorrecta"
assert convierte_a_romanos(500) == 'D', "Conversión incorrecta"

assert convierte_a_romanos(2) == 'II', "conversión incorrecta"
assert convierte_a_romanos(200) == 'CC', "Conversión incorrecta"