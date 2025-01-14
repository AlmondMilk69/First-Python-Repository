'''
name = input('What is your name? ')
print('Hello ' + name)
birth_year = input('Enter your birth year: ')
age = 2025 - int(birth_year)
print(age)
'''

x = input('What is the value of x? ').strip
y = input('What is the value of y? ').strip
# i dont understand why .strip is throwing an error???
# working on how to ask the user what operation they want to perform
# a = input('What operation would you like to perform? ')

z = int(x) + int(y)

print('z is equal to:', int(z))