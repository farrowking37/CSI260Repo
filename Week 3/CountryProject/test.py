from week3 import Country

USA = Country("USA", 10, 2)
SecondCountry = Country("I Don't Care", 10, 3)

test1 = USA.population_density()
test2 = SecondCountry.population_density()
print(f'{test1, test2}')