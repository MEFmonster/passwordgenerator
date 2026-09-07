import secrets
import string
def lenghtspassword():
        lenghts = int(input("Введите длину пароля\n"))
        return lenghts
def generatedpassword(lenght, chars):
    return ''.join(secrets.choice(chars) for _ in range(lenght))

def complexity():
    rezim = int(input("Выберите сложность:\n[1] Легкий пароль\n[2] Средний пароль\n[3] Сложный пароль\n"))
    lenght = lenghtspassword()
    if rezim == 1:
        chars = string.digits
    elif rezim == 2:
        chars = string.digits + string.ascii_letters
    elif rezim == 3:
        chars = string.digits + string.ascii_letters + string.punctuation
    else:
        print("Вы ввели неизвестный режим")
        return
    name = input("Введите название сервиса пароля")
    passwords = generatedpassword(lenght, chars)
    with open('password.txt','w', encoding='utf-8') as f:
         f.write(f"Сервис:{name}\nПароль:")
         f.write(passwords)
    print(passwords)

complexity()