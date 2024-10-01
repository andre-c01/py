years_of_smoking = int(input("Qunatos anos fuma?: "))
day_amount = int(input("Quantos fuma por dia?: "))
cost = float(input("Preco da Carteira?: "))

cost_till_now = (years_of_smoking * (day_amount * 365) / 20) * cost

print(cost_till_now)