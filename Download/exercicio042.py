#tipos de triângulo
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Seguno segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Podemos formar um triângulo ' , end= (''))
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    if seg1 == seg2 != seg3 or seg1 == seg3 != seg2 or seg2 == seg3 != seg1:
        print('ISÓSCELES!')
    if seg1 != seg2 and seg2 != seg3:
        print('ESCALENO!')
else:
    print('NÃO PODEMOS FORMAR UM TRIÂNGULO!')
