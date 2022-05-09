'''
Shopping Cart: 
1. Add Product: (id,name,price,qty,desc,category)
2. View Products: all products
3. Add to cart: Enter Product ID: 2313
4. Checkout: Bill Amount Generation, Stock Update
Enter your choice:
'''

""" Empty Dictionary """
Products = {}
#{3456 :['Samsung A50', 15000,20,'discription]}
''' store cart '''
Cart = []
#[3456,5432]

""" Function for Main Menu here is choice Selection"""

def mainMenu():
    print("This is The Shopping Cart Application")
    print("-------------------------------------------")
    print("1. Add Product")
    print("2. View Product")
    print("3. Add to Cart")
    print("4. Show Cart")
    print("5. Checkout")
    print("6. Delete Product")
    print("7. Exit")
    print("-------------------------------------------")
    ch = int(input("Enter Your Choice: "))
    return ch

""" Create Function to Add product into Application"""
def addProduct():
    pro_id = int(input("Enter product Id: "))
    pro_nm = input("Enter Product Name: ")
    pro_price = float(input("Enter Product Amount: "))
    pro_qty = int(input("Enter Product Quantity: "))
    pro_desc = input("Enter Product Description: ")
    pro_catego = input("Enter Product Category: ")

    """ Now Here we have to add Product in dictionary as an key value pair"""
    Products[pro_id] = [pro_nm,pro_price,pro_qty,pro_desc,pro_catego]
    print("\nProduct has been successfully added...")
    print("-------------------------------------------")

""" create function for Show All product Which is Availble in Dictionary"""
def showProduct():
    print(Products)
    print("-------------------------------------------")

""" Create Function for add product to Cart"""
def add_to_cart():
    pro_id = int(input("Enter Product id which you want to add to Cart: "))
    if pro_id in Products.keys():
        Cart.append(pro_id)   #ex: [101]
        print("\nCart Updated! Successfully.")
    else:
        print("Product Id Doesn't Exist")

    print("-------------------------------------------")

def showCart():
    j = 1
    for pid in Cart:
        if pid in Products.keys():
            """ Display Product Name and Price"""
            print(Products[pid][0], Products[pid][1])
            j = j + 1
        else:
            print("Id Doesn't Exist")

def deleteCart():
    pid = int(input("Enter Product id Which you want to delete in the Cart: "))
    if pid in Cart:
        Cart.remove(pid)
        print("Product remove from Cart Successfully")
    else:
        print("Id Doesn't Exist")

""" Function for Check Out Process """
def checkOut():
    total_amount = 0
    j = 1
    for i in Cart:
        if i in Products.keys():
            val = Products[i][1]
            price = val
            total_amount = total_amount + price
            j += 1

            """ This for Quantity Update"""
            for i in Products.keys():
                qt = Products[i][2]
                qt = qt - 1
                """ Update dictionary"""
                Products[i][2] = qt


    print("---------------------------------------")
    print("Bill Amount : ",total_amount)
    print("Remaining Quantitu: ",Products)
    
    #for clear cart after purchash
    Cart.clear()
                
            
        

while True:
    choice = mainMenu()
    print("\n")
    if choice == 1:
        addProduct()
    elif choice == 2:
        showProduct()
    elif choice == 3:
        add_to_cart()
    elif choice == 4:
        showCart()
    elif choice == 5:
        checkOut()
    elif choice == 6:
        deleteCart()
    elif choice == 7:
        print("Thank You! for using App.")
        break
    else:
        print("Invalid Input Try Again")

        




