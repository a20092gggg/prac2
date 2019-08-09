# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:47:01 2019

@author: t.g.c
"""

# 前面輸入的東西 numpy是數學套件，matplotlib是畫圖套件。
import numpy as np
import matplotlib.pyplot as plt
#設定參數、que=隨機數 、 b為使用者輸入
que = np.random.randint(10)
b = int(input("please key in the number from 0 to 10. \n >> "))

#判斷式迴圈:while，若達成while上的條件，則會重複執行迴圈中的東西!
while b != que:     #若b不等於 que 則...
    print("\nWrong, please do it again. \n ")       #印出"錯誤"
    b = int(input("please key in the number from 0 to 10. \n >> "))     #並要求使用者重新輸入b
else:               #若非上面的條件的話(即 que = b)，則...
    print("\nNice try. you got the answer.")        #印出答案正確，並跳出迴圈
    
    