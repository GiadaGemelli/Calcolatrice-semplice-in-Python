from math import sqrt, exp

# Tabella per le operazioni disponibili:

hello = """
Ciao, benvenuto nella calcolatrice!

Ecco un elenco delle operazioni disponibili:

Addizione: Se vuoi sommare due numeri, digita 'addizione' o '+'
Sottrazione: Se vuoi sottrarre due numeri, digita 'sottrazione' o '-'
Moltiplicazione: Se vuoi moltiplicare due numeri, digita 'moltiplicazione' o '*'
Divisione: Se vuoi dividere due numeri, digita 'divisione' o '/'
Potenza: Se vuoi elevare un numero a una potenza, digita 'potenza' o '**'
Radice quadrata: Se vuoi calcolare la radice quadrata di un numero, digita 'radice' o 'sqrt'
Calcolo esponenziale: Se vuoi calcolare l'esponenziale di un numero, digita 'esponenziale' o 'exp'

Per uscire, digita 'esci' o 'ESC'
"""
while True: 
    print(hello)

    calcolo = input("Quale operazione vuoi eseguire? ")
    

    if calcolo == "addizione" or calcolo == "+":
        print("Hai scelto l'addizione!")
        a= float(input("Inserisci il primo numero: "))
        b= float(input("Inserisci il secondo numero: "))
        
        print("Il risultato è: " + str(a+b))

    elif calcolo == "sottrazione" or calcolo == "-":
        print("Hai scelto la sottrazione!")
        a= float(input("Inserisci il primo numero: "))
        b= float(input("Inserisci il secondo numero: "))
        
        print("Il risultato è: " + str(a-b))

    elif calcolo == "moltiplicazione" or calcolo == "*":
        print("Hai scelto la moltiplicazione!")
        a= float(input("Inserisci il primo numero: "))
        b= float(input("Inserisci il secondo numero: "))
        
        print("Il risultato è: " + str(a*b))

    elif calcolo == "divisione" or calcolo == "/":
        print("Hai scelto la divisione!")
        a= float(input("Inserisci il primo numero: "))
        b= float(input("Inserisci il secondo numero: "))
        
        if b == 0:
            print("Errore: non è possibile dividere per zero!")
        else:
            print("Il risultato è: " + str(a/b))
    
    elif calcolo == "potenza" or calcolo == "**":
        print("Hai scelto la potenza!")
        a= float(input("Inserisci il numero: "))
        b= float(input("Inserisci la potenza: "))
        
        print("Il risultato è: " + str(a**b))

    elif calcolo == "radice" or calcolo == "sqrt":
        print("Hai scelto la radice quadrata!")
        a= float(input("Inserisci il numero: "))
        
        if a < 0:
            print("Errore: non è possibile calcolare la radice quadrata di un numero negativo!")
        else:
            print("Il risultato è: " + str(sqrt(a)))
    
    elif calcolo == "esponenziale" or calcolo == "exp":
        print("Hai scelto il calcolo esponenziale!")
        a= float(input("Inserisci il numero: "))
        
        print("Il risultato è: " + str(exp(a)))
    
    elif calcolo == "esci" or calcolo == "ESC":
        print("Grazie per aver usato la calcolatrice! Arrivederci!")
        break


    new_calcolo = input("\nVuoi eseguire un'altra operazione? (y/n) ")
    if new_calcolo == "y" :
        print("Ritorno al menù principale!\n")
        continue
    else:
        print("Grazie per aver usato la calcolatrice! Arrivederci!")
        break
    

       
   
