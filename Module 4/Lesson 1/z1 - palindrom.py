def palindrom(stroka):
    if stroka.lower() == stroka[::-1].lower():
        print(f'Слово {stroka} является палиндромом')
        return True
    print(f'Слово {stroka} не является палиндромом')
    return False

palindrom('Батарейка')
palindrom('Казак')
palindrom('лепсспел')
palindrom('helloworld')
