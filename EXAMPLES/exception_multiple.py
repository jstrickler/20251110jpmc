x = 5
y = "cheese"
y = 8
try:
    z = x + y
    f = open("sesame.txt")
    print("Bottom of try")

except (IOError, TypeError) as err:  # Use a tuple of 2 or more exception types
    print("Naughty programmer! ", err)

except ZeroDivisionError as err:
    pass

except Exception as err:
    print("Did not expect this:", err)
