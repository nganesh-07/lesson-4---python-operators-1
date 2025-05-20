totalamount = int(input("How much do you want to enter?:"))

bill1 = totalamount//100
bill2 = (totalamount%100)//50
bill3 = (totalamount%100)//20
bill4 = (totalamount%100)//10
bill5 = (totalamount%100)//5

print("100 dollar bills:", bill1)
print("50 dollar bills:", bill2)
print("20 dollar bills:", bill3)
print("10 dollar bills:", bill4)
print("5 dollar bills:", bill5)