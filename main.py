import array
# def ratio():
#     print("\t\t\t\t\tTask 1 Ratio")
#     rationum = int(input("Insert the number: "))
#
#     firstrat = int(rationum/1000)
#     secrat = int(rationum%1000/100)
#     thrrat = int(rationum%1000/10%10)
#     fourat = int(rationum%1000%10)
#
#     if(secrat - thrrat == fourat + firstrat):
#         print("Yes")
#     else:
#         print("No")


#---------------------------------------------------------------------------------

# def Roskomnadzor():
#     print("\t\t\t\t\tTask 2 Roskomnadzor")
#     age = int(input("Your age:"))
#     if(age >= 18):
#         print("Access is allowed")
#     else:
#         print("Access is denied")


#---------------------------------------------------------------------------------


# def ArithmeticProgression():
#     print("\t\t\t\t\tTask 3 Arithmetic Progression")
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     num3 = int(input("Enter third number:"))
#
#     if(num2 == num1+1 and num3 == num2+1):
#         print("Yes")
#
#     else:
#         print("No")


#---------------------------------------------------------------------------------


# def RookMove():
#     print("\t\t\t\t\tTask 4 Rook Move")
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#
#     if(a!=c and b==d or a==c and b!=d):
#         print("Yes")
#     else:
#         print("No")


#---------------------------------------------------------------------------------


# def KingsMove():
#     print("\t\t\t\t\tTask 5 King's Move")
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#
#     if ():
#          print("Yes")
#     else:
#          print("No")


#------------------------------------------------------------------


# def AverageNumber():
#     print("\t\t\t\t\tTask 6 Average Number")
#     a = int(input())
#     b = int(input())
#     c = int(input())
#
#     array = [a, b, c]
#     array.sort()
#     print(array[1])


def NumberOfDays():
    try:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(input("input month:"))
        print(days[month])
    except ValueError:
        print("qwe")


#------------------------------------------------------------------


def WeighInCeremony():
    try:
        kg = int(input("Enter weight:"))
        if kg <= 60 :    print("Light weight")
        elif kg <= 64 and kg >=60:    print("First welterweight ")
        elif kg <= 69 and kg >=64:    print("Welterweight ")
    except ValueError:
        print("qwe")

#ratio()
#Roskomnadzor()
# ArithmeticProgression()
# RookMove()
# AverageNumber()
#NumberOfDays()
WeighInCeremony()
