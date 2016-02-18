import pandas
data = {1: ["Mazda", "Toyota", "Toyota", "Kia", "Honda"],
		2: ["RX", "Tacoma", "Tundra", "Sorrento", "Civic"],
		3: [23, 24, 12, 30,  36],
		4: [240, 268, 400, 150, 176],
		5: [3000, 7000, 10000, 3000, 2500]}
indices = ["Manufacturer", "Model", "MPG", "HP", "Weight"]
dp = pandas.DataFrame(data, indices)
print("Data Frame")
print("==========")
print(dp)
print("Head")
print(dp.head(n=1))
print("Tail")
print(dp.tail(n=1))
print("Maen")
print(dp.mean())