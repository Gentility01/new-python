# Convert a temperature from Celsius to Fahrenheit

# formular  = (C x 1.8) + 32 

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print("Temperature in Fahrenheit:", fahrenheit_temperature)
