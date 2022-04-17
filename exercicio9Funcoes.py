
def media_conceito(nota):
    
    #print(f' A nota é:  {nota}')
    if nota >= 0.0 and nota <= 4.9:
        print(f'Sua nota é: {nota} e seu conceito é: D')
    elif nota >= 5.0 and nota <= 6.9:
        print(f'sua nota é: {nota} e seu conceito é: C')
    elif nota >= 7.0 and nota <= 8.9:
        print(f'Sua nota é: {nota} e seu conceito é: B') 
    elif nota >= 9.0 and nota <= 10:
        print(f"Sua nota é: {nota} e seu conceito é: A") 
media_conceito(7.7)