# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:39:51 2019

@author: t.g.c
"""

import numpy as np
import matplotlib.pyplot as plt

#進階版
a1, a2, a3, a4 = np.random.randint(10),np.random.randint(10),np.random.randint(10),np.random.randint(10)

#4個數字不重複
while a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
    a1, a2, a3, a4 = np.random.randint(10),np.random.randint(10),np.random.randint(10),np.random.randint(10)

k = [str(a1),str(a2),str(a3),str(a4)]
b = list(input("請輸入4個不同的數字。 \n>> "))

while b[0] == b[1] or b[0] == b[2] or b[0] == b[3] or b[1] == b[2] or b[1] == b[3] or b[2] == b[3]:
    print("請不要重複 \n")
    b = list(input("請輸入4個不同的數字。 \n>> "))
    


while b[0] != k[0] or b[0] != k[1] or b[0] != k[2] or b[0] != k[3]:
    #2A2B
    if (b[0] == k[0]) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("2A2B")   #AABB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("2A2B")   #ABAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("2A2B")   #ABBA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("2A2B")   #BAAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("2A2B")   #BABA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] == k[3]):
        print("2A2B")   #BBAA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #1A3B
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A3B")   #ABBB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A3B")   #BABB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A3B")   #BBAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("1A3B")   #BBBA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #4B
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("4B")   #BBBB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #3A
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] == k[2]) and (b[3] == k[3]):
        print("3A")   #XAAA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] == k[2]) and (b[3] == k[3]):
        print("3A")   #AXAA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] == k[3]):
        print("3A")   #AAXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] == k[1]) and (b[2] == k[2]) and (b[3] not in k):
        print("3A")   #AAAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #2A1B
    elif (b[0] == k[0]) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("2A1B")   #AABX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("2A1B")   #AAXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] not in k ):
        print("2A1B")   #ABAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("2A1B")   #AXAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] == k[3]):
        print("2A1B")   #ABXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("2A1B")   #AXBA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] == k[2]) and (b[3] not in k):
        print("2A1B")   #BAAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("2A1B")   #XAAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] == k[3]):
        print("2A1B")   #BAXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("2A1B")   #XABA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k) and (b[2] == k[2]) and (b[3] == k[3]):
        print("2A1B")   #BXAA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] == k[3]):
        print("2A1B")   #XBAA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #1A2B
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("1A2B")   #ABBX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] not in k) and (b[3] in k and b[3] != k[3]):
        print("1A2B")   #ABXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] not in k):
        print("1A2B")   #BBAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A2B")   #AXBB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] == k[3]):
        print("1A2B")   #BBXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("1A2B")   #BXBA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("1A2B")   #BABX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A2B")   #XABB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("1A2B")   #BAXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("1A2B")   #XBBA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A2B")   #BXAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A2B")   #XBAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #3B
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("3B")   #XBBB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("3B")   #BXBB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("3B")   #BBXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("3B")   #BBBX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #2A
    elif (b[0] == k[0]) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] not in k ):
        print("2A")   #AAXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] == k[2]) and (b[3] not in k ):
        print("2A")   #AXAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] not in k ) and (b[3] == k[3]):
        print("2A")   #AXXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] == k[3]):
        print("2A")   #XAXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] == k[2]) and (b[3] not in k):
        print("2A")   #XAAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] == k[2]) and (b[3] == k[3]):
        print("2A")   #XXAA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #1A1B
    elif (b[0] == k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] not in k):
        print("1A1B")   #ABXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("1A1B")   #AXBX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] not in k ) and (b[3] in k and b[3] != k[3] ):
        print("1A1B")   #AXXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] not in k ):
        print("1A1B")   #XABX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("1A1B")   #XAXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] not in k) and (b[2] == k[2]) and (b[3] in k and b[3] != k[3]):
        print("1A1B")   #XXAB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] not in k):
        print("1A1B")   #BAXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k ) and (b[2] == k[2]) and (b[3] not in k ):
        print("1A1B")   #BXAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k ) and (b[2] not in k ) and (b[3] == k[3]):
        print("1A1B")   #BXXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] == k[2]) and (b[3] not in k):
        print("1A1B")   #XBAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] not in k) and (b[3] == k[3]):
        print("1A1B")   #XBXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] == k[3]):
        print("1A1B")   #XXBA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #2B
    elif (b[0] in k and b[0] != k[0]) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] not in k ):
        print("2B")   #BBXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] not in k ):
        print("2B")   #BXBX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k ) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("2B")   #BXXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("2B")   #XBXB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("2B")   #XBBX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] in k and b[3] != k[3]):
        print("2B")   #XXBB
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #1A
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] not in k ) and (b[3] == k[3]):
        print("1A")   #XXXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] == k[2]) and (b[3] not in k):
        print("1A")   #XXAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] == k[1]) and (b[2] not in k ) and (b[3] not in k ):
        print("1A")   #XAXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] == k[0]) and (b[1] not in k ) and (b[2] not in k ) and (b[3] not in k ):
        print("1A")   #AXXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #1B
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] not in k ) and (b[3] in k and b[3] != k[3]):
        print("1B")   #XXXA
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] in k and b[2] != k[2]) and (b[3] not in k):
        print("1B")   #XXAX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] not in k ) and (b[1] in k and b[1] != k[1]) and (b[2] not in k ) and (b[3] not in k ):
        print("1B")   #XAXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    elif (b[0] in k and b[0] != k[0]) and (b[1] not in k ) and (b[2] not in k ) and (b[3] not in k ):
        print("1B")   #AXXX
        b = list(input("請輸入4個不同的數字。 \n>> ")) 
    #0123
    elif (b[0] not in k ) and (b[1] not in k ) and (b[2] not in k ) and (b[3] not in k ):
        print("0")   #XXXX
        b = list(input("請輸入4個不同的數字。 \n>> "))        
    else:
        print("bingo")
        break
    

    