x = 5
y = "cheese"

try:  # Execute code that might have a problem
    z = x + y  # exception happens here
    print("Bottom of try")
except TypeError as err:    # Catch the expected error; assign error object to err
    print("Naughty programmer! ", err)
    exit()
else:
    print(f"{z = }")
finally: # must run, no matter what
    del z
    

print("After try-except")  # Get here whether or not exception occurred
