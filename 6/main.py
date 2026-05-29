from joke import Joke
from dao_joke import Dao_joke

dao = Dao_joke("mongodb://localhost:27017/")

dao.insert(Joke("Warum kann man Informatikern nicht trauen? Sie cachen alles.", ["IT", "Nerd"], "Max"))
dao.insert(Joke("Was ist ein Algorithmus? Ein kranker Alligator.", ["IT", "Kinder"], "Lisa"))

witze = dao.get_category("IT")
for w in witze:
    print(f"{w.author}: {w.text}")