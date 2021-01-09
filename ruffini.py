def equation_to_string(coefficients: list, grade: int) -> str:
    # Rappresenta l'equazione.
    equation: str = ""
    for index in range(grade, -1, -1):
        if not(coefficients[index] == 0):
            if not(index < 2):
                equation += (signed_int(coefficients[index]) + "x^" + str(index) + " ")
            else:
                if index == 1:
                    equation += (signed_int(coefficients[index]) + "x ")
                else:
                    equation += signed_int(coefficients[index])
    
    if equation == "":
        equation = "0"
    
    return equation

def ruffini(coefficients: list, test: int) -> (bool, list, int):
    coefficients.reverse()

    results: list = []
    for index in range(len(coefficients)):
        if index == 0:
            results.append(coefficients[index])
        else:
            results.append(test * results[index - 1] + coefficients[index])

    successful: bool = results[-1] == 0

    return (successful, results, test)


def signed_int(integer: int, force: bool = False) -> str:
    result: str = ""

    if integer >= 0:
        if integer == 1 and not(force):
            return "+"
        result += "+"

    result += str(integer)

    return result

def main():
    grade: int = int(input("Inserisci il grado dell'equazione: "))
    
    # Ottiene i dati dei coefficienti.
    coefficients: list = []
    for index in range(grade, -1, -1):
        coefficients.append(int(input("Inserisci il coefficiente di x^" + str(index) + ": ")))
    coefficients.reverse()

    print("L'equazione è:", equation_to_string(coefficients, grade))

    # Calcola Ruffini.
    value: int = 0
    new_coefficients: list
    test: int = 1
    while value == 0 and test < 100:
        print("Provo a verificare con ±", str(test))

        if not(ruffini(coefficients, test)[0]):
            if not(ruffini(coefficients, -test)[0]):
                test += 1
            else:
                new_coefficients = ruffini(coefficients, -test)[1]
                value = -test
                break
        else:
            new_coefficients = ruffini(coefficients, test)[1]
            value = test
            break
    
    if value != 0:
        print("Il risultato è: ", "(x", signed_int(-value, force=True), ")(", equation_to_string(new_coefficients, grade - 1), ")", sep = "")
    else:
        print("Non puoi scomporre con Ruffini questa equazione")

main()