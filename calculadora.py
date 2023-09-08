def suma(x: float, y: float) -> float:
    """Suma dos números."""
    return x + y

def resta(x: float, y: float) -> float:
    """Resta dos números."""
    return x - y

def multiplicacion(x: float, y: float) -> float:
    """Multiplica dos números."""
    return x * y

def division(x: float, y: float) -> float:
    """Divide dos números. Retorna un mensaje de error si el divisor es cero."""
    if y == 0:
        return "Error: División por cero"
    return x / y

def calculadora():
    """Interfaz para usar la calculadora."""
    while True:
        print("\nOpciones:")
        print("Ingresa 'suma' para sumar")
        print("Ingresa 'resta' para restar")
        print("Ingresa 'multiplicacion' para multiplicar")
        print("Ingresa 'division' para dividir")
        print("Ingresa 'salir' para finalizar el programa")
        user_input = input(": ")

        if user_input == "salir":
            break

        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))

        match user_input:
            case "suma":
                result = suma(x, y)
            case "resta":
                result = resta(x, y)
            case "multiplicacion":
                result = multiplicacion(x, y)
            case "division":
                result = division(x, y)
            case _:
                "Operación no válida"
        
        print(result)

if __name__ == "__main__":
    calculadora()
