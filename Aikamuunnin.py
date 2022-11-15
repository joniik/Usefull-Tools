# Aikamuunnin Tht
true = 1
while true == 1:
    tunti = int(input("Anna tuntimäärä : "))

    def paiva():
        paiva = tunti / 24
        paivavas = round(paiva,3)
        print (tunti, "tuntia on" ,paivavas , "Päivää ")

    def minuutti():
        minuutti = tunti * 60
        print (tunti, "tuntia on" ,minuutti , "Minuuttia")
        
    def sekuntti():
        sekuntti = tunti * 3600
        print (tunti, "tuntia on" ,sekuntti , "Sekunttia ")
        
    def millisekuntti():
        millisekuntti = tunti * 72000
        print (tunti, "tuntia on" ,millisekuntti , "Millisekunttia ")

    aikamuoto = input("Anna aikamuoto (pv , min , sec , msec) : ")

    if aikamuoto == "pv":
        paiva()
        
    if aikamuoto == "min":
        minuutti()
        
    if aikamuoto == "sec":
        sekuntti()
        
    if aikamuoto == "msec":
        millisekuntti()
      
    else:      
        uudelleen = input("Uudelleen ? y/n : ")
        
        if uudelleen == "y":
            true = 1
            
        if uudelleen == "n":
            true = 0
