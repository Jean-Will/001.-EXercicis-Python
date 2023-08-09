print("We will calculate time to be have for you to be retired  ")
minAge = 65
year = 2023
resgisterName = input("please write your name")
registerBirth = int(input("please write your year birth"))
registerActualYear = int(input("please write what year do you stay"))
calc = year - registerBirth
retired = minAge - calc

if retired >= calc:
   print("The year to be completed for retired is "  , retired)
else :
   print("you should be retired ")
 