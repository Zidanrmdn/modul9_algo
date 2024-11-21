# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:45:51 2024

@author: ASUS
"""

def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)

x = int(input("Masukan Nilai Angka : "))
y = int(input("Masukan Nilai Pangkat : "))

print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))