'''1. E-Commerce Order Analysis 
Problem Statement 
An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. '''

#creating order data
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]
#-----------------------------------------
#Task 1: To display all products costing more than ₹1000.
print("Products costing more than ₹1000 : ")
for record in orders:
    if record[1]>1000:
        print(record[0],record[1])
print("---------------------------------")
#Task 2: To find the most expensive product.
max_price=0
for record in orders:
    if record[1]>max_price:
        max_price=record[1]
        product=record[0]
print("Most Expensive Product : ",product,max_price)
print("---------------------------------")
#Task 3: To calculate the total order value.
total_value=0
for record in orders:
    total_value+=record[1]
print("Total Order Value : Rs ",total_value)
print("---------------------------------")
#Task 4: To count products costing below ₹1000.
count=0
for record in orders:
    if record[1]<1000:
        count+=1
        print("Products cost below ₹1000 : ",record[0],record[1])
print("Count of products costing below ₹1000 : ",count)
print("---------------------------------")  

