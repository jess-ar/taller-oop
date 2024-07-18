from src.dc import DCCharacter

class JusticeLeague:
    def __init__(self):
        self.members = []

    def add_member(self, character):
        if isinstance(character, DCCharacter):
            self.members.append(character)
        else:
            raise ValueError("Only DC characters can be added to the Justice League.")

    def introduce_team(self):
        introductions = [member.introduce_team() for member in self.members]
        return "\n".join(introductions)