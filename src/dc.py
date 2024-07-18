from src.character import Character


class DCCharacter(Character):
    def __init__(self, name, age, power, team):
        super().__init__(name, age, power, team)

    def introduce_team(self):
        return f"Hi, I am {self.name} from DC and I belong to the {self.team} team."

    def introduce_individual(self):
        return f"Hi, I am {self.name}, I am {self.age} years old, my power is {self.power} and I belong to the {self.team} team."