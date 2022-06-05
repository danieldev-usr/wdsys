
print("""
-------------------------------------------
Ferramenta em desenvolvimento...
[01] Info
[02] Massa (Newton)
[03] Porcentagem
[04] Gastos eletricos 
[05] Duração de bateria eletronica
[06] Porcentagem da perda de peso
[07] MIT license / reports
-------------------------------------------
""")

while True:
	
	print(" ")
	gg = input("(select)> ")
	
	if gg=="01":
		print("...")
		print("""
		Calculos e mais calculos
		(estudem crianças kkk....)
		""")
	
	elif gg=="02":
		vlm = int(input("Digite o volume: "))
		dns = float(input("Digite a densidade: "))
		sm = vlm*dns
		print(f"Sua massa é {sm}")
		
	elif gg=="03":
		a = int(input(">> "))
		pcr = 100
		b = int(input(">> "))
		cnt1 = pcr*b
		cnt2 =b/a
		print(f"{cnt2}%")
		
	elif gg=="04":
		ge = float(input("Digite os watts do seu aparelho: "))
		hrs = int(input("Quantas horas voce usa o aparelho?: "))
		dvd = ge/1000
		sc = dvd*hrs
		print(f"{sc} kWh")
		
	elif gg=="05":
		dx = float(input("Capacidade: "))
		cx = float(input("Corrente: "))
		cg = dx/cx
		print(f"{cg}h")
		
	elif gg=="06":
		pi = float(input("PI: "))
		pa = float(input("PA: "))
		clc1 = pi-pa
		clc2 = clc1/pi
		clc3 = clc2*100
		print(f"{clc3}%")
		
	elif gg=="07":
		print("")
		print("[Instagram] = [@metalheadkkkk]...")
		print("[Telegram] = [@BaalZevuv6")
		