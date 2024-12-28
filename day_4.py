#reverse of a string
s = 'HelloWorld'
reverse_str = s[::-1]
print(reverse_str)

#substring b/w 5-10
sentence = input("Enter a sentence: ")
# Check- at least 10 characters
if len(sentence) >= 10:
    extracted_substring = sentence[4:10]  
    print("Extracted Substring:", extracted_substring)
else:
    print("Input sentence should have at least 10 characters.")

#q2
input_string = "python is fun"
# Reversing the string using slicing
reversed_string = input_string[::-1]
print(f"The reversed string is: {reversed_string}")

#isalnum()
input_str = "2k25"
is_alnum = input_str.isalnum()
print(f"The string contains only alphanumeric characters: {is_alnum}")

#count()
input_string = "abracadabra"
# Counting 'abra'
substring_count = input_string.count('abra')
print(f"The number of times 'abra' appears is: {substring_count}")