import pandas as pd

# Organizando os dados em um formato estruturado
data = {
    "Year": [],
    "Country": [],
    "GDP": [],
    "Life_Expectancy": []
}

# Preencha os dados a partir do texto
raw_data = '''1971,Canada,313.391,72.8
1971,Germany,298.251,70.8
1971,Great Britain,134.172,71.9
1971,Japan,163.854,72.9
1971,USA,357.988,71.2
1972,Germany,337.364,71.0
1972,Japan,185.39,73.2
1972,USA,397.097,71.2
1973,Germany,384.541,71.3
1973,Japan,205.778,73.4
1973,USA,439.302,71.4
1974,Germany,452.744,71.5
1974,Japan,242.018,73.7
1974,USA,495.114,72.0
1975,Germany,532.481,71.4
1975,France,363.61,73.0
1975,Japan,284.269,74.3
1975,USA,560.75,72.7
1976,Canada,543.337,73.8
1976,Germany,591.098,71.8
1976,Japan,303.725,74.8
1976,USA,638.851,72.9
1977,Germany,647.352,72.5
1977,Japan,340.628,75.3
1977,USA,726.241,73.3
1978,Germany,729.457,72.4
1978,Japan,392.577,75.7
1978,USA,808.884,73.5
1979,Canada,692.269,75.1
1979,Germany,800.703,72.8
1979,Japan,452.931,76.2
1979,USA,908.963,73.9
1980,Canada,791.812,75.2
1980,Germany,908.166,72.9
1980,France,659.826,74.3
1980,Great Britain,385.099,73.2
1980,Japan,535.016,76.1
1980,USA,1036.3,73.7
1981,Canada,898.807,75.5
1981,Germany,1014.713,73.2
1981,Great Britain,433.957,73.8
1981,Japan,603.965,76.5
1981,USA,1191.537,74.1
1982,Canada,996.086,75.6
1982,Germany,1044.528,73.5
1982,Great Britain,448.477,74.1
1982,Japan,664.777,76.9
1982,USA,1329.669,74.5
1983,Canada,1066.746,75.9
1983,Germany,1104.594,73.8
1983,Great Britain,501.924,74.3
1983,Japan,714.857,77.0
1983,USA,1451.945,74.6
1984,Canada,1135.02,76.2
1984,Germany,1196.56,74.3
1984,Great Britain,521.522,74.5
1984,Japan,745.981,77.4
1984,USA,1590.667,74.7
1985,Canada,1212.85,76.3
1985,Germany,1298.555,75.0
1985,France,1001.145,75.4
1985,Great Britain,549.608,74.7
1985,Japan,818.382,77.6
1985,USA,1735.156,74.7
1986,Canada,1278.816,76.5
1986,Germany,1386.51,75.2
1986,Great Britain,578.61,74.8
1986,Japan,859.855,78.1
1986,USA,1847.773,74.7
1987,Canada,1357.453,76.7
1987,Germany,1480.096,75.6
1987,Great Britain,634.956,75.2
1987,Japan,916.703,78.5
1987,USA,1976.166,74.9
1988,Canada,1461.3,76.8
1988,Germany,1616.349,75.9
1988,Great Britain,688.049,75.3
1988,Japan,969.251,78.4
1988,USA,2195.392,74.9
1989,Canada,1579.543,77.1
1989,Germany,1596.16,76.0
1989,Great Britain,739.714,75.4
1989,Japan,1021.247,78.8
1989,USA,2424.654,75.1
1990,Canada,1699.774,77.3
1990,Germany,1724.332,77.3
1990,France,1459.11,77.0
1990,Great Britain,782.612,75.7
1990,Japan,1088.959,78.9
1990,USA,2684.984,75.3
1991,Canada,1805.209,77.6
1991,France,1558.033,77.2
1991,Great Britain,842.797,75.9
1991,Japan,1166.43,79.1
1991,USA,2901.589,75.5
1992,Canada,1897.456,77.8
1992,Germany,2019.308,76.1
1992,France,1651.139,77.5
1992,Great Britain,930.701,76.3
1992,Japan,1253.415,79.2
1992,USA,3100.343,75.7'''

for line in raw_data.splitlines():
    year, country, gdp, life_expectancy = line.split(',')
    data["Year"].append(int(year))
    data["Country"].append(country)
    data["GDP"].append(float(gdp))
    data["Life_Expectancy"].append(float(life_expectancy))

# Crie o DataFrame
df = pd.DataFrame(data)
import matplotlib.pyplot as plt
# Crie uma figura com 15 polegadas de largura e 10 polegadas de altura
plt.figure(figsize=(15, 10))

# Itere sobre cada país
for country in df['Country'].unique():
    country_df = df[df['Country'] == country]
    plt.plot(country_df['Year'], country_df['Life_Expectancy'], label=country)

# Adicione uma legenda ao criar gráfico no Python
plt.legend()

# Adicione um título ao gráfico
plt.title("Evolução da Expectativa de Vida por País")

# Comando para exibir e criar gráfico no Python
plt.show()


# GRÁFICO DE CUSTO DE VIDA POR PAIS


# Crie uma figura com 15 polegadas de largura e 10 polegadas de altura
plt.figure(figsize=(15, 10))

# Itere sobre cada país
for country in df['Country'].unique():
    country_df = df[df['Country'] == country]
    plt.plot(country_df['Year'], country_df['Spending_USD'], label=country)

# Adicione uma legenda ao criar gráfico no Python
plt.legend()

# Adicione um título ao gráfico
plt.title("Evolução do custo de vida por País")

# Comando para exibir e criar gráfico no Python
plt.show()
