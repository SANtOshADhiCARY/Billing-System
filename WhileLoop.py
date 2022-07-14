# # Syntax

# while<condition>:
#     <operation>


# a=0
# while a<=5:
#     print("Interesting")
#     a= a+1

# ****************EASIEST WAY TO FIND THE MULTIPLE OF ANY NUMBER**********************
# i=1
# n=int(input("Enter any Number: "))
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1

a="Education is the key to success"
l=len(a)
i=0
while i<l:
    if a[i]==" ":
        i=i+1
        continue
    print(a[i],end="")
    i=i+1
