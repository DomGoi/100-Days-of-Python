from BeautifulSoup import Soup
from FormularzGoogle import Google



soup=Soup()
adresy, ceny, linki=soup.get_info()
goog=Google(adresy,ceny,linki)
goog.insert_into_formularz()
