import random
import string


def mangler(input_string):
    """
    Simple mangler function that adds a random suffix to the input string.
    """
    # Generate a random suffix of length 5 consisting of letters and digits
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Combine the input string and the suffix
    result = input_string + suffix

    return result


# Example usage:
original_variable = input("Enter a String  ")
mangled_variable = mangler(original_variable)

print(f"Original Variable: {original_variable}")
print(f"Mangled Variable: {mangled_variable}")