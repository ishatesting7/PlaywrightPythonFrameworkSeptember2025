# 
demofruit = ["apple", 23, "banana", 45.6, "cherry", True]
print(type(demofruit))

for itemdemo in demofruit:
    print(itemdemo)
    print(type(itemdemo))

for j in range(5):
    print("Iteration number:", j) # 0 to 4
    
# Looping through a list of fruits and printing each item
fruits = ["apple", "banana", "cherry"] 
print(type(fruits))
for fruit in fruits:
    print(fruit)# Looping through a range of numbers from 0 to 4 and printing each number

    
# While Loop

count = 1
while count <= 20:
    print(" 20 X ", count, "=", 20 * count)
    #count = count + 1
    count +=1

    
# page locator - .classname

# count = await page.locator(".classname").count()
# for i in range(count):
#     text = await page.locator(".classname").nth(i).text_content()
#     print(text)

# API 
# if you know the count - then go for for loop
# if you don't know the count - then go for while loop