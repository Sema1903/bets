import kagglehub
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
import numpy as np

# Download latest version
path = kagglehub.dataset_download("martj42/international-football-results-from-1872-to-2017")

print("Path to dataset files:", path)
f = open(path + '/results.csv', 'r').read().split('\n')
del f[0]
x = []
y = []
for i in range(len(f) - 1):
  f[i] = f[i].split(',')
  x.append([f[i][1], f[i][2], f[i][5], f[i][6], f[i][8]])
  y.append(f[i][3] + ' : ' + f[i][4])
  def coding(n):
    a = {}
    s = 0
    for i in range(len(f) - 1):
      keys = []
      for j in a:
        keys.append(j)
      if f[i][n] not in keys:
        a.update({f[i][n]: s})
      s += 1
    return a
  countries = coding(1)
  others = coding(2)
  tournir = coding(5)
  city = coding(6)
  neural = coding(8)
  x = []
  y = []
  for i in range(len(f) - 1):
    x.append([countries[f[i][1]], others[f[i][2]], tournir[f[i][5]], city[f[i][6]], neural[f[i][8]]])
    y.append(int(f[i][3]) * 100 + int(f[i][4]))
    from sklearn.linear_model import RidgeClassifier
    scores = []
    for i in range(1):
      score = 0
      x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
      neigh = RidgeClassifier()
      neigh.fit(x_train, y_train)
      for j in range(len(y_test)):
        if neigh.predict([x_test[j]])[0] == y_test[j]:
          score += 1
      scores.append(score/len(y_test))
    print('Процент угадывания:', np.mean(scores)*100)
print(tournir)
print(city)
country1 = input('Хозяева поля>> ')
country2 = input('Гости>> ')
tournament = input('Чемпионат>> ')
citys = input('Город>> ')
neu = input('Нейтральная ли страна>> ')
result = neigh.predict([[countries[country1], others[country2], tournir[tournament], city[citys], neural[neu]]])[0]
print('Предварительный результат матча -', result // 100, ':', result % 100)