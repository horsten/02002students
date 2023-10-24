"""Exercise 7.4: Color Hue."""

import cmath
import math

def rgb_to_hue_complex(RGB: tuple) -> float:
    """Return the hue given RGB values using complex math.

    :param RGB: Tuple containing  three RGB values.
    :return: Hue in degrees.
    """
    (r,g,b) = RGB
    angle = math.degrees(cmath.phase(complex(r - g, g - b)))
    return angle if angle>=0 else angle+360

def rgb_to_hue(RGB: tuple) -> float:
    """Return the hue given RGB values.

    :param RGB: Tuple containing  three RGB values.
    :return: Hue in degrees.
    """
    (r,g,b) = RGB
    m = max(r,g,b)
    delta = m-min(r,g,b)
    if (r == m):
        angle = 60*(g-b)/delta
    elif (g == m):
        angle = 120+60*(b-r)/delta
    else:
        angle = 240+60*(r-g)/delta
    return angle if angle>=0 else angle+360

if __name__ == '__main__':
    testcases = [
                    ((0.6, 0.2, 0.3), 345.0),
                    ((0.3, 0.6, 0.2), 105.0),
                    ((0.1, 0.1, 0.2), 240.0),
                    ((0.2, 0.25, 0.3), 210.0),
                    ((0.9, 0.9, 0.3), 60.),
                    ((0.6, 0.8, 0.8), 180.),
                    ((1.0, 0.1, 0.1), 0.0),
                    ((0.7, 0.6, 0.7), 300.0),
                    ((0.5, 0.1, 0.6), 288.0)
                ]

    for (rgb, angle) in testcases:
        print(f'RGB: {rgb} Complex method: {rgb_to_hue_complex(rgb)} Non-complex method: {rgb_to_hue(rgb)} Expected: {angle}')
