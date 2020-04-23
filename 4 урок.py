list_name1=['Вася','Петя','аня','васяк','петяк','аняк','васян','Петян','анян','васяг','петяг','аняг''васяс','петяс',
           'Аняй','Васяв','Петяв','Аняр','васяр','петяр','аняв','васяв','петяв','Аням']
# приводим все к заглавным буквам
list_name=list(map(str.title,list_name1))
print(list_name)
# формируем список из 100 случайных имен
from random import choices
def list_20(list_name, n):
    return choices(list_name,k=n)

name_100=list_20(list_name, n=100)
print(name_100)
# находим наиболее встречающееся слово
def common_name(name_100):
    dict_name={}
    for el in name_100:
        dict_name[el] = dict_name.get(el, 0) + 1
    dict_name =list(dict_name.items())
    dict_name.sort(key=lambda x:x[1],reverse=True)
    return dict_name[0][0]

print(common_name(name_100))
# ищем редко встречающуюся заглавную букву
def rare_letter(name_100):
    dict_letter={}
    for el in name_100:
        for letter in el[0]:
            dict_letter[letter]=dict_letter.get(letter,0)+1
    dict_letter=sorted(list(dict_letter.items()),key=lambda x:x[1])
    return dict_letter[0][0]
print(rare_letter(name_100))


