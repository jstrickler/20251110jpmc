import sys
FILE_PATH = "DATA/words.txt"

count = 0

if len(sys.argv) == 1:
    print("Please specify word length")
    exit()

word_length = int(sys.argv[1])
with open(FILE_PATH) as words_in:
    for raw_line in words_in:
        line = raw_line.rstrip()
        if len(line) == word_length:
            count  += 1
print(f"{count = }")

