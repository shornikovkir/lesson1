number=[3,5,7,9,10.5]
print(number)
number.append('Python')
print(number)
print (len(number))
print(number[1:4])
del number[-1]
print(number)

city_stat = {"city": "Москва", "temperatura": "20"}
print(city_stat["city"])
city_stat["temperatura"]=int(city_stat["temperatura"])-5
city_stat["temperatura"]=str(city_stat["temperatura"])
print(city_stat)
city_stat['country']='Россия'
print(city_stat)
city_stat['date']='27.05.2019'
print(city_stat)

