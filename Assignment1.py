products=[]
def addProduct():
    productname=input("Enter product's name: ")
    for prod in products:
        if(prod['name']==productname):
            print("Product already existed!")
            return
    try:
        price=float(input("Enter price: "))
        stock=float(input("Enter product in stock: "))
    except ValueError:
        print("Incorrect format for price and stock.")
        return
    location=input("Location ")
    tag_input=input("Enter tags")
    tags={t.strip() for t in tag_input.split(",")}
    products.append({'name': productname,"price": price, "stock": stock,"location ": location,"tags": tags})
    
    print(f"name : {productname}, price : {price}, stock : {stock} ,location : {location} ,tags: {tags}  Product added successfully! ") 

#printing all the products
def getallproducts():
    if (products==[]):
        print("No products is added. First add products.")
    else:
        for prod in products:
            print(prod)

def lowstockWarning():
    lowstockproducts=[]
    if products==[]:print("No product is being added. First add products.")
    else:
        for prod in products:
            
            if prod['stock']<=5:
                print("Warning! Low on stock.")
                lowstockproducts.append(prod)
        print(" Low stock products are ")
        for lsp in lowstockproducts:
            print(lsp)
                
def updatestock():
    
    if products==[]:print("No product is being added. First add products.")
    else:
        for prod in products:
            name=input("Enter name: ")
            if prod['name']==name:
                newstock=int(input("Enter updated stock value."))
                prod['stock']=newstock
                print("Stock is updated successfully.") 
            else:
                print("Product is not added.")   
        
def deleteproduct():
    if products==[]:print("No product is being added. First add products.")
    else:
        rpname=input("enter product name : ")
        for prod in products:
            if prod['name']==rpname:
                products.remove(prod) 
                print("product is successfully removed.")
            else:
                print("product doesn't existed.")

def totalvalueofallprodinstock():
    if products==[]:print("No product is being added. First add products.")
    else:
        totalvalueofallprodinstock=1.0
        for prod in products:
                totalvalueofallprodinstock+=prod['stock']*prod['price']
        print("\n Total value of all products in stock are :",totalvalueofallprodinstock)
                
        

def discountbytags():
    if products==[]:print("No product is being added. First add products.")
    discount_products=[]
    for prod in products:
        if prod['tags']=="clearance":
            prod['price']*=0.5
            discount_products.append(prod)
            print("Discount is applied successfully!")
    for prod in discount_products:
        print(prod)
        
def menu():
    choice=1
    while choice:
        print("******************Welcome to the Inventory Tracker*****************")
        print()
        print( "1.Get all products \n",
              "2. Low on stock warnings \n ",
              "3. Add product \n","4. Update stock\n",
              "5. Delete product \n", 
              "6.Print Total value of all products in stock \n ", 
              "7. Apply Discount ny Tag \n","8.Exit")
        choice=int(input("\n Enter Choice: "))
        if(choice ==1):getallproducts()
        if(choice ==2): lowstockWarning()
        if (choice==3):addProduct()
        if(choice ==4):updatestock()
        if(choice ==5):deleteproduct()
        if(choice ==6):totalvalueofallprodinstock()
        if(choice ==7):discountbytags()
        if (choice==8):
            choice=0
            return      
menu()
    