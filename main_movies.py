import requests
from bs4 import BeautifulSoup


URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
site_content=requests.get()
site_content.raise_for_status()
site_html=site_content.text

soup=BeautifulSoup(site_html, "html.parser")


movie_titles_from_back=[]
titles=soup.find_all(name="h3", class_="title")
for title in titles:
    movie_titles_from_back.append(title.getText())

final_list=[]
for i in reversed(movie_titles_from_back):
    final_list.append(i)
print(final_list)

# try: # This is for new url to add new movies to the list from the same
#     with open(file="movie_list.txt", mode="a", encoding="utf-8") as file:
#         for title in final_list:
#             file.write(title+"\n")
# except FileNotFoundError:
    with open(file="movie_list.txt", mode="w", encoding="utf-8") as file:
        for title in final_list:
            file.write(title + "\n")
