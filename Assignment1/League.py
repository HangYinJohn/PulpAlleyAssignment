from Assignment1.Character import Character
from Assignment1.Follower import Follower
from Assignment1.Leader import Leader
from Assignment1.Sidekick import Sidekick
from Assignment1.Ally import Ally

__author__ = 'HangYin'


def print_line1():
    print("__________________________________________________________________")


def print_line():
    print("------------------------------------------------------------------")


def print_status():
    print("  Pos |  Name  |Health| Brawl|Shoot| Dodge| Might |Fine | Cunning ")


class League(object):
    def __init__(self, leagueName):
        self.leagueName = leagueName
        self.leagueSlot = 10
        self.characters = []

    def add_leader(self, name, health, brawl, shoot, dodge, might,
                   finesse, cunning, abilityName1, abilityName2,
                   abilityName3):
        leader = Leader(name, health, brawl, shoot, dodge, might,
                        finesse, cunning, abilityName1, abilityName2,
                        abilityName3, types="Leader", slot=0, level=4)
        if leader.add_ability(abilityName1) \
                is True and leader.add_ability(abilityName2) \
                is True and leader.add_ability(
                abilityName3) is True:
            self.characters.append(leader)
            return True
        else:
            return False

    def add_sidekick(self, name, health, brawl, shoot, dodge, might,
                     finesse, cunning, abilityName1, abilityName2,
                     abilityName3):
        sidekick = Sidekick(name, health, brawl, shoot, dodge, might,
                            finesse, cunning, abilityName1, abilityName2,
                            abilityName3, types="Sidekick", slot=3, level=3)
        if sidekick.add_ability(abilityName1) is True and sidekick.add_ability(
                abilityName2)\
                is True and sidekick.add_ability(abilityName3) is True:
            self.characters.append(sidekick)
            self.leagueSlot -= 3
            return True
        else:
            return False

    def add_ally(self, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, abilityName1, abilityName2):
        ally = Ally(name, health, brawl, shoot, dodge, might,
                    finesse, cunning, abilityName1, abilityName2,
                    types="  Ally", slot=2, level=2)
        if ally.add_ability(abilityName1) \
                is True and ally.add_ability(abilityName2) is True:
            self.characters.append(ally)
            self.leagueSlot -= 2
            return True
        else:
            return False

    def add_follower(self, name, health, brawl, shoot, dodge, might,
                     finesse, cunning, abilityName):
        follower = Follower(name, health, brawl, shoot, dodge, might,
                            finesse, cunning, abilityName, types="Follower",
                            slot=1, level=1)
        if follower.add_ability(abilityName) is True:
            self.characters.append(follower)
            self.leagueSlot -= 1
            return True
        else:
            return False

    def display_league(self):
        print_line1()
        print("--------{}---Available Slots: {}".
              format(self.leagueName, self.leagueSlot) + "---------")

    def display_chars(self):
        for i in self.characters:
            print_line()
            print_status()
            print_line()
            print(Character.__str__(i))
            Follower.display_ability(i)
