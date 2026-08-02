my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value =", my_list[index])

except IndexError:
    print("Error: Index out of range.")

except TypeError:
    print("Error: Index must be an integer.")

except ValueError:
    print("Error: Please enter a valid integer.")
