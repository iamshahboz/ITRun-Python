# here we are saving pasword and balance
pin_code = 3045
balance = 80

max_attempts = 3
attempts = 0

# the system takes the password from user
print("Добро пожаловать, ставьте карту")
while attempts < max_attempts:
    user_pin_code = int(input("Введите пин код: "))
    attempts += 1 
    if user_pin_code == pin_code:
        cash_withdraw = int(input("Сколько вы хотите снять: "))
        if cash_withdraw <= balance:
            balance -= cash_withdraw
            print("Остаток на счете", balance, "сомони")
        else:
            print("У вас недостаточно средств")
        break
    else:
        if attempts < max_attempts:
            print("Неправильный пин код, повторите еще раз")
        else:
            print("Превишено количество попыток. Карта заблокировано")

    


