import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("imdb.csv")
rating1 = len(df[df['Rating'] > 8.5]['Title'])
rating2 = len(df[df['Rating'] == 8.5]['Title'])
rating3 = len(df[df['Rating'] < 8.5]['Title'])

plt.bar(8.2, rating1, color='r',width=0.4)
plt.bar(8.5, rating2, color='y',width=0.2)
plt.bar(8.9, rating3, color='b',width=0.6)
plt.xlabel('imdb rating')
plt.ylabel('Movie Numbers')
plt.title('Top250 according to imdb rating')
plt.show()

year0 = len(df[df['Year'] > 2010]['Year'])
year1 = len(df[(df['Year'] > 2000) & (df['Year'] <= 2010)]['Year'])
year2 = len(df[(df['Year'] > 1990) & (df['Year'] <= 2000)]['Year'])
year3 = len(df[(df['Year'] > 1980) & (df['Year'] <= 1990)]['Year'])
year4 = len(df[(df['Year'] > 1970) & (df['Year'] <= 1980)]['Year'])
year5 = len(df[(df['Year'] > 1960) & (df['Year'] <= 1970)]['Year'])
year6 = len(df[(df['Year'] > 1950) & (df['Year'] <= 1960)]['Year'])
year7 = len(df[(df['Year'] > 1940) & (df['Year'] <= 1950)]['Year'])
year8 = len(df[(df['Year'] > 1930) & (df['Year'] <= 1940)]['Year'])
year9 = len(df[(df['Year'] > 1920) & (df['Year'] <= 1930)]['Year'])

years = "1921-1930","1931-1940","1941-1950","1951-1960","1961-1970","1971-1980","1981-1990","1991-2000","2001-2010","2011-"
films = [year9,year8,year7,year6,year5,year4,year3,year2,year1,year0]

plt.title("imdb top250 by release year of movies")
plt.pie(films, labels=years, shadow=True, explode=(0.01,0.01,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1), autopct="%1.1f%%")
plt.show()

mean1 = df[(df['Year'] > 2000) & (df['Year'] <= 2010)]['Rating'].mean()
mean2 = df[(df['Year'] > 1990) & (df['Year'] <= 2000)]['Rating'].mean()

plt.bar(mean1, year1, color='r', label="2001-2010 imdb rating averages", width=0.01)
plt.bar(mean2, year2, color='y', label="1991-2000 imdb rating averages", width=0.01)
plt.legend()
plt.xlabel('imdb rating')
plt.ylabel('Movie Numbers')
plt.title("Comparison of imdb rating averages by years")
plt.show()

max80s = df[(df['Year'] >= 1980) & (df['Year'] < 1990)].head(1)
max70s = df[(df['Year'] >= 1970) & (df['Year'] < 1980)].head(1)
print(max80s)
print(max70s)