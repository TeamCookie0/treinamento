# -*- coding: utf-8 -*-

entrada = []
entrada.append(raw_input()) #adiciona item a lista
entrada.append(raw_input())
entrada.append(raw_input())

if entrada[0] == "vertebrado": #condições
	if entrada[1] == "ave":
		if entrada[2] == "carnivoro":
			print("aguia")
		else:
			print("pomba")
	else:
		if entrada[2] == "onivoro":
			print("homem")
		else:
			print("vaca")
else:
	if entrada[1] == "inseto":
		if entrada[2] == "hematofago":
			print("pulga")
		else:
			print("lagarta")
	else:
		if entrada[2] == "hematofago":
			print("sanguessuga")
		else:
			print("minhoca")