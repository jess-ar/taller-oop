class Character:
    def __init__(self, name, age, power, team):
        self.name = name
        self.age = age
        self.power = power
        self.team = team

    def introduce_team(self):
        return f"Hi, I am {self.name} from Marvel and I belong to the {self.team} team."

    def introduce_individual(self):
        return f"Hi, I am {self.name}, I am {self.age} years old, my power is {self.power} and I belong to the {self.team} team."

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age