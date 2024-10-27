def password(number):
    pass_ = ""
    for i in range(1,number):
        for j in range(i + 1,number):
            if number % (i + j) == 0:
                pass_ += format(str(i) + str(j))
        return f'{number} - {pass_}'

number = int(input("Введите ваше число: "))
result = password(number)
print(result)
