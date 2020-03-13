'''
Below is the logic of the program.
Check the Design Pattern file for its implementation using design pattern.
For the learning purpose I've used Facade design pattern.
'''
thesentence = input("Enter the string : ")
print(thesentence)
splitlist = thesentence.split()
print(splitlist)
logo = [x[0] for x in splitlist]
print(logo)
seperator = ""
print(seperator.join(logo))
