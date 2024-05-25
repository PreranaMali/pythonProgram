my_string = "   Hello World! it's me piya  "

print(my_string.upper())  # Output: '   HELLO, WORLD!   '
print(my_string.strip())  # Output: 'Hello, World!'

words = my_string.split(",")
print(words)  # Output: ['   Hello', ' World!   ']

