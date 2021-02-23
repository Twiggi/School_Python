import math

x = 3

def my_sin(theta):
    theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    result = 0
    termsign = 1
    power = 1

    for i in range(x):
        result += (math.pow(theta, power) / math.factorial(power)) * termsign
        termsign *= -1
        power += 2
    return result

def my_cos(theta):
    theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    result = 0
    termsign = 1
    power = 0

    for i in range(x):
        result += (math.pow(theta, power) / math.factorial(power)) * termsign
        termsign *= -1
        power += 2
    return result

def my_tan(theta):
    return my_sin(theta) / my_cos(theta)

def my_atan(theta):
    if theta > (-1) and theta < (1):
        return my_atan_working(theta)
    result = 0
    termsign = 1
    power = 1

    for i in range(x):
        result += (1 / ((math.pow(theta, power)) * power)) * termsign
        termsign *= -1
        power += 2

    if theta > 0:
        result = (math.pi/2) - result
    else:
        result = - (math.pi / 2) - result
    return result

def my_atan_working(theta):
    result = 0
    termsign = 1
    power = 1

    for i in range(x):
        result += ((math.pow(theta, power)) / power) * termsign
        termsign *= -1
        power += 2

    return result

def my_arcsin(theta):
    if theta < (-1) and theta > (1):
        raise ValueError('Parameter should be in interval <-1;1>')
    result = 0
    power = 1

    for i in range(x):
        result += (math.factorial(2*i)*math.pow(theta,power))/(math.pow(4,i)*(math.factorial(i))*(math.factorial(i))*(2*i+1))
        power += 2

    return result



# print("Sinus")
# print(my_sin(1))
# print(math.sin(1))
# print()
# print()
#
# print("Cosinus")
# print(my_cos(1))
# print(math.cos(1))
# print()
# print()
#
# print("Tang")
# print(my_tan(101))
# print(math.tan(101))
# print()
# print()

# print("Atang")
# print(my_atan(0.5))
# print(math.atan(0.5))

# print("Arcsin")
# print(math.asin(0.01))
# print(my_arcsin(0.01))