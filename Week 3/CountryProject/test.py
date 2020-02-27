from week3 import Country

USA = Country("USA", 10, 2)
SecondCountry = Country("I Don't Care", 10, 3)
ThirdCountry = Country("The THird Country", 1109257192385701289537, 12593250)

test1 = USA.population_density()
test2 = SecondCountry.population_density()
test3 = ThirdCountry.population_density()
sum1 = USA.summary()
sum2 = SecondCountry.summary()
sum3 = ThirdCountry.summary()
print(f'{test1, test2, test3}')
print(f'{sum1, sum2, sum3}')
