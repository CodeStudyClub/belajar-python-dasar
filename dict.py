customer = {"Name": "Alief", "Age": 21, "Address": "Jawa Timur"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "Imanuel"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}:{value}")

