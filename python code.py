import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_titles.csv")


df=df.dropna(subset=["type","release_year","rating","country","duration"])
 
mvt= df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(mvt.index,mvt.values,color=["lightblue"])
plt.title("Number of movies vs tv shows in netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("MVT.png",dpi=300,)
plt.show()

![pd](https://github.com/ammarkhan6949/-Project-Using-Python-Pandas-Matplotlib/blob/main/top.png)


rating_count= df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct="%1.1f%%",startangle=90,)
plt.title("Percentage of content rating ")
plt.legend()
plt.tight_layout()
plt.savefig("ranting.png",dpi=300)
plt.show()




movie_du=df[df["type"]=="Movie"].copy()
plt.figure(figsize=(8,6))
movie_du["duration_int"]=movie_du["duration"].str.replace("min" ," ").astype(int)
plt.hist(movie_du["duration_int"],bins=30,color="pink",edgecolor="black")
plt.xlabel("Minutes")
plt.ylabel("No of movies")
plt.title("Duration of movies")
plt.tight_layout()
plt.savefig("movie_du.png" ,dpi=300)
plt.show()

relation=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(relation.index, relation.values,color= "#f9d43a")
plt.xlabel("Release year")
plt.ylabel("No of Shows")
plt.grid()
plt.title("Relation b/w Release year and Movies ")
plt.tight_layout()
plt.savefig("relation.png" ,dpi=300)
plt.show()


top = df["country"].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(top.index ,top.values, color=["#43b7f9","pink"])
plt.xlabel("Country")
plt.ylabel("No of Show")
plt.title("Top 10 countries by highest number of show")
plt.tight_layout()
plt.savefig("top.png" ,dpi=300)
plt.show()

content = df.groupby(["release_year","type"]).size().unstack().fillna(0)
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(content.index ,content["Movie"] ,color= "pink")
plt.title("Moives released per year")
plt.xlabel("Year")
plt.ylabel("NO of Movies")
plt.grid()
plt.subplot(1,2,2)
plt.plot(content.index,content["TV Show"] , color="black")
plt.title("Tv shows released per year")
plt.suptitle("Comparision of movies and tv shows released over year")
plt.xlabel("Year")
plt.ylabel("NO of Tv shows")
plt.grid()
plt.tight_layout()
plt.savefig("comp.png",dpi=300)
plt.show()


