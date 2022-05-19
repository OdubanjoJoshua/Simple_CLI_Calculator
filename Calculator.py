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

# Assigning values based on the operator string been chosen
multiply = int(first_number) * int(second_number)
divide = int(first_number) / int(second_number)
add = int(first_number) + int(second_number)
subtract = int(first_number) - int(second_number)

# A conditional statement to select the various options gven
if arithmetic_op == "Multiply":
    print(" >>> " + str(first_number) + " * " + str(second_number) + " = " + format(multiply))
elif arithmetic_op == "Divide":
    print(" >>> " + str(first_number) + " / " + str(second_number) + " = " + format(divide))
elif arithmetic_op == "Add":
    print(" >>> " + str(first_number) + " + " + str(second_number) + " = " + format(add))
elif arithmetic_op == "Subtract":
    print(" >>> " + str(first_number) + " - " + str(second_number) + " = " + format(subtract))
else:
    print("""--- Not valid!!! ---
--- Pick from the options given ---""")