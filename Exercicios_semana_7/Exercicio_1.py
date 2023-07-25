def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def main():
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)

        print(f"{celsius} graus Celsius equivalem a:")
        print(f"{fahrenheit:.2f} graus Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
    except ValueError:
        print("Digite um valor numérico válido.")

if __name__ == "__main__":
    main()