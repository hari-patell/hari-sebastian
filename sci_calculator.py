#Set up code, import math library
import math
current_result = 0.0
print(f'Current Result: {current_result}')
num_calculations = 0
sum_calculations = 0.0
user_operation = 0
stop_code = 0
menu= True
#as long as the operation selected isn't 0, the code will continue to show the menu
while menu:
    print('Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')
    calc_run=True

    while calc_run:
        user_operation = int(input("Enter Menu Selection: "))
        #if the operation isn't between 0 and 7 it will display the error

        if user_operation < 0 or user_operation > 7:
            print('Error: Invalid selection!')
        #if the operation is 0 it will print an exit statement and break the while loop
        elif user_operation == 0:
            print('Thanks for using this calculator. Goodbye!')
            stop_code = 1
            calc_run=False
            menu=False
            break
        #if the other statements didn't go off, they must have input a valid number and thus we can try and calculate
        elif user_operation != 7:
            first_operand = (input("Enter first operand: "))
            second_operand = (input("Enter second operand: "))
            num_calculations += 1
            if first_operand == 'RESULT':
                first_operand = float(current_result)
            elif second_operand == 'RESULT':
                second_operand = float(current_result)
            else:
                first_operand = float(first_operand)
                second_operand = float(second_operand)

            if user_operation == 1:
                current_result = first_operand + second_operand
                print("Current Result: " + str(current_result))
                sum_calculations += (current_result)
                break
            elif user_operation == 2:
                current_result = first_operand - second_operand
                print("Current Result: " + str(current_result))
                sum_calculations += (current_result)
                break
            elif user_operation == 3:
                current_result = first_operand * second_operand
                print("Current Result: " + str(current_result))
                sum_calculations += (current_result)
                break
            elif user_operation == 4:
                current_result = first_operand / second_operand
                print("Current Result: " + str(current_result))
                sum_calculations += (current_result)
                break
            elif user_operation == 5:
                current_result = float(first_operand) ** float(second_operand)
                print("Current Result: " + str(current_result))
                sum_calculations += (current_result)
                break
            elif user_operation == 6:
                current_result = math.log(second_operand, first_operand)
                print("Current Result: " + str(current_result))
                sum_calculations += (current_result)
                break
            #this will keep adding to the sum of all the calculations




        #if the number of calculations were 0 and they user put in 7 on the menu it will display that
        elif num_calculations == 0 and user_operation == 7:
            print('Error: No calculations yet to average!')
            menu=False
        #this shows the averages
        else:
            print('Sum of calculations: '+ str(sum_calculations))
            print('Number of calculations: '+ str(num_calculations))
            print(f"Average of calculations: {float(sum_calculations / num_calculations):.2f}")
            menu=False




