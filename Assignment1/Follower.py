from Assignment1.Character import Character

__author__ = 'HangYin'


class Follower(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, ability1, types="Follower", slot=1, level=1):
        self.types = types
        self.slot = slot
        self.level = level
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.ability1 = ability1
        self.abilities = []