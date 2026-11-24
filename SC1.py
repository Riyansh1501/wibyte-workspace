print("hello")
print("welcome to Riyansh`s cake bakery")
print("if u dont want cake go next doors")

menu["mammas cake","choco cake","lemon cake","vanilla cake","fruit cake"]
pric[20.00,18.99,19.87,20.00,23.00]
#swiss francs


print('ITEM', 'PRICE (swiss francs), excl. Tax', sep='\t\t\t')
for jj in range(len(menu)):
    print(str(jj+1)+'. '+menu[jj], price[jj], sep='\t\t')


shopping cart=[]
shopping quant=[]
shopping complete=0

while shopping == 0:
    order = int(input('Enter 1 to 5 to select a cake, 6 to proceed to checkout.\n')) 
   

print('You selected', menu[order-1])
quant = int(input('How many cakes do you wish to purchase?\n'))





if menu[order-1] in shopping cart:
            idx = shopping cart.index(menu[order-1])
            
            shopping quant[idx]+=quant
        else:
            shopping cart.append(menu[order-1])        
            shopping quant.append(quant)        
        
        print('Added to shopping cart:', quant, 'units of', menu[order-1])
    elif order == 6:
        shopping complete = 1
    else: 
        print("Sorry that was not a valid input.")

print()
print() 
print(" ur shopping cat :")


grandtot = 0.0
print('ITEM', 'QUANT', 'CAKE PRICE', 'TOTAL', sep='\t\t\t')    
for jj in range(len(shopping cart)):
    idx = menu.index(shopping cart[jj])
    unit price=price[idx]
    tot price = round(unit price*shopping quant[jj], 2)
    grand tot += tot price
    print(shopping cart[jj], shopping quant[jj], unit price, tot price, sep='\t\t\t')

grand tot = round(grand tot, 2)

print()
print()
print()

print("your total price in (swiss francs) is ",grand tot)
        