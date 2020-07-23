def compare(input_1,input_2):
    return_string =""

# - - - - - - C O R E - - - - - - -

    if input_1 > input_2:
        return_string = f"{input_1} is greater than {input_2}"
    if input_1 < input_2:
        return_string = f"{input_1} is smaller than {input_2}"
    if input_1 == input_2:
        return_string = "both numbers are equal"
    return return_string

# - - E X T E N D E D  - - assume input will be provided from the INPUT class which is always in the string format - - 

# to remain sane, limit types to float, int and string. Initiate empty variables: 

    # int_1 = None
    # float_1 = None
    # string_1 = None
    # int_2 = None
    # float_2 = None
    # string_2 = None

  


# - Derermine what type of input will be supplied and store in a resective holder by changing it if supplied input matches type 

#     try:    
#         float_1 = float(input_1)   
#     except ValueError:
#         string_1 = input_1

#     try:
#         float_2 = float(input_2)
#     except ValueError:
#         string_2 = input_2

# # determine if numeric strings are ints or floats: ???
#     if float_1 == int(input_1):
#         int_1 = int(input_1)
#         float_1 = None
   
   
#     # if float_1.is_integer():
#     #     int_1 = int(float_1)
#     #     float_1 = None
    
#     if float_2 == int(input_2):
#         int_2 = int(input_2)
#         float_2 = None


    # if float_2.is_integer():
    #     int_2 = int(float_2)
    #     float_2 = None

    # print("1 fl1")
    # print(float_1)
    # print("2 fl2")
    # print(float_2)
    # print("3 int1")
    # print(int_1)
    # print("4 int2")
    # print(int_2)
    # print("5 str1")
    # print(string_1)
    # print("6 str2")
    # print(string_2)

# - - - - OLD working code
    # try:
    #     print("1")
    #     int_1 = int(input_1)
    #     print("2")
    # except ValueError:
    #     print("3")
    #     try:
    #         print("4")
    #         float_1 = float(input_1)
    #         print("5")
    #     except ValueError:
    #         print("6")
    #         string_1 = input_1
    #         print("7")

    # try:
    #     print("8")
    #     int_2 = int(input_2)
    #     print("9")
    # except ValueError:
    #     print("10")
    #     try:
    #         print("11")
    #         float_2 = float(input_2)
    #         print("12")
    #     except ValueError:
    #         print("13")
    #         string_2 = input_2
    #         print("14")
# -- - - - - - --  END OF OLD 

# - EXT104:125
    # if (int_1 is not None) and (int_2 is not None):
    #     if int_1 > int_2:
    #         return_string = f"{int_1} is greater than {int_2}"
    #     if int_1 < int_2:
    #         return_string = f"{int_1} is smaller than {int_2}"
    #     if int_1 == int_2:
    #         return_string = "both numbers are equal"
    # #return return_string


    # elif (string_1 is not None) and (string_2 is not None):
    #     print("st1")
    #     if string_1 == string_2:
    #         print("st2")
    #         return_string = f"both inputs were equal strings of value: {string_1}"

    # elif (float_1 is not None) and (float_2 is not None):
    #     return_string = "Whaaaat"

    # return return_string
    
# one = "3.5"
# two = "6.7"
#print(compare(str("hi"),str("hi")))
#print(compare(one,two)
#print(f"{float_1} and {float_2}")

#valueError - exception you get when you try to convert the string from the input method into int or float using int(input) or float(inpiut)

#print(compare(1,4))

# "3 is greater than 1"

# '5 is smaller than 11"

# "both numbers are equal"

#compare("McGruuuber","McGruuuber")