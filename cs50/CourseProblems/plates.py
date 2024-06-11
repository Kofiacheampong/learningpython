def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        len(s) >= 2 and len(s) <= 6  # Minimum length of 2 characters and a max of 6
        and s[:2].isalpha()  # First two characters are letters
        and s.isalnum()  # Only alphanumeric characters (letters and numbers)
        and not s.isspace()  # No whitespace characters
        and numbers_at_end(s)  # Numbers must be at the end
    ):
        return True
    else:
        return False


def numbers_at_end(s):
    # Find the index of the first digit
    num_start_idx = None
    for i, c in enumerate(s):
        if c.isdigit():
            num_start_idx = i
            break
    
    # If no digits found, return True
    if num_start_idx is None:
        return True
    
    # Check if all characters after the first digit are also digits
    for c in s[num_start_idx:]:
        if not c.isdigit():
            return False
    
    # Check if the first digit is not '0'
    if s[num_start_idx] == '0':
        return False
    
    return True


main()