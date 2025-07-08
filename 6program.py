n=int(input("Enter how long list you want:"))
num_list=[]
for i in range(n):
    num=int(input("Enter a number: "))
    num_list.append(num)

max_value=max(num_list)
min_value=min(num_list)
sum_value = sum(num_list)
print("Maximum of list is:",max_value)
print("Minimum of list is:",min_value)
print("Sum of list:",sum_value)