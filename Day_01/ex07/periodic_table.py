import sys

def get_object_from_line():
    line_read = open("periodic_table.txt", "r").readline().strip().split('=')[1].strip()

    # Split the string into a list of key-value pairs
    key_value_pairs = line_read.split(', ')

    # Create an empty dictionary
    data_dict = {}

    # Loop through each key-value pair and add it to the dictionary
    for key_value in key_value_pairs:
        key, value = key_value.split(':')
        data_dict[key] = value.strip()

    return data_dict

if __name__ == "__main__":
    print(get_object_from_line())