# CHALLENGE 4:
# Create a LIST that starts with a generic template for a contact
# Have user input one item at a time to eventually modify the template contact to be their own information

# Add screenshot of code and screenshot of terminal window to Lesson 5 Challenges doc

contract = [
    'name', 
    'location',
    'phone number',
    'email', 
    'contract type',
    'contract body',
    'signature',
    'extra data'
    ]

for i in range(len(contract)):
    print(f'please input your: {contract[i]}')
    
    #get input and edit the list
    res = input(">"); contract[i] = res.upper()


print(contract)