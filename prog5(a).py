num=int(input("Enter the number : "))
l=0
for i in range(2,num):
    if num % i==0:
        l+= 1
        break
else:
    print("The number has remainder when one number divided by another number  ")

if(l!=0):
  print("The number hsa not remainder when one number divided by another number")
