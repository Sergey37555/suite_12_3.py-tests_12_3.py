class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            temp = {}
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    temp[str(participant)] = participant.speed
            temp = sorted(temp.items(), key=lambda item: item[1], reverse=True)
            for participant in temp:
                finishers[place] = participant[0]
                place += 1
                self.participants.remove(participant[0])

        return finishers