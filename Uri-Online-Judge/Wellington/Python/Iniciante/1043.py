# -*- coding: utf-8 -*-

linha = raw_input().split(' ')
a, b, c = linha
a = float(a)
b = float(b)
c = float(c)

if abs(b-c) < a and a < b+c and abs(a-c) < b and b < a+c and abs(a-b) < c and c < a+b: #condição
	print("Perimetro = %.1f" % (a+b+c))
else:
	print("Area = %.1f" % ((c * (a+b))/2))