# Corrected and commented code

# This variable stores the total inventory count
total_inventory = 100

# A dictionary with some initial key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


# Function to process numbers and modify a global variable
def process_numbers():
    global total_inventory  # Indicates we are using the global total_inventory variable
    local_inventory = 5  # Local variable within this function
    numbers = [1, 2, 3, 4, 5]  # List of numbers to process

    # Loop to process numbers while local_inventory is greater than 0
    while local_inventory > 0:
        if local_inventory % 2 == 0:  # Check if local_inventory is even
            # Removed logical error: Ensured the number being removed is present in the list
            if local_inventory in numbers:
                numbers.remove(local_inventory)  # Remove the number from list if it's even
        local_inventory -= 1  # Decrease local_inventory by 1

    return numbers  # Return the modified list of numbers


# Set with some duplicate values, sets in Python automatically handle duplicates
# Fixed an error: Using a set to demonstrate that duplicates will be removed automatically
my_set = {1, 2, 3, 4, 5}

# Call the process_numbers function and store the result
result = process_numbers()


# Function to update the dictionary
def update_dict():
    local_inventory = 10  # Local variable within this function
    # Added a key 'key4' to the dictionary with the value of local_inventory
    my_dict['key4'] = local_inventory


# Call the update_dict function to modify the dictionary
update_dict()


# Function to update the total_inventory
def update_total():
    global total_inventory
    # Increment total_inventory by 10
    total_inventory += 10


# A loop to print numbers from 0 to 4
for v in range(5):
    print(v)
    # Removed redundancy: The increment `v += 1` is unnecessary since `v` is controlled by the loop
    # Removed `v += 1`

# Condition to check and print a message if certain conditions are met
if my_set != set() and my_dict['key4'] == 10:
    # Fixed the logical error: Used proper syntax to check if a set is not empty
    print("Condition met!")

# Check if the number 5 is not a key in the dictionary
# Fixed logical error: Check for presence of 5 as a key in the dictionary, not as a value
if 5 not in my_dict:
    print("5 not found in the dictionary!")

# Print statements to display the current state of variables
print(total_inventory)  # Output the total inventory value
print(my_dict)  # Output the current state of the dictionary
print(my_set)  # Output the set to show unique values only

print("https://github.com/Rahman421-star/Assignment-2")