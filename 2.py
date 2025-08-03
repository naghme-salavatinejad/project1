# x=input("enter 1st number:")
# y =input("enter 2nd number:")
# x=int(x)
# y=int(y)
# print(x+y)
# x = float (input("enter 1st number:"))
# y = float (input ("enter 2nd number:"))
# print( x , "+" , y , "=" , x+y)
# print( x , "-" , y , "=" , x-y)
# print( x , "*" , y , "=" , x*y)
# print( x , "/" , y , "=" , x/y)

# تعداد روز را بگیرد و تبدیل به سال و ماه و روز کند.
# total= int (input("enter total : "))
# h= total // 3600
# m= (total-(h*3600)) // 60
# s= total-((h*3600)+(m*60))
# print (h , "h " , m , "m " , s , "s ")

# روز ماه سال روز تولد و روز ماه سال امروز را بگیرد و سن را دقیقا چاپ کند
y0 = int ( input("enter sal tavalod : "))
m0 = int ( input("enter mah tavalod : "))
d0 = int ( input("enter rooz tavalod : "))
y1 = int ( input("enter sal alan : "))
m1 = int ( input("enter mah alan : "))
d1 = int ( input("enter rooz alan : "))
d = (((y1 * 365)+ (m1*30)+ d1)-((y0 * 365)+ (m0*30)+ d0))
print ("  sen shoma be rooz : " , d)
print ("  sen shoma be mah :" , d//30 , " mah va " , d % 30 , " rooz")
#print ("  sen shoma be mah : %s mah va %s rooz " % (d//30 , d%30))
#print (f"  sen shoma be mah :" , d//30 , " mah va " , d % 30 , " rooz")
print ("  sen shoma be sal :" , d//365 , " sal , " , (d % 365)// 30 , " mah ," , (d % 365) % 30 , "rooz")
