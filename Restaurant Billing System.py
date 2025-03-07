menu={
    'Pizza':100,
    'Pasta':60,
    'Burger':50,
    'Tea':15,
    'Hot Tea':20,
    'Green Tea':30
}

print("Welcome To Bann Restaurant")
print("Pizza:100/-\nPasta:'=60/-\nBurgur:=50/-\nTea:=15/-\nHot Tea:=20/-\nGreen Tea:=30/-\n")

order_total=0

item1=input("Enter the name of the item you want to order :")
if item1 in menu:
    order_total=order_total+menu[item1]
    print(f"your item {item1} has beeen added to your order ")

else:
    print(f"Your order item is not available")

print("----------------------------------------------------")

another_order=input(f"Do you want to add another order ?(Yes/No)")

if another_order=="Yes "or "yes":
    item2=input("Enter the name of second item :")
    if item2 in menu :
        order_total=order_total+menu[item2]
        print(f"Your item has been added to order")
    
    else:
        print(f"Item is not available")

print("----------------------------------------------------")
print(f"Total amount of :{order_total}")