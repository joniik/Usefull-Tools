import random
import time

laskuri = 1
laskuri2 = 1 
kesken = 1
sanalista = ["kissa","koira","piraatti","kyllä","joo","kuu",
             "suihkuturbiini","koodari","käärme","pyyttoni",
             "kärppä","hyttynen","kitka","pitsa","viikatemies",
             "puuro","ei","miksi","auto","mopo","ulko-ovi","autotalli",
             "tietokone","kannettavatietokone","Elintarviketurvallisuusvirasto"
             "poliisi","aarni","aatto","joulu","ammattikoulu","prosessori","näytönohjain",
             "ralli","kulli","muovi","kirjasto","lasku","polkuvene"]
kirjoita = []
vastaus = []
slistapituus = len(sanalista) - 1

maara = int(input("kuinka monta sanaa? : "))

while laskuri <= maara:
    kirjoita.append (sanalista[random.randint(0,(slistapituus))])
    laskuri += 1
    
print (kirjoita)
print("N", end='\r', flush=True)
time.sleep(0.50)
print("Y", end='\r', flush=True)
time.sleep(0.50)
print("T", end='\r', flush=True)
time.sleep(0.50)
print("Nyt")
time.sleep(0.50)
# while laskuri2 <= laskuri:
start_time_1 = time.time()
x = input("").split(" ")
vastaus.extend(x)
end_time_1 = time.time()
#     laskuri2 += 1
aikasec = (end_time_1 - start_time_1)
aika = aikasec / 60
wpm = maara / aika
if vastaus == (kirjoita):
    print ("voitit")
    print ("Kirjoitit " + str(maara) + " sanaa " + (f'{aikasec:.2f}') + " sekunnissa")
    print ("Kirjoitus nupeutesi on " + (f'{wpm:.2f}') + "WPM")
    
else:
    print ("Et kirjoittanut oikein")
    print ("Kirjoitus nupeutesi on " + (f'{wpm:.2f}') + " WPM")
    