import math
r=40e6/(2*math.pi) #Earth's radius in meters
h=float(input("What is your height in meters? "))
theta=math.acos(r/(r+h))
horiz=theta*r
km=horiz/1000
miles=horiz*100*(1/2.54)*(1/12)*(1/5280)
print("The horizon is %s km away (%s miles)"%(km,miles))