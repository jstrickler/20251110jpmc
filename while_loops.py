i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("Enter  your name: ")
    if name == 'q':
        break
    if name == '':  # user just pressed <ENTER>
        print("Please enter your name")
        continue
    print(f"Hello, {name}")