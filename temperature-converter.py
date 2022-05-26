def convert(s):

    f = float(s)

    c = (f - 32) * 5/9

    return round(c,0)

temp = input('Please enter temperature in Fahrenheits:\n')

print(str(convert(temp))+"°C")
