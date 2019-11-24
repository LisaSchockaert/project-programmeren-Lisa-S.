# -*- coding: utf-8 -*-
"""
TEMPLATE VOOR PROJECT PROGRAMMEREN I (aj. 2019-2020)

Vul deze template aan (en dien deze in via indianio.ugent.be)

Groepsleden:    Groepslid 1: Jenne Leus
                Groepslid 2: Ine Pynebrouck
                Groepslid 3: Jiete Maertens
                Groepslid 4: Lisa Schockaert 

"""
import infoFun

########################################################
# -- Opdracht 1
########################################################

def temp_naar_getal_omzetten(strTemp):
    return str(int(float(strTemp) / 10)) 

sequentie = "" 
temperatuur = input("Geef een temperatuur: ")

while temperatuur != "STOP": 
    if 0 <= float(temperatuur) <= 79 :
        sequentie += temp_naar_getal_omzetten(temperatuur) 
        
    temperatuur = input("Geef een temperatuur: ")

print(" De sequentie is ", sequentie)



########################################################
# -- Opdracht 2
########################################################

def temp_naar_getal_omzetten(strTemp):
    return int(float(strTemp) / 10) 

def getal_naar_binairstr_omzetten(strGetal):
    return '{0:03b}'.format(int(strGetal))

def codeer_T_seq(temp): 
    sequentie= ""
    binair_str = ""
    
    for n in temp:
        if 0 <= float(n) <= 79 :
            sequentie += str(temp_naar_getal_omzetten(n))
    
    for i in sequentie: 
        binair_str += getal_naar_binairstr_omzetten(i) 
        
    return binair_str

print(codeer_T_seq([12.1]))
print(codeer_T_seq([5.6, 16.3]))
print(codeer_T_seq([26.3,34.6,38.9,40.0]))

########################################################
# -- Opdracht 3
########################################################

import infoFun 


def decodeer_bin_T_seq(bin_getal):
    gedecodeerde_str = ""
    for y in range(0, len(bin_getal), 3):
        gedecodeerde_str += str(int(bin_getal[y:y+3],2))

    return gedecodeerde_str 

print(decodeer_bin_T_seq('010011011100'))


Teller = 0
fouten_Teller = 0

lijst = infoFun.listRead('temperatuursequenties.txt')

for regel in lijst:
    Teller+=1
    reeks = regel.split() #splits lijn in decimale en binare gedeelde
    getallen_str = reeks[0]
    binair_str = reeks[1]
    
    if decodeer_bin_T_seq(binair_str) != getallen_str:
        print("Temperatuur-sequentie ", getallen_str , " werd fout gecodeerd.")
        fouten_Teller+=1
 
print("In totaal werden ", fouten_Teller," van de ", Teller, " sequenties fout gecodeerd.")


print(decodeer_bin_T_seq("001"))
print(decodeer_bin_T_seq("000001"))
print(decodeer_bin_T_seq("010011011100"))

########################################################
# -- Opdracht 4
########################################################

seq_list = ["36733675","1234224567", "535645567522402233202224"] # lijst met cijfer sequenties

sequentie=input("Geef een sequentie: ")

aantal_stijgingen = 0
vorige = None

for getal in sequentie :
        if vorige and int(getal) > int(vorige):
           aantal_stijgingen += 1 
        vorige = getal

print("sequentie: ", sequentie)
print("telt", aantal_stijgingen, "stijgingen")



########################################################
# -- Opdracht 5
########################################################
#functie om de temperaturen om te zetten naar een geheel getal
def temp_naar_getal_omzetten(strTemp):
    return int(float(strTemp) / 10) 

#functie om nummers om te zetten in de binare string
def getal_naar_binairstr_omzetten(strGetal):
    return '{0:03b}'.format(int(strGetal))

# Functie om de partiteitsbit te berekenen
def controleer_pariteit(binair_str):
    teller=0;
    for i in binair_str:
        teller+=int(i)
    return str(teller%2)

# functie om nummers om te zetten naar binarire string + parieteitsbit
def getal_naar_binair_omzetten_met_pariteit(strGetal):
    #converteel nummer naar binare string
    binair_omgezet = getal_naar_binairstr_omzetten(strGetal)
    #voeg er de pariteitsbit aan toe
    return controleer_pariteit(binair_omgezet) + binair_omgezet


def codeer_T_seq(temp): 
    sequentie= ""
    binair_str = ""
    
    for n in temp:
        if 0 <= float(n) <= 79 :
            sequentie += str(temp_naar_getal_omzetten(n))
    
    for i in sequentie: 
        binair_str += getal_naar_binair_omzetten_met_pariteit(i) 
        
    return binair_str 

def decodeer_bin_T_seq(bin_getal):
    gedecodeerd_str = ""
    # per stuk van 4
    for y in range(0, len(bin_getal), 4):
        # eerste getal parieit
        pariteit = bin_getal[y]
        #getal1-4
        binairGetal = bin_getal[y+1:y+4]
        getal = str(int(bin_getal[y+1:y+4],2))
        
        if pariteit != controleer_pariteit(binairGetal):
            gedecodeerd_str +='X'
        else:
           gedecodeerd_str += getal 

    #pariteit uit string vergelijken met de berekende pariteit

    return gedecodeerd_str 
    
######################################### 5a


print(codeer_T_seq_PB([12.1]))
print(codeer_T_seq_PB([5.6, 16.3]))
print(codeer_T_seq_PB([26.3,34.6,38.9,40.0]))

# hier komt het antwoord op opdracht 5.b

