# MachineLearning-MultipleRegression

# MultipleRegression
## Vücut Yağ Oranı Analizi için Çoklu Doğrusal Regresyon Modeli
Bu proje kapsamında, birkaç bağımsız değişkene dayanarak vücut yağ yüzdesini tahmin etmek için çoklu doğrusal regresyon modeli oluşturmayı hedefliyoruz. Verilerimizi yükleme, işleme ve görselleştirme işlemleri için pandas, numpy ve matplotlib.pyplot kütüphanelerini kullanacağız. Ayrıca, verilerimizi eğitim ve test setlerine bölmek, çoklu doğrusal regresyon modelimizi oluşturmak ve model performansımızı R-kare metriği kullanarak değerlendirmek için sklearn kütüphanesini kullanacağız.

# Kütüphaneleri İçe Aktarma ve Verileri Yükleme
Verileri Python'a aktarmadan önce, import ifadesi kullanarak ilgili kütüphaneleri içe aktarıyoruz. Kodumuzda kullanmadan önce gerekli kütüphaneleri de içe aktarıyoruz. Bu projede pandas, numpy ve matplotlib.pyplot kütüphanelerini kullanacağız.

Verilerimizi daha sonra pandas kütüphanesinden read_csv yöntemini kullanarak yüklüyoruz ve veri çerçevesi oluşturuyoruz.

# Verileri Eğitim ve Test Setlerine Ayırma
Çoklu doğrusal regresyon modeli oluşturmak için verilerimizi eğitim ve test setlerine ayırmamız gerekiyor. sklearn kütüphanesinden train_test_split işlevini kullanarak verilerimizi ayırıyoruz. Verilerimizin %67'sini eğitim ve %33'ünü de test için kullanıyoruz.

# Çoklu Doğrusal Regresyon Modeli Oluşturma
Çoklu doğrusal regresyon modelimizi oluşturmak için sklearn kütüphanesinden LinearRegression işlevini kullanıyoruz. Modelimizi eğitim seti ile uygun hale getiriyoruz ve ardından test seti kullanarak tahminler yapıyoruz.

# Model Performansımızı Değerlendirme
Çoklu doğrusal regresyon modelimizin performansını değerlendirmek için R-kare metriğini kullanıyoruz. sklearn kütüphanesinden r2_score işlevini kullanarak R-kare değerini hesaplıyoruz, bu da modelimizin verilere ne kadar iyi uyduğunu ölçer. R-kare değeri 0 ile 1 arasında değişir ve daha yüksek değerler daha iyi model performansını gösterir.

Genel olarak, bu proje, sklearn kütüphanesini kullanarak çoklu doğrusal regresyon modeli oluşturmayı ve R-kare metriği kullanarak performansını değerlendirmeyi göstermektedir.
