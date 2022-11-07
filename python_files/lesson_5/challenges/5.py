# CHALLENGE 5: 
# Create an empty list
# APPEND list to add items: 76, 92.3, “hello”
# Use CONCATENATION to add True, 4, 76
# (new list should be: [76, 92.3, “hello”, True, 4, 76]
# THEN:
# Append “apple” and 76 to the list.
# Insert the value “cat” at position 3.
# Insert the value 99 at the start of the list.
# Find the index of “hello”.
# Count the number of 76s in the list.
# Remove the first occurrence of 76 from the list.
# Remove True from the list using pop and index.

# Add screenshot of code and screenshot of terminal window to Lesson 5 Challenges doc

listy = []
listy.append(76)
listy.append(92.3)
listy.append('hello')
listy.append(True)
listy.append(4)
listy.append(76)

print(listy)

listy.append('apple')
listy.append(76)
listy[3] = "cat"
listy[0] = 99

print(listy.index('hello'))
print(listy.count(76))

listy.pop(listy.index(76))
listy.pop(5)

print(listy)

