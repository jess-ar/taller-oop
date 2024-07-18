from src.marvel import MarvelCharacter

class Avengers:
    def __init__(self):
        self.members = []

    def add_member(self, character):
        if isinstance(character, MarvelCharacter):
            self.members.append(character)
        else:
            raise ValueError("Only Marvel characters can be added to the Avengers.")

    def introduce_team(self):
        introductions = [member.introduce_team() for member in self.members]
        return "\n".join(introductions)