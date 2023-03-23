'''Dosya Python içine alınmadan önce ilgili kütüphaler import edilir.Gerekli diğer kütüphaneler ilgili işlemden önce import edilecektir.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''Veri seti pandas kütüphanesi read methodu ile python'a aktarılır.'''

data=pd.read_csv('bodyfat.csv')
print(data)

'''Veri setinde bulunan değişkenlerden bağımlı ve bağımsız değişkenler belirlenir ve x ve y değişkenlerine atanır.X, nitelikler matrisi olup içinde 
bağımsız değişkenleri bulundururken y ise bağımlı dğişkenin olduğu vektördür.'''
X = data.iloc[:,1:].values
y = data.iloc[:,:1].values 

'''Oluşturulan dataframeler eğitim ve test olmak üzere 4' bölünür.Bu işlem hem bağımlı değişkenler için hem de bağımsız değişkenler için yapılır.Eğitim ve test için 
bölünen veri setinin %33'lük kısmı test için kullanılırken kalan kısmı eğitim için kullanılır.'''

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

'''Veri seti incelendiğinde bağımlı bir değişkenin birden fazla bağımsız değişken tarafından etkilendiği görülmektedir.Veri setinde yer alan veri tipleri sürekli
 değişken olup değişkenlerin arasında çoklu lineer regresyon modelinin uygulanması öngörülmektedir.Bir bağımlı değişken ile onu etkileyen birden fazla 
 bağımsız değişken arasındaki ilişkide çoklu lineer regresyon söz konudur.'''
from sklearn.linear_model import LinearRegression
mlr=LinearRegression()
egitim=mlr.fit(X_train, y_train)
tahmin=mlr.predict(X_test)

'''Çoklu lineer regresyon uygulandıktan sonra modelimizin başarısını ölçmek için R-square değeri kullanılabilir.R-square regresyon modellerinin başarısını ölçmede kullanılan 
analiz yöntemidir.Bu değer 0 ile 1 arasında bir değer alıp 1'e yaklaştıkça modelin performansının da iyi sonuç verdiği anlaşılmaktadır.'''

from sklearn.metrics import r2_score
r_2=r2_score(y_test,tahmin)
print(r_2)




