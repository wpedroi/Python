# x = [1, 2, 3, 4, 5]
# x.sort(reverse=True)
# for i in x:
#     print (i)

x = {}
for i in range(2):
    item = input("Enter item: ")
    qyt = int(input("Enter quantity: "))
    x[item] = qyt
y = input ("DO you want to sell('y' for yes - 'n' for no): ")
if y == 'y':
    p = input("enter item name: ")
    for j in range(2):
        if p == x:
            while a <= x[item]:
                a = int(input("Quantity is ", x[item], "Enter qyt: "))
                x[item] = x[item] - a

