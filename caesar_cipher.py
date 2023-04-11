# Описание проекта: требуется написать программу,
# способную шифровать и дешифровать текст в
# соответствии с алгоритмом Цезаря.

def code(isx, k, abc):
    str=''
    for i  in range(len(isx)):
        if isx[i].upper() not in (abc):
            str +=(isx[i])
        if isx[i].upper() in (abc):
            c = abc[(abc.index(isx[i].upper()) + k) % len(abc)]
            if isx[i].isupper():
                str +=c.upper()
            else:
                str += c.lower()
    print(str)

def decode(isx, k, abc):
    str=''
    for i  in range(len(isx)):
        if isx[i].upper() not in (abc):
            str +=(isx[i])
        if isx[i].upper() in (abc):
            c = abc[(abc.index(isx[i].upper()) - k) % len(abc)]
            if isx[i].isupper():
                str +=c.upper()
            else:
                str += c.lower()
    print(str)

print('Приветствуем в  вас программе (де)шифрования.')
print('На каком языке (де)шифруем текст? Введите 1 - русский язык, 2 -  английский язык: ')
while True:
    n = int(input())
    if n == 1:
        abc1 = ('А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'.split())
        break
    elif n == 2:
        abc1 = ('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split()
        break
    else:
        print('Неверный язык (де)шифрования, повторите ввод:')
    
print('Введите текст для (де)шифрования: ')
isx1 = input()
print('Введите шаг (де)шифрования: ')
k1 =  int(input())
print('Если необходимо шифование, введите 0, если дешифрование, введите 00')
while True:
    m = input()
    if m == '0':
        code(isx1, k1, abc1)
        break
    elif m == '00':
        decode(isx1, k1, abc1)
        break
    else:
        print('Вы неправильно ввели вид шифрования, повторите ввод: ')
