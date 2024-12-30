class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def perform_action(self):
        raise NotImplementedError


class Audience(Person):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        return f"{self.name} is watching the game"


class Player(Person):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        return f"{self.name} is playing the game"


class Coach(Person):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        return f"{self.name} is coaching the team"


class Referee(Person):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        return f"{self.name} is refereeing the game"


class PersonFactory:
    def create_person(self, name, role):
        if role == "audience":
            return Audience(name)
        elif role == "player":
            return Player(name)
        elif role == "coach":
            return Coach(name)
        elif role == "referee":
            return Referee(name)
        else:
            return None


if __name__ == "__main__":
    factory = PersonFactory()
    audience = factory.create_person("John", "audience")
    player = factory.create_person("Tom", "player")
    coach = factory.create_person("Alice", "coach")
    referee = factory.create_person("Bob", "referee")

    print(audience.perform_action())
    print(player.perform_action())
    print(coach.perform_action())
    print(referee.perform_action())
