"""Search for a number in a list
Robin Small 06/12/2016"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
found = False
print("Before search", found)
for number in my_list:
    if number == 7:
        found = True
        print("After search found =", found)
        print("The number ", number, "was found")
        break  # ends loop as soon as first instance of 7 is found rather than continuing to search the list.
