#DONE BY: IVAN CELIS A01703860 MARLA GALVAN A01701180

numberOfVariable=int(input("Enter how many variables: "))
numberOfTerminals=int(input("Enter how many terminals: "))
numberOfRules=int(input("Enter how many rules: "))

rules = [[] for j in range(numberOfVariable)]

variable = []
terminals = []
rules = []

firstRules = []
secondRules = []
thirdRules = []
fourthRules = []
queue = []

# Python program to illustrate union 
# Without repetition  
def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

#ESCANEO DE LAS VARIABLES(NON-TERMINAL SYMBOLS)
print("-------SCANNING VARIABLES(NON-TERMINAL SYMBOLS)---------")
for i in range(0, numberOfVariable):
    print("Set variable "+str(i+1)+" :")
    n=str(input())
    variable.append(n.lower())
variable.append("3")
print(variable)

#ESCANEO DE LAS TERMINALES
print("-------SCANNING TERMINALS---------")
for i in range(0, numberOfTerminals):
    print("Set terminal "+str(i+1)+" :")
    n=str(input())
    terminals.append(n.upper())

print(terminals)

#ESCANEO INITIAL VARIABLE
acceptanceTerminal = str(input("Initial terminal:  "))
queue.append(acceptanceTerminal.upper())

#ESCANEO DE LAS REGLAS  
print("-------SCANNING RULES---------")
for i in range(0, numberOfRules):
    aux = []
    print("Which terminal use this rule: ")
    print(terminals)
    t=str(input())
    aux.append(t.upper())
    print("---Rule string: ---")
    print("list of variables: (3 for empty)")
    print(variable)
    n=str(input())
    aux.append(n)
    rules.append(aux)
print(rules)

#ESCANEO DE LAS REGLAS  
print("-------your STRING LENGHT 4---------")
stringue=str(input())

#     FUNCTION TO MAP index with rule
def manualJoin(listaX, listaY):
    aux1 = []
    if  len(listaX) > 0 and  len(listaY) > 0: 
        for letterX in listaX:
            aux1 = []
            for letterY in listaY:
                aux1.append(letterX+letterY)
        return aux1
    elif len(listaY) == 0 and len(listaX) > 0:
        return listaX
    elif len(listaY) > 0 and len(listaX) == 0:
    
        return listaY
    else:
 
        return listaY

#FUNCTION THAT RETURNS THE RULE OF THE FIRST CORRESPONDING TERMINAL
def firstCoincidence(lista, letter):
    for i in lista:
        if(i[0] == letter):
            casti = i[1]
            return casti

#FUNCTION THAT RETURNS THE TERMINAL OF THE FIRST CORRESPONDING RULE
def firstRuleCoincidence(lista, letter):
    for i in lista:
        if(i[1] == letter):
            casti = i[0]
            return casti
          
# FUNCTION TO get the rules string from join terminal
def findingAvailableRulesForJoin(terms):
    aux1 = []
    aux2 = []
    for j in terms:
        for i in rules:
            if(i[1] == j):
                aux1.append(i[0])
    aux2.append(aux1)
    return aux2


# FUNCTION TO get the terminal from the matching rule
def firstfindingAvailableRules(term):
    aux1 = []
    aux2 = []
    aux2.append(term)
    for i in rules:
        if(i[1] == term):
            aux1.append(i[0])
    aux2.append(aux1)
    return aux2

#FUNCTION TO get the terminal from the matching rule
def secondfindingAvailableRules(terms):
    aux1 = []
    aux2 = []
    aux2.append(terms)
    for letter in terms:
        aux1.append(firstCoincidence(firstRules, letter))
    aux2.append(aux1)
    return aux2

    
#FUNTION to find the accepatnce
def acceptance(terms):
    n = False
    if(len(terms) == 1):
        if(terms[0] == acceptanceTerminal):
            print("ACCEPTED")
        else:
            print("NOT ACCEPTED")
    else:
        for element in terms:
            for i in rules:
                if(element == acceptanceTerminal):
                    print("ACCEPTED")
                    n = True
                    break
                elif(i[0] == acceptanceTerminal and i[1] == element):
                    print("ACCEPTED")   
                    n = True
                    break
        if(n == False):
            print("NOT ACCEPTED")

       
    
        


print("-------LENGHT 1---------")
for letter in stringue:
    firstRules.append(firstfindingAvailableRules(letter))
print(firstRules)

print("-------LENGHT 2---------")
for letter in range(len(stringue)-1):
    aux3 = []
    aux1 = secondfindingAvailableRules(stringue[letter] + stringue[letter+1])
    aux3.append(stringue[letter] + stringue[letter+1])
    aux2 = aux1[1]
    auxSecondJoinCast = manualJoin(aux2[0], aux2[1])
    aux3.append(findingAvailableRulesForJoin(auxSecondJoinCast))
    secondRules.append(aux3)
print(secondRules)

print("-------LENGHT 3---------")
for letter in range(len(stringue)-2):
    regla = []
    list1 = {}
    list2 = {}
    regla.append(stringue[letter] + stringue[letter+1] + stringue[letter+2])

    aux1 = firstCoincidence(secondRules, stringue[letter+1] + stringue[letter+2])
    aux2 = manualJoin( firstCoincidence(firstRules, stringue[letter]), aux1[0] )
    list1 = findingAvailableRulesForJoin(aux2)

    aux3 = firstCoincidence(secondRules, stringue[letter] + stringue[letter+1])
    aux4 = manualJoin(aux3[0],  firstCoincidence(firstRules, stringue[letter+2]))
    list2 = findingAvailableRulesForJoin(aux4)
    regla.append(Union(list1[0], list2[0]))
    thirdRules.append(regla)
print(thirdRules)

print("-------LENGHT 4---------")
regla = []
list1 = []
list2 = []
list3 = []
aux1 = []
regla.append(stringue)

aux1 = firstCoincidence(thirdRules, stringue[1] + stringue[2]+ stringue[3])
aux2 = manualJoin(firstCoincidence(firstRules, stringue[0]), aux1[0])
list1 = findingAvailableRulesForJoin(aux2[0])

aux3 = firstCoincidence(secondRules, stringue[0] + stringue[1])
aux4 = firstCoincidence(secondRules, stringue[2] + stringue[3])
aux5 = manualJoin(aux3[0], aux4[0])
list2 = findingAvailableRulesForJoin(aux5)

aux6 = firstCoincidence(thirdRules, stringue[0] + stringue[1]+ stringue[2])
aux7 = manualJoin(firstCoincidence(firstRules, stringue[3]), aux6)
list3 = findingAvailableRulesForJoin(aux7)

union1 = []
union1 = Union(list1[0], list2[0])
union2 = Union(list3[0], union1)
print(union2)

acceptance(union2)

    




   
 


 
