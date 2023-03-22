from os import system
from time import sleep

cmd = 'mode 45, 16'
system(cmd)

def opc():
    system('cls')
    
    response = int (input ("\n\n\n\n\n\t1 - Ver a sequência de números\n\n\t2 - Sair\n\n\t==> "))

    
    if response == 1:
        while True:
            cmd = 'mode 149, 35'
            system(cmd)
            sleep(0.5)
            system('cls')
            initial = int (input ("\n\n\n\tDigite o número inicial da sequência:\t"))
            
            fim = int (input ("\n\n\tDigite o número final da sequência:\t"))
            
            sleep(1)
            system('cls')
            
            item = initial
            strI = "\n  ->  "

            if initial <= fim:
                while item <= fim:
                    strI = strI + "\t" + '{:>4}'.format(item)
                    item = item + 1
            else:
                while item >= fim:
                    strI = strI + "\t" + str(item)
                    item = item - 1
                
            print (strI)
            break
        
    elif response == 2:
        print ("\n\n\tTchau!")
        sleep (2)
        system ('cls')
        
    else:
        print ("\n\n\tDigite uma opção válida!")
        sleep(2)
        system('cls')
        return opc()
    
opc()