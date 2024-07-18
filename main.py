from src.marvel import MarvelCharacter
from src.dc import DCCharacter
from src.xmen import Xmen
from src.avengers import Avengers
from src.justiceLeague import JusticeLeague

# Crear personajes de Marvel
iron_man = MarvelCharacter("Iron Man", 45, "Advanced Technology", "Avengers")
captain_america = MarvelCharacter("Captain America", 100, "Super Strength", "Avengers")
tormenta = MarvelCharacter("Tormenta", 38, "Control of Weather", "X-Men")

# Crear personajes de DC
batman = DCCharacter("Batman", 35, "Martial Arts", "Justice League")
superman = DCCharacter("Superman", 30, "Super Strength", "Justice League")
wonderwoman = DCCharacter("Wonderwoman", 35, "Super Strength", "Justice League")

# Crear equipo de Avengers y añadir miembros
avengers_team = Avengers()
avengers_team.add_member(iron_man)
avengers_team.add_member(captain_america)

# Crear equipo de La Liga de la Justicia y añadir miembros
justiceLeague_team = JusticeLeague()
justiceLeague_team.add_member(batman)
justiceLeague_team.add_member(wonderwoman)

# Crear equipo de X-Men y añadir miembros
xmen_team = Xmen()
xmen_team.add_member(tormenta)

# Introducir equipos de Avengers, La Liga de la Justicia y X-Men
print("Avengers Team:")
print(avengers_team.introduce_team())

print("\nJustice League Team:")
print(justiceLeague_team.introduce_team())

print("\nX-Men Team:")
print(xmen_team.introduce_team())

# Introducir personajes individuales
print("\nIndividual Introductions:")
print(batman.introduce_individual())
print(superman.introduce_individual())
print(tormenta.introduce_individual())