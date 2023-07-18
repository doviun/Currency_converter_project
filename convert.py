import requests
import os
from coins import USD,ILS,EUR

result_list = []


def get_user_value():  #function will get user option USD or Shekel or EURO
    try:
        user_choice = int(input("Please choose an option (1/2/3) :\n1.Dollar to Shekels\n2.Shekels to Dollars\n3.Shekels to Euro\n"))
        if user_choice == 1:
            value_to_convert = amount_to_convert()
            usd = USD(user_input=0)
            result = float(round(usd.calculate(value_to_convert) , 3))
            print("the result is : ",result ," Shekel")
            result_list.append(result)
            start_over()
        elif user_choice == 2:
            value_to_convert1 = amount_to_convert()
            ils = ILS(user_input=0)
            result = float(round(ils.calculate(value_to_convert1),3))  #round the result with 3 digits after the dot
            print("the result is : ",result, " Dollar") # print the result of calculate function
            result_list.append(result)   # add the result to a list
            start_over()
        elif user_choice == 3:
            value_to_convert = amount_to_convert()
            euro = EUR(user_input=0)
            result = float(round(euro.calculate(value_to_convert),3))
            print("the result is : ", result, " euro") # print the result of calculate function
            result_list.append(result)
            start_over()
        else:
            print("Invalid option" )
            get_user_value()
    except ValueError:
        print("Invalid option")
        get_user_value()
def amount_to_convert():  # function will get from user the amount to convert
    try:
        value_to_convert = float(input("Please enter an amount to convert : "))
        return value_to_convert
    except ValueError:
        print("Invalid option")
        amount_to_convert()
def start_over():  # function will ask user if want to start over
    try:
        user_choice2 = input("Do you want to start over? y/n ")
        if user_choice2 == 'y':
            get_user_value()
        elif user_choice2 == 'n':
            finish_calc()
        else:
            print("Invalid option")
            start_over()
    except ValueError:
        print("Invalid option")
        start_over()

def finish_calc(): # function close user actions and summerize the results
    print("Thanks for using our currency converter")
    for results in result_list:
        print(results)
    with open("C:\\Users\\doviu\\PycharmProjects\\Currency_converter_project\\results.txt", "w") as file:
        for num in result_list:
            file.write(str(num) + "\n")
    os.startfile("C:\\Users\\doviu\\PycharmProjects\\Currency_converter_project\\results.txt") # bonus number 5



def main():
    print("Welcome to currency converter")
    get_user_value()

main()


