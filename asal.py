top = 0
y = int(input('bir sayı gir:'))
for a in range(2,y):
    if y%a == 0:
        print('sayı asal değil')
        break
else:
    print('sayı asal')