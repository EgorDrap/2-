mutable_list=[1,2,3,(True),'Преподаватели отвечают быстро и объясняют понятно']
print(mutable_list)
mutable_list[0]=400
print(mutable_list)
mutable_list[3]=False
print(mutable_list)
mutable_list[4]='кодинг меня успокаивает'
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)
print(1 in mutable_list)
print(400 in mutable_list)
mutable_list.append('каждый урок становится сложнее и интреснее')
print(mutable_list)


immutable_var=tuple[(1,2,3,(True),'Проверяющий красавчик =)')] #Кортеж - неизменяем
print(immutable_var)
immutable_var[0]=2
print(immutable_var) # кортеж не поддерживает обращение по элементам
# кортеж используется для качественного хранения информации, которая занимает меньше памяти, и + мы можем каждый элемент доставать и работать
