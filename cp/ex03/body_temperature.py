"""Exercise 3.4: Body Temperature."""

def body_temperature(temperature):
    """Calculate the body's response based on the given temperature.
    
    :param temperature: The temperature in degrees Celsius.
    :return: The body's response as a string.
    """
    if temperature < 35:
        return "Hypothermia"
    elif temperature <= 37:
        return "Normal"
    elif temperature <= 38:
        return "Slight fever"
    elif temperature <= 39:
        return "Fever"
    else:
        return "Hyperthermia"
    
if __name__ == "__main__":
    for t in [34.5, 35, 38, 39.5]:
        print("%f: %s" % (t, body_temperature(t)))
