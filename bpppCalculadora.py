import math

def validar_positivo(valor):
    """
    Verifica que el valor sea un número positivo.

    Args:
        valor (str or float): El valor a verificar.

    Returns:
        bool: True si el valor es un número positivo, False de lo contrario.

    Raises:
        ValueError: Si el valor no es un dato numérico.
    """
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        raise ValueError("el valor debe ser un dato numérico.")

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (str or float): El radio del círculo.

    Returns:
        float: El área del círculo.

    Raises:
        ValueError: Si el radio no es un número positivo.
    """
    if not validar_positivo(radio):
        raise ValueError("el radio debe ser un número positivo.")
    radio = float(radio)
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    Args:
        base (str or float): La base del triángulo.
        altura (str or float): La altura del triángulo.

    Returns:
        float: El área del triángulo.

    Raises:
        ValueError: Si la base o la altura no son números positivos.
    """
    if not (validar_positivo(base) and validar_positivo(altura)):
        raise ValueError("la base y la altura deben ser números positivos.")
    base = float(base)
    altura = float(altura)
    return (base * altura) / 2

def area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el tamaño de su lado.

    Args:
        lado (str or float): El lado del cuadrado.

    Returns:
        float: El área del cuadrado.

    Raises:
        ValueError: Si el lado no es un número positivo.
    """
    if not validar_positivo(lado):
        raise ValueError("el lado debe ser un número positivo.")
    lado = float(lado)
    return lado ** 2

def volumen_cubo(lado):
    """
    Calcula el volumen de un cubo dado el tamaño de su lado.

    Args:
        lado (str or float): El lado del cubo.

    Returns:
        float: El volumen del cubo.

    Raises:
        ValueError: Si el lado no es un número positivo.
    """
    if not validar_positivo(lado):
        raise ValueError("el lado debe ser un número positivo.")
    lado = float(lado)
    return lado ** 3

def menu():
    """
    Muestra el menú de opciones de la calculadora y maneja la selección del usuario.
    """
    opciones = {
        "1": ("Área del círculo", area_circulo, ["radio"]),
        "2": ("Área del triángulo", area_triangulo, ["base", "altura"]),
        "3": ("Área del cuadrado", area_cuadrado, ["lado"]),
        "4": ("Volumen del cubo", volumen_cubo, ["lado"])
    }

    while True:
        print("**** Calculadora ****")
        for key, (desc, _, _) in opciones.items():
            print(f"{key}) {desc}")
        print("0) SALIR")

        entrada_operacion = input("Por favor, elige una opción: ")

        if entrada_operacion == "0":
            print("Calculadora cerrada.")
            break
        elif entrada_operacion in opciones:
            desc, func, params = opciones[entrada_operacion]
            try:
                print(f"\n{entrada_operacion}) {desc}")
                valores = [input(f"Introduzca valor de {param}: ") for param in params]
                resultado = func(*valores)
                print(f"El resultado de {desc} es {resultado}\n")
            except ValueError as e:
                print(f"Error, {e}\n")
        else:
            print("Opción inválida, por favor seleccione correctamente la operación a realizar.\n")

if __name__ == "__main__":
    menu()
