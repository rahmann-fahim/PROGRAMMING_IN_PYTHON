string = input("Enter a string: ")

words = string.split()
reversed_words = [word[::-1] for word in words]

result = " ".join(reversed_words)


print("Original String:", string)

print("Reversed Words:", result)
