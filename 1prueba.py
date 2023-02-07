import pandas as pd

paises = ['Mexico', 'Colombia', 'Peru', 'Argentina']
poblacion = [126014024, 34352719, 52682689, 46044703]


dict_poblacion = {'Países': paises, 'Población': poblacion}
df_poblacion = pd.DataFrame.from_dict(dict_poblacion)
df_poblacion.to_csv('poblacion.csv', index=False)

""" print(paises[-3]) """



""" for pais in paises:
	print(pais)
 """


""" with open('text.txt', 'w') as file:
	file.write("Data extracted correctly!") """
