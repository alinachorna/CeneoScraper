from os import listdir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#print(*listdir('/Users/alinachorna/CeneoScraper/reviews'),sep="\n") #gwiazdka, zeby rozpakowac liste




pd.set_option("display.max_columns",None)

print(*[file_name.split(".")[0] for file_name in listdir("reviews")], sep="\n")

product_id=input("Podaj kod produktu: ")

reviews=pd.read_json(f"reviews/{product_id}.json")

#print(reviews)

#reviews_count = reviews.review_id.count()
#reviews_count = reviews["review_id"].count()
#reviews_count = reviews.shape[0] --o/1 w zaleznosci od tego czy wiersz, czy kolumna

reviews.stars=reviews.stars.map(lambda stars: float(stars.split("/")[0].replace(",",".")))
reviews_count=len(reviews.index)
#pros_count
pros_count=reviews.pros.astype(bool).sum()
#pros_count=reviews.pros.map(bool).sum()

#cons_count
cons_count=reviews.cons.astype(bool).sum()

#average_score
average_score=reviews.stars.mean().round(2)

stars = reviews.stars.value_counts().reindex(np.arange(0,5.5,0.5),fill_value=0)
stars.plot.bar(color="green")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")

#plt.savefig(f"plots/{product_id}.png")
#plt.close()
plt.show()
#print(reviews.stars)
#print(stars)
