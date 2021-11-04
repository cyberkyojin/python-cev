ci = input('cidade: ').strip()

x = str(ci[:5].title() == 'Santo')

print(x.replace('True', 'Sim, tem Santo.'))