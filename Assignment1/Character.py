from Assignment1.Abilities import Abilities

__author__ = 'HangYin'


class Character(object):
    def __init__(self, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, types=None, slot=None, level=None):
        self.types = types
        self.level = level
        self.slot = slot
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.abilities = []

    def __str__(self):
        return "{} {}  {}    {}    {}   {}   {}    {}   {}" \
            .format(self.types, self.name, self.health, self.brawl, self.shoot,
                    self.dodge, self.might, self.finesse, self.cunning)

    def add_ability(self, abilityName):
        if abilityName == "animal":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="unable to shoot, but adds 1d "
                                        "to 2 more skills.",
                          abilityLevel=1))
            return True

        elif abilityName == "clever":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of cunning has "
                                        "been increased by 1 \n"
                                        " die",
                          abilityLevel=1))
            return True

        elif abilityName == "agile":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of dodge has "
                                        "been increased by 1 \n"
                                        " die.",
                          abilityLevel=1))
            return True

        elif abilityName == "mighty":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of might has "
                                        "been increased by 1 \n"
                                        " die.",
                          abilityLevel=1))
            return True

        elif abilityName == "savvy":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of finesse has "
                                        "been increased by 1 \n"
                                        " die.",
                          abilityLevel=1))
            return True

        elif abilityName == "fierce":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of brawl has "
                                        "been increased by 1 \n"
                                        " die.",
                          abilityLevel=1))
            return True

        elif abilityName == "marksman":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of shoot has "
                                        "been increased by 1 \n"
                                        " die.",
                          abilityLevel=1))
            return True

        elif abilityName == "speedy":
            self.abilities.append(
                Abilities(abilityName,
                          abilityEffect="the status of running speed has "
                                        "been increased to 15 \n"
                                        " - instead of 12.",
                          abilityLevel=1))
            return True

        elif abilityName == "athletic":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="You can only shift this "
                                            "character's\n"
                                            "dice-type up when rolling "
                                            "for Might or Finesse \n"
                                            "one time per turn",
                              abilityLevel=2))

                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "brute":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character may re-roll "
                                            "one Brawl or Might \n"
                                            "one time per turn \n"
                                            "die.",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "daredevil":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character receives a +1d "
                                            "bonus when rolling for a Peril \n"
                                            "one time per turn",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False
        elif abilityName == "crafty":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character may re-roll"
                                            "one Dodge or Cunning \n"
                                            "one time per turn \n"
                                            "die.",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "eagleeyed":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character's range is "
                                            "raised to 12 - 48 up from 6 - 24",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "intrepid":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character able to "
                                            "move one step \n"
                                            " when successfully dodge "
                                            "an peril or attack ",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "finagler":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="You can only shift this "
                                            "character's \n"
                                            "dice-type up when rolling "
                                            "for Cunning or Finesse \n"
                                            "one time per turn",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "sharp":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character may re-roll "
                                            "one shoot or finesse \n"
                                            "one time per turn \n"
                                            "die.",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "specialist":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="You can only shift this "
                                            "character's \n"
                                            "dice-type up when rolling "
                                            "for Cunning or Might \n"
                                            "one time per turn",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "stealthy":
            if self.level >= 2:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character may hide "
                                            "as an action - instead "
                                            "of a full action",
                              abilityLevel=2))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "astute":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="while injuries,the character's "
                                            "Shoot and Finesse \n"
                                            "dice-type are not lowered .",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "brash":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character is not limited "
                                            "to rushing to the closest enemy.",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "deadeye":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character is not limited "
                                            "to shooting to the "
                                            "closest enemy.",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "deductive":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="this character allow you "
                                            "to draw one fortune card",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "indomitable":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character may re-roll "
                                            "one recovery check per turn.",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "muscle-of-steel":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="while injuries,the character's "
                                            "brawl and might \n"
                                            "dice-type are not lowered .",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "hardened-veteran":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="the character ignores "
                                            "to multiple combats penalty.",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "shrewd":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="while injuries,the character's"
                                            "dodge and cunning \n"
                                            "dice-type are not lowered .",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "quick-shot":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="You can only shift this "
                                            "character's one time per turn \n"
                                            "the shooting dice-type down "
                                            "to gain a +2d bonus \n"
                                            "this effect only work "
                                            "against close target.",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "quick-strike":
            if self.level >= 3:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="You can only shift this "
                                            "character's one time per turn \n"
                                            "the brawling dice-type "
                                            "down to gain a +2d bonus.",
                              abilityLevel=3))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        elif abilityName == "lucky-devil":
            if self.level >= 4:
                self.abilities.append(
                    Abilities(abilityName,
                              abilityEffect="When leader activates, "
                                            "the opponent cannot play "
                                            "any fortune cards",
                              abilityLevel=4))
                return True

            else:
                print("\(-_-)/ character's level is not enough \(B_B)/")
                return False

        else:
            print("\(-_-)/ unknown ability \(B_B)/")
            return False

    def display_ability(self):
        for i in self.abilities:
            print(Abilities.__str__(i))
