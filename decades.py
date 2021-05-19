age = input('How old are you?\n')
age = int(age)

#decades = int(age / 10)
decades = age // 10
years = age % 10

print('You are ' + str(decades) + ' decade(s) and ' + str(years) + ' year(s) old')
