# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:33:37 2024

@author: MUHARREM GEDİK
"""

#%%

# shape => kaça kaçlık bir matris ekrana basar.
# reshape => matrisi yeniden sınırlandırmamızı sağlıyor.
# ndim => dimension bilgisini verir. boyut bilgisidir. 3,7'lik 2 boyutlu bir matrisimiz var şu an.
# dtype => Matrisimizdeki verilerin veri türlerini verir.
# size => Matrisimizde ne kadar veri olduğunun boyutunu yani sayısını verir.
# type => parantez içerisine yazılan değişkenin değerin hangi veri tipinde olduğunu geri döndürür.
# np.array => Numpy array oluşturmaya yarar.
# np.zeros => verilen shape boyutlarında tamamı 0 değerlerden oluşan array oluşturur.
# np.ones => verilen shape boyutlarında tamamı 1 değerlerden oluşan array oluşturur.
# np.empty => verilen shape boyutlarında tamamı 0'ın altında çok küçük değerlerden oluşan array oluşturur.
# np.arange => verilen başlangıç,bitiş,miktar değerleri ile başlangıç dahil, bitiş hariç olacak şekilde miktar kadar eklenerek bir array oluşturur.
# np.linspace => verilen başlangıç,bitiş,adet değerli ile başlangıç ve bitiş dahil olacak şekilde adet kadar rastgele sayıyla bir array oluşturur.

#%% Numpy Basics

import numpy as np

array1 = np.array([1,2,3,4,5,6,87,54,12,4,2,4,1,25,6,7,89,3,1325,5,6])
print(array1.shape)

array2 = array1.reshape(3, 7)
print("Shape: ",array2.shape)
print("Dimension: ",array2.ndim)
print("Data Type: ",array2.dtype)
print("Size: ",array2.size)
print("Array Type: ", type(array2))

#%% 3 boyutlu array oluşturma

array3 = np.array([[1,2,3,4],[5,6,7,8],[8,7,6,9]])
print(array3)
print("Shape: ",array3.shape)


#%% Zeros Array, Ones Array, Empty Array
# Amacı Daha sonra oluşabilecek ekleme işlemleri için en başta matrisde yer ayırtarak 0 değerleri basılır.
# Eğer daha sonra yeni bir veri eklenmek istenirse hafızayı yormak yerine 0 olan değer eklenmek istenen değer ile güncellenir.
#Empty Array içindeki sıfırın çok altında küçük değerler atanır 0 veya 1 yerine.

zeros = np.zeros((3,5))
print(zeros)

zeros[0,3] = 5
print(zeros)

#-------------------------

ones = np.ones((3,4))
print(ones)

ones[1,3] = 3
print(ones)

#-------------------------

empty = np.empty((3,3))
print(empty)

empty[2,1] = 5
print(empty)

#%% arange

# 10'dan başlayıp 50'ye kadar 5'er 5'er arttıracak ve 10 dahil 50 hariç olacak.
a = np.arange(10,50,5)
print(a)

#%% linspace

# 0'dan 10'a kadar olan sayılar arasından 20 adet rastgele sayıyı ekrana bas.
b = np.linspace(0, 10, 20)
print(b)
