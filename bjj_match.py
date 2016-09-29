belts = {'white': 2, 'blue': 8, 'purple': 10, 'brown': 14, 'black': 17, 'red': 20}

strategies = {'guard': 1, 'chokes_back': 2, 'control_positions': 3, 'agressive_submissions': 4, 'takedowns': 5}

weight_classes = {'straw': 0, 'fly': 1, 'bantam': 2, 'feather': 3, 'light': 4,
                  'welter': 5, 'middle': 6, 'lightheavy': 7, 'heavy': 8}


class Fighter:

    def __init__(self, name, belt, weight, strategy, training):
        self.name = name
        self.belt = belt
        self.weight = weight
        self.strategy = strategy
        self.training = training
        self.odds = 0


class Royce_Gracie(Fighter):
    def __init__(self):
        # super().__init__()  # ?
        self. name = "Royce"
        self.belt = belts['black']
        self.weight = weight_classes['welter']
        self.strategy = strategies['agressive_submissions']
        self.training = 10
        self.odds = 0


class Me(Fighter):
    def __init__(self):
        # super().__init__()  # ?
        self.name = "Connor"
        self.belt = belts['blue']
        self.weight = weight_classes['light']
        self.strategy = strategies['chokes_back']
        self.training = 3
        self.odds = 0


class Match:
    def __init__(self):
        self.contestants = []

    def add_contestant(self, contestant):
        self.contestants.append(contestant)

    def odds_calc(self):

        strats = self.contestants[0].strategy - self.contestants[1].strategy
        m = strats / 5

        if m == 1 or m == 3:
            self.contestants[0].odds += 4
        elif m == 2 or m == 4:
            self.contestants[1].odds += 4
        elif m == 0:
            pass

        for fighter in self.contestants:
            fighter.odds += fighter.training
            fighter.odds += fighter.belt
            fighter.odds += fighter.weight

    def sim(self):
        if self.contestants[0].odds > self.contestants[1].odds:
            print("\nThe winner is: {}".format(self.contestants[0].name))
        elif self.contestants[1].odds > self.contestants[0].odds:
            print("\nThe winner is: {}".format(self.contestants[1].name))
        else:
            print("Draw")


print("The contestants are:")

fighter1 = Me()

fighter2 = Royce_Gracie()


ibjjf = Match()

ibjjf.add_contestant(fighter1)
ibjjf.add_contestant(fighter2)

ibjjf.odds_calc()

for fighter in ibjjf.contestants:
    print(fighter.name)


ibjjf.sim()
