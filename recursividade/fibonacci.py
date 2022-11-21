def recursao_fibonacci(n):
    if n > 1:
        return recursao_fibonacci(n-1) + recursao_fibonacci(n-2)
    return n

while True:
    print("=-="*40)
    print("• Calculadora de Fibonacci • ")
    print("=-="*40)
    print("• Quer calcular a sequência de Fibonacci por recursão ou iteração?")
    print("[1] RECURSÃO  [2] ITERAÇÃO [3] SAIR")
    option = int(input("• DIGITE A OPÇÃO: "))
    print("=-="*40)
            
    if option == 1:
        num = int(input("• Digite o número de termos da sequência: "))
        for c in range(num):
            print(f"{recursao_fibonacci(c)}, ", end='')
        sn = int(input("     ► Quer continuar? [1] para SIM [2] NÃO: "))
        if sn == 1:
            continue
        elif sn == 2:
            print("TCHAU!")
            break  
        
    if option == 2:
        num = int(input("• Digite um número de termos para a sequencia: "))
        termo_1 = 0
        termo_2 = 1
        print('=-='*40)
        print(f"{termo_1} , {termo_2}", end='')
        contador = 3
        while contador <= num:
            termo_3 = termo_1 + termo_2
            print(f', {termo_3}', end='')
            # faz a transição de termos, vai andando e vai somando no t3
            termo_1 = termo_2
            termo_2 = termo_3
            contador += 1
        sn = int(input("     ► Quer continuar? [1] para SIM [2] NÃO: "))
        if sn == 1:
            continue
        elif sn == 2:
            print("TCHAU!")
            break   
        
    if option == 3:
        print("TCHAU!")
        break
        
 

        
























