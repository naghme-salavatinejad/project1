# ایا عدد زوج است یا فرد
# x=int (input("addad vared kon:"))
# if x%2 ==0:
#     print ("zowj")
# else:
#     print ("fard")

# سه عدد را بگیر آیا تشکیل اضلاع مثلث قایم الزاویه می دهند ؟ 
x = int (input( "number 1: "))
y = int (input( "number 2: "))
z = int (input( "number 3: "))
# if x**2 == (y**2 + z**2):
#     print ("ghaemozaviye ast")
# elif z**2 == (x**2 + y**2):
#     print ("ghaemozaviye ast")
# elif y**2 == (x**2 + z**2):
#     print ("ghaemozaviye ast")
# else:
#     print ("ghaemozaviye nist") 

# max_number = x
# if max_number < y:
#     max_number = y
# if max_number < z:
#     max_number = z
# print (max_number)

if  x**2 == y**2 + z**2 or y**2 == x**2 + z**2 or z**2 == y**2 + x**2 :
    print ("yes")
else :
    print ("no")
