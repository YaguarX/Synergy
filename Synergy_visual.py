import matplotlib.pyplot as plt


year=[1950,1975,2000,2018]
population=[2.12,3.681,5.312,6.981]

plt.figure(figsize=(8,6))
plt.plot (year,population, marker = 'o')


plt.title ('Население земли с 1950 по 2018 г.')
plt.xlabel('Год')
plt.ylabel('Насление ')


plt.show()

