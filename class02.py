# n=int(input("Enter the Number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)



# ****************BILLING SYSTEM********************
grandtotal=0

bills=str()
n=int(input("Enter the Value of n: "))
for i in range(n):
    product=str(input("Enter the Product Name: "))
    price=int(input("Enter the Price: "))
    quantity=int(input("Quantity: "))
    total=price*quantity
    grandtotal=grandtotal+total
    bill=product+" "+str(price)+" "+str(quantity)+"\n"
    

print(bill)
print("Your GrandTotal of Bill is: "+str(grandtotal)+" rs")







    

