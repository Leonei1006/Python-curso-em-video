#o objetivo desse programa e transformar metros em centímetros e milímetros
m = float(input("Metros: "))
cm = m * 100
mm = m * 1000
print('{} metros equivalem à {:.0f} centímetros e {:.0f} milímetros.'.format(m, cm, mm))

