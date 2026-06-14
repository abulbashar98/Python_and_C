# *args allow you to pass multiple non-key arguments
# **kwargs allow you to pass multiple keyword arguments

# 1.positional 2.default 3.keyword 4. ARBITRARY


# 1️⃣
#def shipping_labe(*args, **kwargs):
#   for arg in args:
#        print(arg, end=" ")
#    print()

#    for value in kwargs.values():
#        print(value, end=" ")    

#Note: positional arguments must be passed before keyword arguments
#shipping_labe("Mr","Spongebob","Squarepants","III",street="123fakestreet",city="Detroit",state="MI",Zip="54321")


# 2️⃣
 
#def shipping_labe(*args, **kwargs):
#   for arg in args:
#        print(arg, end=" ")
#   print()

#   for key, value in kwargs.items():
#        print(f"{key}: {value}", end=" ")

#Note: <dictionary-name>.itemms() hold both key value pairs in python

#shipping_labe("Mr","Spongebob","Squarepants","III",       street="123fakestreet",
#city="Detroit",
#state="MI",
#Zip="54321")



# 3️⃣
 
def shipping_label(*args, **kwargs):
   for arg in args:
        print(arg, end=" ")
   print()
   
   if 'apt' in kwargs:
       print(kwargs.get('street'), kwargs.get('apt'))
   elif 'poBox' in kwargs:
       print(f"{kwargs.get('street')} {kwargs.get('poBox')}")    
   else:
       print(kwargs.get('street'))
            
   print(f"{kwargs.get('city')} {kwargs.get('state')},{kwargs.get('Zip')}")



shipping_label("Mr","Spongebob","Squarepants","III",       street="123fakestreet",
apt="6A1",              
poBox="#10001",              
city="Detroit",
state="MI",
Zip="54321")

