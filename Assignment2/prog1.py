n=int(input("Enter the number of items: "))
cost=0
if(n<10):
    cost=n*120
elif(n>=10 and n<=99):
    cost=n*100
elif(n>=100):
    cost=n*70

print(f"The total cost is:{cost}")
