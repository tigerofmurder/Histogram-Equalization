import cv2
import numpy as np
from matplotlib import pyplot as plt

def sn(L,n,Pn):
	L = L-1
	Pr = 0
	for i in range(0,n,1):
		Pr += Pn[i]
	return L*Pr

def Pn(L,size,pn):
	for x in L:
	        pn.append(x/size)

imgc= cv2.imread('hist10_1.jpg')
img = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)


crop_img = img[280:280+110,172:172+88]

cv2.imshow('Coverted Image',crop_img)
cv2.waitKey(0)
plt.axis("on")

L = plt.hist(crop_img.ravel(),256,[0,256])[0]
print(L,"  ",len(L))
plt.show()

height, width = crop_img.shape
size = height * width

height, width = img.shape
print(size)

pn = []
Pn(L,size,pn)
S_n = []

for i in range (1,len(L)+1):
	S_n.append(int(sn(len(L),i,pn)))

print("size: ",S_n)
for y in range(0,width):
	for x in range(0,height):
		img[x,y] = S_n[img[x,y]]
cv2.imshow('Cted Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(img.ravel(),256,[0,256])[0]
plt.show()



