frase = input('frase: ').lower().strip()
print('A letra "A" aparece' , frase.count('a') , 'vezes')
print('inicialmente aparece na', frase.find('a') + 1 ,'posição')
print('a ultima vez q aparece é na posição {}'.format(frase.rfind('a') + 1))
