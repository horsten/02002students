"""Exercise 3.6: BAC Calculator."""

def bac_calculator(alcohol_consumed: float, weight: float, gender: str, time: float) -> float:
    """Calculate the blood alcohol concentration based on the alcohol consumed, body weight, and time since consumption.
    
    :param alcohol_consumed: The total amount of alcohol consumed in grams (float)
    :param weight: The person's body weight in kilograms (float)
    :param gender: The person's gender, which must be a string of either "male" or "female" (str)
    :param time: The time elapsed since alcohol consumption in hours (float)
    :return: The calculated blood alcohol concentration (BAC) as a float value.
    """
    if gender.lower() == "male":
        b = 0.015
        r = 0.68
    elif gender.lower() == "female":
        b = 0.017
        r = 0.55
    else:
        raise Exception("Invalid Gender specified")
    return (((alcohol_consumed)/(r*weight)) * 100 ) - (b * time)

if __name__ == "__main__":
    for t in [(0.028,80,"male",2),
              (0.028,80,"female",2)]:
        print("BAC %f %f %s %f: %f" % (t[0], t[1], t[2], t[3], bac_calculator(t[0],t[1],t[2], t[3])))
