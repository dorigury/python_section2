from bs4 import BeautifulSoup

fp = open("car.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)


car_lamda = lamda q : print("car_lambda", soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
