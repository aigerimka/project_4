lst_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
const_letters = ['с', 'б', 'з', 'ф', 'к']

while 1:
    text = input('Введите текст(0 = выход, 1 = обратный перевод)):')
    if text == '0':
        break
    elif text == '1':
        text = input('Введите текст для обратного перевода:')
        while 1:
            letter = input('Введите согласную (с/б/з/ф/к):')
            if letter in const_letters:
                for char in lst_letters:
                    text = text.replace(char+letter+char.lower(), char)
                print(text)
                print('')
                break
            else:
                print('Введите букву из списка!')
                continue
    else:
        while 1:
            letter = input('Выберите согласную (с/б/з/ф/к):')
            if letter in const_letters:
                for char in lst_letters:
                    text = text.replace(char, char+letter+char.lower())
                print(text)
                print('')
                break
            else:
                print('Введите букву из списка!')
                continue