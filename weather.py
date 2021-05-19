temperature = 50
forecast = "rain"
raining = True

if temperature > 80:
    print("It's too hot!")
    print('Stay inside!')

elif temperature < 60:
    print("It's too cold!")
    print('Stay inside')
else:
    print('Enjoy the outdoors!')

# print("Is raining ? " + raining)
if not raining:
    print("Go outside is not raining")
else:
    print("Stay inside is raining")
