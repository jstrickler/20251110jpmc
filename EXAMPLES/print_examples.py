city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

# write to STDOUT (=SCREEN)
# STDERR (also SCREEN)
# STDIN (kbd)
#         SP           SP         SP       NL
print(city, temperature, hit_count, average)
print()
count = 5
#           SP   ' '
print(count, city, end=' ')  # Print space instead of newline at the end
print(temperature)
print()

# Item separator is comma + space
#       ", "          ", "       ", "
print(city, temperature, hit_count, average, sep=", ")
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="")
print()

print(city, temperature, hit_count, average, sep="\t")
print()

language = "Python"

print(f"{language = }")

x = 5
print(f"{x = }")


