#Создайте функцию format_price, которая принимает один аргумент price
def format_price(price):
    #Приведите price к целому числу (тип int)
    price = int(price)
    #Верните строку "Цена: ЧИСЛО руб."
    return('Цена: '+str(price)+' руб')
#Вызовите функцию, передав на вход 56.24 и положите результат в переменную 
a = format_price(56.24)
#Выведите значение переменной с результатом на экран
print(a)