print(decodeer_bin_T_seq_PB("1001"))
print(decodeer_bin_T_seq_PB('010011011100'))
print(decodeer_bin_T_seq_PB("10100011001011001001", wrong_PB = "_"))
########################################################
# -- Opdracht 6
########################################################

import infoFun 


def verbeter_binair(lijst_foute_elementen):
    """
    Functie die we gebruiken om een missing bit te berekenen en toe te voegen
    
    Maar we gebruiken pariteit om de fouten te detecteren, we veronderstellen dat
    we de eerste bit en pariteit nog hebben, we voegen 0 of 1 toe zodat de
    pariteitsbit klopt. Er zijn meerdere oplossingen mogelijk, we kunnen die bit
    voor, tussen of na de missing bit plaatsen. Maar het zou ook kunnen dat de
    pariteitsbit miste. 
    """
    verbeterde_lijst = []
    verbeterde_lijst +=  lijst_foute_elementen  

    pariteit =  lijst_foute_elementen[0]
    parityCorruptedString = controleer_pariteit(''.join(map(str, lijst_foute_elementen[1:3])))           
    
    if (pariteit != parityCorruptedString):
        verbeterde_lijst.append('1')
    else:
        verbeterde_lijst.append('0') 
    
    return verbeterde_lijst


def lijst_naar_string_omzetten(list):
    """
    een lijsr naar een string omzetten
    """
    return ''.join(map(str, list))   


def controleer_pariteit(binair_str):
    """
    Functie die we gebruiken om de pariteit te controleren
    """
    teller=0;
    for i in binair_str:
        teller+=int(i)
    return str(teller%2)

def tel_missing_bits(binaire_getallen_str):
    """ 
    Functie die we gebruiken om de missing bits te tellen, 
    de lengte zou een veelvoud van 4 moeten zijn.
    
    Parameters
    ----------
    binaire_getallen_str : str
        De string met de binaire getallen
        
    """
    if (len(binaire_getallen_str)%4 != 0):
        return (4 - len(binaire_getallen_str)%4)
    else:
        return 0

def verbeter_binaire_getallen_str(binair_str, aantal_missing_bits):
    """
    Functie die missing bits toevoegt aan de string 
    
    Parameters
    ----------
    binair_str : str
        De string die verbeterd moet worden 
    aantal_missing_bits : int
        Het aantal missing bits in de string die verbeterd moet worden
    """
    
    verbeterde_binaire_lijst = []
    incorrecte_lijst = list(binair_str)
    
    while aantal_missing_bits > 0:

        pariteit = incorrecte_lijst[0] #eerste element is de pariteit
         # de volgende 3 elementen moeten we controleren met het eerste element
        te_controleren_string = lijst_naar_string_omzetten(incorrecte_lijst[1:4])
        if pariteit != controleer_pariteit(te_controleren_string):
            #print(lijst_naar_string_omzetten(incorrecte_lijst[0:4]) + ' incorrect')
            """
            als te_controleren_string incorrect is, dan zijn de eerste 3 elementen incorrect, 
            Het vierde is van het volgende deel
            probeer de eerste 3 elementen te verbeteren en te verwijderen van de incorrecte lijst 
            verhoog de incorrecte teller
            """
            verbeterde_binaire_lijst += verbeter_binair(incorrecte_lijst[0:4])
            del incorrecte_lijst[0:4]
            aantal_missing_bits -= 1
        else:
            #print(lijst_naar_string_omzetten(incorrecte_lijst[0:4]) + ' correct')
            """
            als te_controleren_string correct is, 4 elementen toevoegen aan te verbeteren lijst
            en 4 elementen verwijderen van de incorrecte lijst
            """
            verbeterde_binaire_lijst += incorrecte_lijst[0:5]
            del incorrecte_lijst[0:5]
        
      
    #all errors found add rest of list to the corrected list 
    verbeterde_binaire_lijst +=incorrecte_lijst

    #return lijst omgezet naar een string    
    return ''.join(map(str, verbeterde_binaire_lijst))   


Teller = 0
 
#test string 
#lijst_te_verbeteren_binaire_str = ['0000110010010110000001011100111100000000010100111011100110101101010011001010110101100000011110101001110011111001101011100101010100101011001011111111111111100111110101111101001010110110111110011001100101010011110010101100011000111100001101101111011011001100011000111001001110101100000011000110000011000000101001100011000001010110010101010000010111001111']
lijst_te_verbeteren_binaire_str = infoFun.listRead('missing_bits.txt')
lijst_verbeterde_binaire_str = []

for te_verbeteren_binaire_str in lijst_te_verbeteren_binaire_str:
    # Teller om de regels te tellen
    Teller += 1 
    # controleren hoeveel missing bits zich in de huidige regel bevinden
    missingBits = tel_missing_bits(te_verbeteren_binaire_str) 
    # Proberen de huidige lijn te verbeteren
    verbeterde_string = verbeter_binaire_getallen_str(te_verbeteren_binaire_str, missingBits) 
    # de verbeterde regel aan een lijst toevoegen, zodat we deze later in een bestand kunnen opslaan
    lijst_verbeterde_binaire_str.append(verbeterde_string) 
    #printen om te zien wat er gebeurd 
    print('regel ', Teller, 'heeft ',missingBits, 'missing bits, verbeterde string = ', correctedString) 
    # schrijf de verbeterde regels in een bestand met infoFun
    infoFun.listWrite("missing_bits_corrected.txt", lijst_verbeterde_binaire_str) # write list with corrected string to a file
    print('Alle verbeterde strings zijn in het bestand missing_bits_corrected.txt gezet')   


