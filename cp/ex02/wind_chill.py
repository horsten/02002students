"""Exercise 2.4: Wind chill."""
def wind_chill(temperature:int, windspeed:float):
    """Calculate and print the wind chill temperatures.

    :param temperature: the actual temperature.
    :param windspeed: the wind speed.
    """
    wc = 13.12 + 0.6215 * temperature - 11.37 * pow(windspeed,0.16) + 0.3965*temperature*pow(windspeed,0.16)
    print("Temperature: %d degrees feels like %d degrees." % (temperature, round(wc) ))