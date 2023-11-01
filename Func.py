#Through this Python code, we will show some simple
#implementation of certain functions

#First, we are going to make a small program using lambda function

add_2 = lambda x,y:x+y
sub_2 = lambda x,y:x-y
mul_2 = lambda x,y:x*y
div_2 = lambda x,y:x/y
check_age = lambda x:True if x>18 else False

print(add_2(3,5))
print(sub_2(3,5))
print(mul_2(3,5))
print(div_2(3,5))
print(check_age(40))

#Now, let's use the map() function to create a simple money conversion program
#We will convert from Indian currency to Korean Currency
#Conversion Rate => 1Rs=16.21won

store=[("Capri",200),
       ("Jeans",250),
       ("Shirt",500)]

#Let's create a Lambda function
to_won=lambda x:(x[0],x[1]*16.21)

final_cost=list(map(to_won,store))

print(final_cost)

#Now,we will write a small program using the filter() function

friends = [("Chandler",22),
           ("Ross",21),
           ("Joey",16),
           ("Phoebe",15),
           ("Monica",20),
           ("Rachel",24)]

#Let's create a lambda function
voting_age = lambda x:x[1]>18
filtered_set = list(filter(voting_age,friends))
print(filtered_set)

#Now,let's create a small program using the reduce funnction
#It is important to know that before implementing these 
#functions,you must import the functools library and 
#that reduce function returns only one value

import functools
letters=["H","E","L","L","O"]
combine=functools.reduce(lambda x,y:x+y,letters)
print(combine)

#We can also use it to find factorial of certain small numbers
numbers=[5,4,3,2,1]
factorial=functools.reduce(lambda x,y:x*y,numbers)
print(factorial)


