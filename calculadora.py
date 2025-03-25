print('=-'*10)
print('''    calculadora''')
print('=-'*10)
while True:
  try:
    n1 = float(input('\ndigite um numero para calcular:'))
    n2 = float(input('\ndigite outro numero:'))

    print()
    calculos =[
        '[+]',
        '[-]',
        '[*]',
        '[/]',
        '[%]', ]
    print(calculos)

    prg = str(input('\ndigite uma das opções acima:')).lower().strip()

    if prg =='+':
        print(f'\n{n1} + {n2} = {n1 + n2}')

    if prg == '-':
        print(f'\n{n1} - {n2} = {n1 - n2}')
        
    elif prg == '*':
        print(f'\n{n1} * {n2} = {n1 * n2}')

    elif prg == '/':
        if n2  == 0:
           print('\nnao se divide com zero')
        else:
         print(f'\n{n1} / {n2} = {n1 / n2}')

    elif prg == '%':
        if n2  == 0:
           print('\nzero n é permitido nessa opção')
        else: 
         print(f'\n{n1} % {n2} = {n1 % n2}')

    perg = str(input('\n deseja continuar? S/N:')).lower().strip()
  
    if perg == 's':
     print('=-'*13)
     print('  continuando os calculos')
     print('=-'*13)
     continue

    elif perg == 'n':
     print('=-'*12)
     print('    fim dos calculos')
     print('=-'*12)
     break
    
  except ValueError:
    print('\nVALORES INVALIDOS!!')