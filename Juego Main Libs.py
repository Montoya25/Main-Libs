sus = input("Ingresa un sustantivo: ")
lug = input("Ingresa un lugar: ")
ver = input("Ingresa un verbo: ")
lug2 = input("Ingresa otro lugar: ")

historia = "Había una vez un/a {sus} que vivía en {lug}. Un día decidió {ver} hacia {lug2}."

print("La historia final es así: ", historia.format(sus=sus, lug=lug, ver=ver, lug2=lug2))