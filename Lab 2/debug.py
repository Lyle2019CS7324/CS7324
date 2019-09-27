from matplotlib import pyplot as plt
from PIL import Image
import seaborn as sns
import cv2

j = Image.open('./dataset/A/g/color_6_0036.png')
# print(i.size)
j = j.convert("L")
print(j)
i = cv2.imread('./dataset/A/g/color_6_0036.png')
# print(i.size)
# i = cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
# print(i.)
i = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

cv2.imshow('1',i)
cv2.waitKey()
print(i)
