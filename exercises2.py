minimumScore = 70
n1 = float(input("digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
n3 = float(input("digite a terceira nota"))

results = (n1 + n2 + n3)/3

if results >= minimumScore:
   print("You are Approved")
else :
   print("You was invited to be remake this discipline")

print("Your final score is  " , results )    