def begin():
  print("try not to get cancelled")
  print("=======================")
  print("type alleen hoofdletter\n")
  spel()

def spel():
  Answer = (input("je ziet iemand lopen \nwat doe je?\n A) je zegt hallo meneer \n B) loopdoor \n")).upper()

  if Answer == ("B"): 
    print("goedzo het was geen man")
    ren()
  elif Answer == ("A"):
    print("het bleek geen man te zijn")
    cancelled()
  else:
    print("dat was geen keuse")
    spel() 
    

def cancelled():
  Answer = (input("GECANCELLED\n\ntype N om opnieuw te starten:")).upper()
  if Answer == ("N"): 
    begin()
  else: 
    print("dan niet")

def dood():
  Answer = (input("je bent dood\n\ntype N om opnieuw te starten:")).upper()
  if Answer == ("N"): 
    begin()
  else: 
    print("dan niet")

def ren():
  Answer = (input("je had honger dus je ging ergens heen om te eten \nwaar ga je heen?\n A) een vegan restaurant\n B) mc donalds \n")) .upper()
  if Answer == ("A"): 
    print("je rekening was hoog maar niemand heeft je gecancelled")
    vegan()
  elif Answer == ("B"):
    print("een blauwharige feminist komt op je af en zegt dat die kippen OOK EEN LEVEN HADDEN") 
    cancelled()
  else:
    print("dat was geen keuse")
    ren()

def vegan():
  Answer = (input("opweg naar huis loop je langs een steegje. \nje ziet dat er een meisje wordt lastig gevallen door een man \nhij ziet dat jij hem hebt gezien \nwat doe je nu?\n A) je rent keihard weg \n B) je gaat met hem vechten \n C) je gaat de man helpen om het meisje lastig te vallen\n")).upper()
  if Answer == ("A"): 
    print("ze hebben je beide gezien, het was op een beveiligings camera gefilmt en dat is online viral gegaan")
    cancelled()
  elif Answer == ("B"):
    print("") 
    vechten()
  elif Answer == ("C"):
    print("de politie kwam ze schoten de man. \nze weten nog niet wie je bent, dus je rent weg ") 
    politie()
  else:
    print("dat was geen keuse")
    vegan()

def vechten():
  Answer = (input("de man komt op je af met een vuist richting je gezicht \nwat doe je?\n A) je ontwijkt zijn slag en stomt hem in zijn maag \n B) je ontwijkt zijn slacht en stomt hem in zijn kruis \n")) .upper()

  if Answer == ("B"): 
    print("het werkte hij kan niet meer opstaan en geen kinderen meer krijgen jij bent nu een held")
    win()
  elif Answer == ("A"):
    print("hij nam de slacht en trapte je dood zwakkeling")
    dood()
  else:
    print("dat was geen keuse")
    vechten() 

def politie():
  Answer = (input("je rent zover als je kan maar je komt bij een splitsing \nwelke kant ga je op\n A) links\n B) rechts \n")).upper()
  if Answer == ("A"): 
    print("dit was een slechte keuze het was een doodlopende steeg en de politie heeft je dood geschoten")
    dood()
  elif Answer == ("B"):
    print("je heb geluk het eindigt in een drukke straat.\nje gaat op in de menigte en niemand weet ooit dat jij dat meisje heb lastig gevallen") 
    ontsnapt()
  else:
    print("dat was geen keuse")
    politie()

def win():
  Answer = (input("je heb het gevecht gewonnen de politie arresteert de man en het meisje is nu hopeloos verlieft op je \nwat nu? \n A) je wordt verlieft op het meisje\n B) je nergeert het meisje \n")).upper()
  if Answer == ("A"): 
    print("na een paar jaar trouw je met haar en ben jij heel gelukkig")
    gelukkig_eind()
  elif Answer == ("B"):
    print("je zal nooit iemand vinden een na 5 jaar pleeg je zelfmoord uit eenzaamheid") 
    dood()
  else:
    print("dat was geen keuse")
    win()

def ontsnapt():
  Answer = (input("paar maanden later kom je het meisje tegen in een bar \nze herkent je niet, je begint met haar te praten \n ga je haar vertellen dat JIJ haar heb lastiggevallen?\n A) ja\n B) nee\n")).upper()
  if Answer == ("A"): 
    print("iedereen is opeens stil en je word opgepakt door de beveiliging en gaat de gevangenis in")
    cancelled()
  elif Answer == ("B"):
    print("je vertelt het niet en ze wordt verliefd op je na een aantal jaar zijn jullie getrouwd") 
    leugen()
  else:
    print("dat was geen keuse")
    ontsnapt()

def gelukkig_eind():
  Answer = (input("je bent al jaren gelukkig getrouwt met een paar kinderen\nje kwam vaak in situaties waar je gecancelled had kunnen worden maar jij wist wat jij moest doen\n\njij hebt het spel gewonnen type N om nog een keer te spelen:")).upper()
  if Answer == ("N"): 
    begin()
  else: 
    print("dan niet")

def leugen():
  Answer = (input("je leeft in een leugen\nje bent al jaren getrouwd met een paar kinderen je weet niet wat je moet doen\n\njij hebt het spel gewonnen maar ook niet je leeft een leugen type NEE om nog een keer te spelen\nje weet niet wat je moet doen je leeft in een leugen type HELP:\n")).upper()
  if Answer == ("NEE"): 
    begin()
  elif Answer == ("HELP"):
    print("wat wie ben ik ik moet HULP ik ben getrouwd WIE BEN IK huh LEUGEN AHH wat hoe ehh HELP")
    huh()
  else: 
    print("HELP ME")

def huh():
  Answer = (input("je loopt naar het dak van het hoogste gebouw dat je kent om te springen want je weet het niet meer\nje vrouw probeert je tegen te houden\nwat nu???\n A) je neemt haar mee in de val\n B) je ontwijkt haar en springt zelf\n C) je vertelt dat jij haar hebt lastiggevallen\n")).upper()
  if Answer == ("A"):
    print("nu ben je dood en heb je je vrouw megenomen maar jij gaat naar een andere plek")
    dood()
  elif Answer == ("B"):
    print("nu ben je dood")
    dood()
  elif Answer == ("C"):
    print("WAT dit wou ik niet dit zou ZIJ nOOIT doen WAt")
    moord()

def moord():
  Answer = (input("je bent van het gebouw geduwt door je vrouw\n\njij hebt het spel misschien uitgespeeld ik weet het niet type N dit weer te doen val haar NIET lastig:")).upper()
  if Answer == ("N"): 
    begin()
  else: 
    print("dan niet")

begin()

