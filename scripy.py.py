connectors = ['AND', 'OR', '<=>', '=>', 'NOT']

relation = input('Scrie relatia: ').upper().split(" ")

def check_relation(relation):
    index = 0
    #numar aparitie conectori
    con = 0
    #numar aparitie paranteza deschisa
    open_bracket = 0
    #numar aparitie paranteza inchisa
    closed_bracket = 0
    #urmareste relatia propozitie / conector
    prop_con = False
    #urmareste prima propozitie
    first_prop = True
    #urmareste ultima propozitie
    last_prop = False
    for char in relation:
        # numara aparitie paranteza deschisa
        if char == '(':
            # verifica daca inainte de paranteza deschisa apare propozitie
            if index != 0 and relation[index - 1] >= 'A' and relation[index - 1] <= 'Z' and len(relation[index - 1]) == 1:
                return False
            open_bracket += 1
            first_prop = True
            last_prop = False
            index += 1
            continue
        # numara aparitie paranteza inchisa
        elif char == ')':
            # verifica daca dupa paranteza inchisa exista un conector / paranteza inchisa, cu conditia sa nu ne aflam
            # pe ultima pozitie, adica len(relation) - 1
            if index != len(relation) - 1 and relation[index + 1] not in connectors and relation[index + 1] != ')':
                return False
            closed_bracket += 1
            first_prop = True
            last_prop = False
            index += 1
            continue
        # numara aparitie conector
        elif char in connectors:
            # verifica daca inainte de not exista o paranteza deschisa
            if char == 'NOT' and relation[index - 1] != '(':
                return False
            con += 1
            prop_con = False
            first_prop = False
            last_prop = True
            index += 1
            continue
        elif(char >= 'A' and char <= 'Z' and len(char) == 1):
            # verifica daca intre oricare doua propozitii exista un conector
            if prop_con == True:
                #daca nu exista returneaza False
                return False
            # verifica daca inainte de prima propozitie exista paranteza deschisa sau not
            if first_prop and relation[index - 1] != 'NOT' and relation[index - 1] != '(' or first_prop and index == 0:
                return False
            # verifica daca dupa ultima propozitie se inchide paranteza
            if last_prop and relation[index + 1] != ')':
                return False
            prop_con = True
            index += 1
            continue
        return False
    #daca numarul de aparitie al conectorilor este egal cu numarul de aparitie a parantezelor deschis / inchis
    #returneaza True
    #altfel returneaza False
    return open_bracket == con == closed_bracket


if check_relation(relation):
    print('Relatia este buna')
else:
    print('Relatia nu este buna')