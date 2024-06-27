# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:38:52 2024

@author: MUHARREM GEDİK
"""

#%%  default and flexible function

#default function: çember çevre hesabı: 2*pi*r
def cember_cevresi_hesapla(r,pi=3.14):
    """
        Amaç: Çember çevresi hesaplar.
        Parameter: r=yarıçap, pi=pi sayısı(default girili).
        Output: Çember Çevresi.
    """
    output = 2*pi*r
    return output

cember_cevresi_hesapla(2)



#flexible function : * ile kesin olmayan parametreleri dahil etmek için kullanılır.
def hesapla(boy,kilo,*a):
    """
        Amaç: Vücut kitle indexi hesaplar.
        Parameter: boy,kilo
        Output: kilo/(boy*boy)
    """
    print("Flexible parameters :"+str(a))
    output = kilo/(boy*boy)
    return output

hesapla(1.92,136,1,14,41,412,21)