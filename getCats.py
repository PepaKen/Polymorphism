from Cats import Cats

catA = Cats("Сэм", "мальчик", 2)
catB = Cats("Барон", "мальчик", 2)

cat_list = [catA, catB]

for cat in cat_list:
    cat.getList()
