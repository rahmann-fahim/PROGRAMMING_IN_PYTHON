numbers = [10, 20, 30, 40, 50, 60]

target = int(input("Enter value to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Value found at index", i)
        found = True
        break

if not found:
    print("Value not found")
