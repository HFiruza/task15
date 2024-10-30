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

#Добрый день. Решили практически верно, но нужно сохранить подходящие пары в виде строки. Дорабатывая ваш код, можно получить

#def generate_password(n):
#result = ""
#for i in range(1, n):
    #for j in range(i + 1, n):
        #if (i + j) <= n and n % (i + j) == 0:
            #result += str(i) + str(j)
        #return result
#n = int(input("Введите число от 3 до 20: "))
#password = generate_password(n)
#print("Пароль:", password)
