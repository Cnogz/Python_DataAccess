# bağlantı için gerekli olan kütüphaneleri indiriyoruz. MongoClient ve bson.
from pymongo import MongoClient

# bson sayesinde objectid kodunu kullanabileceğiz.
from bson.objectid import ObjectId
import pymongo.mongo_client


# client = pymongo.MongoClient("localhost", 27017) => Bağlantıyı şu şekilde de kurabiliriz.

# Bağlantı kodları.
connection = MongoClient()

# Eğer veritabanı yoksa oluşturacaktır. Var ise onu seçecektir.
db = connection.FirstDB

# Hangi tabloda çalışıyor isek işlemi kısaltmak amacı ile db.Employees dediğimiz tabloyu Employees değişkeninde saklıyoruz.
# Eğer istersek db.Employees şeklinde devam edebilirdik.


Employees = db.Employees

# Entry altında json objemizi hazırlıyoruz.

age = 30
entry = {"Name": "Can",
         "LastName":"Oğuz",
         "Age": age}

# Tablomuza kaydımızı girmek için insert komutunu kullanıyoruz.
Employees.insert(entry)


# Girilen değeri ekranda görütülemek için tüm tabloyu bir liste halinde printliyoruz.
print(list(Employees.find()))

# Eğer istersek sadece bir kaydı find ile bulabilir ve görüntüleyebiliriz.

print(list(Employees.find({"Name":"Can"})))

# Güncelleme işlemleri
Employees.update_one({'_id':ObjectId("5ad5ef410404062768ad1078")},{'$set':{"Name":"OzanUpdated"}})


# Bağlantı silme işlemleri

# Eğer belirttiğimiz duruma uyan tüm kayıtları silmek istersek
silinenKisiler = Employees.delete_many({"Name":"Can"})
print(list(Employees.find()))

# Kaç kişi silindiğini almak için
print(silinenKisiler.deleted_count)

# Eğer tüm dökümanları silmek istersek
silinenKisiler = Employees.delete_many({})  # Kullanabiliriz.

# Bir koleksiyonu kaldırmak için
Employees.drop()  # Kullanabiliriz.

# Bağlantıyı connection.close() ile kapatabiliriz.

connection.close()
