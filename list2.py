#Создайте словарь:
citytmp = {
    'city' : 'Москва',
    'temperature' : '20',
}

#Выведите на экран значение ключа city
print(citytmp['city'])

#Уменьшите значение "temperature" на 5
citytmp['temperature'] = int(citytmp['temperature']) - 5 

#Выведите на экран весь словарь
print(citytmp)

#Проверьте, есть ли в словаре ключ country
print(citytmp.get('country'))

#Выведите значение по-умолчанию "Россия" для ключа country
print(citytmp.get('country', 'Россия'))

#Добавьте в словарь элемент date со значением "27.05.2019"
citytmp['date'] = "27.05.2019"

#Выведите на экран длину словаря
print(len(citytmp))