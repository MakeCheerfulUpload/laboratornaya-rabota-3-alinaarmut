import re


test_main = [
'Классное слово - обороноспособность, которое должно идти после слов: трава и молоко.',
'Король провел казнь на глазах у всех.',
'Ворон сидел и клевал кукурузу.',
'Молоко пьют с медом, но не пьют с печеньем.',
'В лес пришел жук и сел на пень.'
]

def test():
    for n in range(5):
        print(f' Результат теста {n + 1}')
        sogl = 'б-джай-нп-тф-ьь'
        reg = []
        glas = 'аеиоюуыёяэ'
        for i in range(len(glas)):
            reg.append('[' + sogl + ']*(?:' + glas[i] + '[' + sogl + ']+)*' + glas[i] + '[' + sogl + ']*')
        match = re.findall(r'\b('+"|".join(reg)+r')\b', test_main[n], re.I)
        match.sort(key=len)
        for word in match:
            print(word)
        print()

test()