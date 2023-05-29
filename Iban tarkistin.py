tilinumero = input("Anna tilinumero : ")

testi = tilinumero.replace(" ","")

temp = testi[4:]+testi[:4]

temptili = ""

for kirjain in temp:
        if kirjain.isdigit():
            temptili += kirjain
        else:
            temptili += str(ord(kirjain) - ord("A") + 10)

jakojaanos = int(temptili) % 97

if jakojaanos == 1:
    print("-" * 75)
    print (tilinumero + "  (On kelvollinen tilinumero)")
    print("-" * 75)
else:
    print("-" * 75)
    print (tilinumero + "  (Ei ole kelvollinen tilinumero)")
    print("-" * 75)
