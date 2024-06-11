

import __main__


def main():
	user_input = input("Enter a string in camel case: ")
	print(camel_to_snake(user_input))

def camel_to_snake(s):
	# Initialize an empty string to build the output
	new_string = ""
	
	# Iterate over each character in the input string
	for char in s:
		# Check if the character is an uppercase letter
		if char.isupper():
			# Add an underscore followed by the lowercase version of the character
			new_string += "_" + char.lower()
		else:
			# Add the original character (lowercase or non-letter) to the output
			new_string += char
	
	# Return the completed output string
	return new_string

if __name__ == __main__:
	main()
