car_speed = int(input("Velocidade do carro?: "))
max_spped = int(input("velocidade maxima da rua?"))

diff = car_speed - max_spped 

if diff > 0 and diff <= 10:
    print("50€")
elif diff >= 11 and diff <= 30:
    print("100€")
elif diff >= 31:
    print("300€")
else:
    print("nada")