# -*- coding: utf-8 -*-
"""Final_Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14d3VAyeAdVT4vM_5NPIeKeYyb5sQxv3F
"""

class Yemek:
  __sebzeler=''

  def __init__(self,sebzeler={}):
    self.__sebzeler=sebzeler
    
  def SebzeYika(self,sebzeler):

    self.__sebzeler=sebzeler
    for sebze in sebzeler:
      print("{} iyice yıkanır.".format(sebze))

  def SebzeSoy(self):
    print("Yıkanan sebzeler soyulur.")

  def Dogra(self,sebzeler):
    self.__sebzeler=sebzeler
    for sebze in sebzeler:
      print("{} doğranır.".format(sebze))

  def MalzemeBirlestir(self):
    print("Malzemeler karıştırılıp tencereye alınır.")

  def Ekle(self,malzeme):
    self.__malzeme=malzeme
    print("{} tencereye eklenir.".format(malzeme))

  def Pisir(self,pisirmesuresi):
    self.__pisirmesuresi=pisirmesuresi
    print("{} pişirilir.".format(pisirmesuresi))


class HaslanmisTavuk(Yemek):
  def __init__(self):
    print("---Haşlanmış Tavuk Tarifi---")
    malzemeler=["3 adet havuç","3 adet patates","1 adet soğan","600 gr tavuk"]
    pisirmesuresi="30 dk"
    self.SebzeYika(malzemeler[0:2])
    self.SebzeSoy()
    self.Dogra(malzemeler[0:3])
    self.MalzemeBirlestir()
    self.Ekle(malzemeler[-1])
    self.Ekle("su")
    self.Ekle("tuz")
    self.Ekle("yağ")
    self.Pisir(pisirmesuresi)


class SebzeCorbasi(Yemek):
  def __init__(self):
    print("---Sebze Çorbası Tarifi---")
    malzemeler=["1 adet havuç","1 adet kabak","1 adet patates","1 adet soğan","un"]
    pisirmesuresi="5 dk"
    self.SebzeYika(malzemeler[0:3])
    self.SebzeSoy()
    self.Dogra(malzemeler[0:4])
    self.MalzemeBirlestir()
    self.Kavur(malzemeler[3])
    self.Ekle("su")
    self.Kavur(malzemeler[-1])
    self.Ekle("yağ")
    self.Ekle("tuz")
    self.Pisir(pisirmesuresi)

  def Kavur(self,malzeme):
    print("{} kavrulur.".format(malzeme))

class HavucTatlisi(Yemek):
  def __init__(self):
    print("---Havuç Tatlısı Tarifi---")
    malzemeler=["4 adet havuç","bisküvi", "4 adet ceviz","şeker","un","vanilya","süt","nişasta","hindistan cevizi"]
    pisirmesuresi="20 dk"
    self.__malzemeler=malzemeler
    self.SebzeYika(malzemeler[0:1])
    self.Parcala(malzemeler[2])
    self.Rendele(malzemeler[0])
    self.Pisir(pisirmesuresi)
    self.MalzemeBirlestir()
    self.MuhallebiYap(malzemeler)
    self.MalzemeBirlestir()
    self.SuslemeYap(malzemeler[-1])


  def Parcala(self,malzeme):
    print("{} parçalara ayrılır.".format(malzeme))

  def Rendele(self,malzeme):
    print("{} rendelenir".format(malzeme))

  def MuhallebiYap(self,malzemeler):
    print("{} {} {} {} {} kullanılarak muhallebi yapılır".format(malzemeler[3],malzemeler[4],malzemeler[5],malzemeler[6],malzemeler[7]))

  def SuslemeYap(self,malzeme):
    print("Üzeri {} ile süslenir.".format(malzeme))

if __name__ == '__main__':

  haslanmisTavuk=HaslanmisTavuk()
  print()
  sebzeCorbasi=SebzeCorbasi()
  print()
  havucTatlisi=HavucTatlisi()