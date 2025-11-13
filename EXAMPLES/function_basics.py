# define function

def doit():
    say_hello()

def say_hello():
    print("Hello, world")

#say_hello()  # Call function
x = doit()
print(f"{x = }")

def eggs():
    return 123

e = eggs()
print(f"{e = }")

print(eggs()  + 2)

def get_things():
    return 'a', 'b'

result = get_things()
print(f"{result = }")


def greet(whom="world"):
    print(f"Hello, {whom}")

greet("world")
person = "Mom"
greet(person)
greet()

def make_string(chr, count):
    return chr * count

print(make_string('*', 10))
print(make_string('-', 60))


def process_files(color="red", *file_list):
    print(f"{color = }")
    
    for file_name in file_list:
        print(f"processing {file_name}")

process_files('blue', 'eggs.txt', 'spam.txt')
process_files('purple', 'wombats.txt')
process_files()