from src.marvel import MarvelCharacter

class Xmen:
    def __init__(self):
        self.members = []

    def add_member(self, character):
        if isinstance(character, MarvelCharacter):
            self.members.append(character)
        else:
            raise ValueError("Only Mutants characters can be added to the X-Men.")

    def introduce_team(self):
        introductions = [member.introduce_team() for member in self.members]
        return "\n".join(introductions)