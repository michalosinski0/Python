countries = ['China', 'Iran', 'South Korea', 'Italy', 'Germany', 'Japan', 'Spain']
print(countries[0])
print(countries[0].title())
print(countries[-1].title())

print("Covid started in " + countries[0])

countries.append('Poland')
countries.insert(4, 'Portugal')
print(countries)
del countries[-1]
print(countries)

cured_country = countries.pop(-1)
print(countries)
print("cured country is: " + cured_country)

countries.remove('Italy')
print(countries)

countries.sort()
print(countries)
