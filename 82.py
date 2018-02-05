import ephem

jupiter = ephem.Jupiter('1230/1/1')
print(jupiter.sun_distance)
