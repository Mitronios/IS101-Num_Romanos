#Iniciaremos creando funciones que nos ayuden a generar números romanos
#Creamos nuestros números
numeros_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 100
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
        #si el valor del dict es = al valor ingresado
        if value == valor:
            #El romano será igual a la clave
            romano = key
    #Devuelvo el romano
    return romano



assert convierte_a_romanos(1) == 'I', "Conversión incorrecta"
assert convierte_a_romanos(500) == 'D', "Conversión incorrecta"

assert convierte_a_romanos(2) == 'II'
assert convierte_a_romanos(200) == 'CC'