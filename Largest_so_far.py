'''Searches through a list of numbers and prints the highest value.
Robin Small 06/12/2016'''

my_list = [4,8,5,10,25,100,1,77,98,37,29]

largest_so_far = None
print("Before loop", largest_so_far)
for number in my_list:
    if largest_so_far is None:
        largest_so_far = number
    elif number > largest_so_far:
        largest_so_far = number
    print(largest_so_far, number)

print("Loop complete", largest_so_far)