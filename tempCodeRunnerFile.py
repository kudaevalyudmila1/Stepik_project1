import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_'
chars = ''

count = int(input(('Сколько паролей сгенерировать? ')))
len_chars = int(input('Введите длину одного пароля: '))
numbers = input('Включать ли цифры 0123456789? Введите:да или нет: ')
simbol_up = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите:да или нет: ')
simbol_low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите:да или нет: ')
simbol_special= input('Включать ли символы !#$%&*+-=?@^_? Введите:да или нет: ')
simbol_suncertain = input('Исключать ли неоднозначные символы il1Lo0O? Введите:да или нет:')
if numbers in 'да':
    chars += digits
if simbol_up in 'да':
    chars += uppercase_letters
if simbol_low in 'да':
    chars += lowercase_letters
if simbol_special in 'да':
    chars += punctuation
     
for i in range(1, count + 1):
    chars1 = ''
    for j in range(len_chars):
        chars1 += random.choice(chars)
        if simbol_suncertain in 'да':
            for c in 'il1Lo0O': 
                chars1 = chars1.replace(c, '') 
    print(chars1, sep='') 