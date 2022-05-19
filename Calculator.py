# Created input for 2 numbers
first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))

# Option for the arithmetic operator the user wants to use
arithmetic_op = input("""Do you want to : Multiply
                 Divide
                 Add
                 Subtract
Pick one of the above options: """)
# Even though the user doesn't capitalize it, this makes the option capitalize so python understands
arithmetic_op = arithmetic_op.capitalize()
print(arithmetic_op.capitalize())