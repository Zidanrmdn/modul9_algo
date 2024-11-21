# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:23:26 2024

@author: ASUS
"""

def pjumlah(angka=0, jumlah=0, i=1):
    if(jumlah<=0):
        return 0
    else:
        angka=float(input("masukan bilangan ke-"+str(i)+": "))
        if (jumlah==1):
            return angka
        else:
              i+=1
              return angka+pjumlah (angka,jumlah-1,i)
       
        
tot=int(input("masukkan jumlah: "))
nilai=pjumlah(jumlah=tot)
print("hasil: " + str(nilai))


