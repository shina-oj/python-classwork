#find x if 4= 2x + 5
x = (4-5)/2
print(x)

#find the area of a triangle using herons formula if a=5, b=7 c= 10
a=5
b=7
c=10
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5
#simplifying

j=(s-a)
k=(s-b)
l=(s-c)
m=(s*j*k*l)
n=m**0.5
print(n)