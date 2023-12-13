from gempa import*

gempa_1 = Gempa("Banten", 1.2)
gempa_2 = Gempa("Palu", 6.1)
gempa_3 = Gempa("Cianjur", 5.6)
gempa_4 = Gempa("Jayapura", 3.3)
gempa_5 = Gempa("Garut", 4.0)

print(gempa_1.dampak())

print(gempa_2.dampak())

print(gempa_3.dampak())

print(gempa_4.dampak())

print(gempa_5.dampak())


