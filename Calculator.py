# This is a simple arithmetic calculator
print ("Welcome to this calculator")

# Create add function
def add(x, y):
    result = int(x) + int(y)
    print (result)
# Create sub function
def sub(x,y):
    result = int(x) - int(y)
    print (result)
# Create multiplication function
def mul(x, y):
    result = int(x) * int(y)
    print (result)
# Create divide function
def div(x,y):
    result = int(x) / int(y)
    print (result)

# Clear initial variable
on = 0
result = 0

# Main loop
while on < 1:

    # Ask for calculation
    op = input("Please enter your calculation with a space between values:")

    # Check if user is trying to exit calculator
    if op == 'exit':
        print("Exiting, good bye.")
        break

    # Check if it is a addition
    elif op.split(' ')[1] == '+':

        # Call addition function
        add(op.split(' ')[0], op.split(' ')[2])

    elif op.split(' ')[1] == '-':

        # Call subtraction function
        sub(op.split(' ')[0], op.split(' ')[2])

    elif op.split(' ')[1] == '*' or op.split(' ')[1] == 'x':

        # Call subtraction function
        mul(op.split(' ')[0], op.split(' ')[2])

    elif op.split(' ')[1] == '/':

        # Call subtraction function
        div(op.split(' ')[0], op.split(' ')[2])