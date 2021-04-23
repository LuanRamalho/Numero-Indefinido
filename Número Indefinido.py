#-*- coding:utf-8 -*-

class Números:
    def VetoresAlternativos():
        a = [0]*10000000
        
        print("Digite a quantidade de vetores a ser utilizado: ")
        qtd = int ( input())
        
        i = 1
        z = 0
        c = 1 

        while(i>0 and z<qtd):
            print("")
            
            print("Digite o ", c , "/",qtd,"Númmero Inteiro")
            a[z] = int (input())
            
            z = z + 1
            c = c + 1
            
            print("")
     
        print("")
    
        i = 0
        c = 1
        while(i<z):
            print(" ", c , " Númmero Inteiro: ",a[i])
            i = i + 1
            c = c + 1
        
        
        print("")
        
        maior = a[0]
        i = 1
        while(i<z):
            if (a[i] > maior):
                maior = a[i]
            i = i + 1
        
        
              
        print("Este é o maior número: ",maior)
        
        print("")
        
        menor = a[0]
        i = 1
        while(i<z):
            if (a[i] < menor):
                menor = a[i]
            i = i + 1    
        
        print("Este é o menor número: ",menor)
        
        
        
n = Números
n.VetoresAlternativos()
input()
        

