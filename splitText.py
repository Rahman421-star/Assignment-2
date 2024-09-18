# Corrected Decrypted Code with Comments

total_inventory = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


def process_numbers():
    global total_inventory  # Refers to global total_inventory
    local_inventory = 5
    numbers = [1, 2, 3, 4, 5]

    # Iterate while local_inventory is greater than 0
    while local_inventory > 0:
        if local_inventory % 2 == 0:  # Check if even
            numbers.remove(local_inventory)  # Remove the number from list
        local_inventory -= 1  # Decrease inventory

    return numbers  # Return modified list


# Set with some duplicate values
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()


def update_dict():
    local_inventory = 10
    my_dict['key4'] = local_inventory  # Add new key-value pair to dictionary


update_dict()


def update_total():
    global total_inventory
    total_inventory += 10  # Increment the global total_inventory by 10


# Print numbers from 0 to 4
for v in range(5):
    print(v)
    v += 1  # Increment v (not needed in Python for loop)

if my_set != set() and my_dict['key4'] == 10:
    print("Condition met!")  # Print message if conditions are met

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(total_inventory)
print(my_dict)
print(my_set)
