DEBUG = False

color = "red" if DEBUG else "blue"

if DEBUG:
    color = "red"
else:
    color = "blue"

print(f"{color = }")

# write_message("red" if DEBUG else "blue")
# write_message(DEBUG?"red":"blue"); JAVA