my_list = [12, 14, 15, 34, 45, 56, 67, 78, 89, 90]

# print("my_list all items", my_list)

# Accessing the first item
# print(my_list[0])

# # Accessing the third item
# print("Third item", my_list[2])

# # Accessing the last item
# print("Last item", my_list[-2])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[0:4])

# Accessing from the 5th item to the end
# print(numbers[4:])

# Accessing items slice two by two
# print(numbers[::3])

numbers.append(11)
# print("After appending 11", numbers)

# pint last item
# print("Last item", numbers[-1])

# Inserting an item at a specific index
numbers.insert(3, 100)
# print("After inserting 100 at index 3", numbers)

# Removing an item by value
numbers.remove(100)
# print("After removing 100", numbers)

# min, max, sum
# print("Min", min(numbers))
# print("Max", max(numbers))
# print("Sum", sum(numbers))


list_numbers = [12, 13, 15, 18, 20, 21, 23, 25, 27, 30]

sum_numbers = 0
for number in list_numbers:
    # print("Number", number)

    if number % 2 == 0:
        # print("Even number", number)

        sum_numbers = sum_numbers + number

# print("Sum of even numbers", sum_numbers)


students_scores = [45, 67, 89, 90, 78, 56, 34, 23, 12, 10]

print("Students scores", students_scores)

sorted_scores = sorted(students_scores, reverse=True)

print("Sorted scores", sorted_scores)

top_3_scores = sorted_scores[:3]
# print("top 3 scores", sorted_scores[-3:])
print("top 3 scores", top_3_scores)
















