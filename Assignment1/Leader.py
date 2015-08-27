from Assignment1.Character import Character

__author__ = 'HangYin'


class Leader(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse,
                 cunning, ability1, ability2, ability3, types="Leader",
                 slot=0, level=4):
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
        self.ability2 = ability2
        self.ability3 = ability3
        self.abilities = []
