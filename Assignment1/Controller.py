import cmd
import os
import pickle
from Assignment1.League import League

__author__ = 'HangYin'


# -------------------------------------------------------------------------------
# Name:        Pulp Alley - Character Sheet
# Purpose:     PR301 - Assignment 1
# Author:      HangYin
# Created:     17/08/2015
# -------------------------------------------------------------------------------

def print_wall():
    print("----------------------------------------------------------- \n"
          " \(^o^)/ \(@_@)/ \(-o-)/ \(8o8)/ \(*_*)/ \(ToT)/  \([]_[])/ \n"
          "-----------------------------------------------------------")


def print_fields():
    print("")


# this is the Controller Class
class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "\nType command: "
        print_wall()
        print("      Welcome to Pulp Alley Character Sheet Creator \n"
              "               Tips: about and help command \n"
              "             will bring you useful information ")
        print_wall()
        self.leagues = League(self)
        self.hasLeader = False
        self.hasLeague = False
        self.error = 0

    @staticmethod
    def do_about(command):
        # this about command shows user some information about this application
        print_wall()
        print("Welcome to Pulp Alley Character Sheet Creator \n" +
              "Created by Hang Yin \n"
              "This application is created for build up a \n" +
              "Character sheet that contains league \n"
              "which have information \n" +
              "of a Leader, Sidekick, Ally, and Follower\n "
              "the league must be created before character\n"
              "please notice the command MUST start with lower case!! \n"
              "the ability of character must be in lower case as well!! \n"
              "for example: \n"
              "leader "
              "DeathWing,d9,4d9,4d10,3d9,4d10,4d9,3d10,astute,brute,shrewd \n"
              "is used for create leader named DeathWing,\n "
              "the following syntax is the details \n"
              "the details must be provide for you to create a character  ")
        print_wall()

    def do_league(self, command):
        # this league command is used for create league
        # for example "league Horde" is used for create the league named Horde
        try:
            if command == "":
                raise InvalidActionError(
                    "\(0o0)/ you league need a name! \(@_@)/"
                )
            elif self.hasLeague is True:
                raise InvalidActionError(
                    "\(-_-)/ that league is already created \(B_B)/"
                )
            else:
                self.leagues = League(command)
                print(
                    "(^o^)League " + command + " is created!(^o^)"
                )
                self.hasLeague = True
        except InvalidActionError as err:
            print(err)

    def do_leader(self, command):
        # you have to type input in this way, or it will be an error
        # for example:
        # leader DeathWing,d9,4d9,4d10,3d9,4d10,4d9,3d10,astute,brute,shrewd
        leagues = self.leagues
        try:
            if self.hasLeader is False and self.hasLeague is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create league first!!!!!"
                )
            elif self.hasLeader is True:
                raise InvalidActionError(
                    "\(^o^)/ you already have a leader \(-o-)/"
                )
            else:
                arg = command.split(",")
                if leagues.add_leader(
                        arg[0], arg[1], arg[2], arg[3], arg[4],
                        arg[5], arg[6], arg[7], arg[8], arg[9],
                        arg[10]) \
                        is True:
                    self.hasLeader = True
                    print(
                        "(^o^)Leader '{}' is created!(^o^)".format(arg[0])
                    )
                else:
                    print("\(B_B)/Leader Not Created!\(-_-)/")
        except InvalidActionError as err:
            print(err)

    def do_sidekick(self, command):
        # you have to type input in this way, or it will be an error
        # for example:
        # sidekick LifeReaper,d7,2d7,4d7,d9,3d5,2d9,3d7,finagler,brash,intrepid
        l = self.leagues
        try:
            if self.hasLeague is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create a league first!!!!!"
                )
            elif l.leagueSlot < 5:
                raise InvalidActionError(
                    "\(0_0)/ not enough details !!!!!"
                )
            elif self.hasLeader is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create a leader first!!!!!"
                )
            else:
                arg = command.split(",")
                if len(arg) < 11:
                    print("INCOMPLETE")
                else:
                    if l.add_sidekick(
                            arg[0], arg[1], arg[2], arg[3], arg[4],
                            arg[5], arg[6], arg[7], arg[8], arg[9],
                            arg[10]) is True:
                        print(
                            "(^o^)Sidekick  '{}' is created!(^o^)".format(
                                arg[0]
                            )
                        )
                    else:
                        print(
                            "\(0o0)/ your Sidekick is not created ! \(@_@)/"
                        )
        except InvalidActionError as err:
            print(err)

    def do_ally(self, command):
        # you have to type input in this way, or it will be an error
        # for example:
        # ally BloodQueen,2d5,3d5,d9,1d10,3d5,1d7,1d7,sharp,specialist
        leagues = self.leagues
        try:
            if self.hasLeague is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create a league first!!!!!"
                )
            elif leagues.leagueSlot < 2:
                raise InvalidActionError(
                    "\(0_0)/ not enough details !!!!!"
                )
            elif self.hasLeader is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create a leader first!!!!!"
                )
            else:
                arg = command.split(",")
                if leagues.add_ally(arg[0], arg[1], arg[2], arg[3], arg[4],
                                    arg[5], arg[6], arg[7], arg[8],
                                    arg[9]) is True:
                    print(
                        "(^o^)your Ally '{}' is created!(^o^)".format(arg[0])
                    )
                else:
                    print(
                        "\(0o0)/ your Ally is not created ! \(@_@)/"
                    )
        except InvalidActionError as err:
            print(err)

    def do_follower(self, command):
        # you have to type input in this way, or it will be an error
        # for example:
        # follower Deathbringer,d5,1d5,1d5,3d5,1d5,2d5,1d9,speedy,marksman
        leagues = self.leagues
        try:
            if self.hasLeague is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create a league first!!!!!"
                )
            elif leagues.leagueSlot < 1:
                raise InvalidActionError(
                    "\(0_0)/ not enough details !!!!!"
                )
            elif self.hasLeader is False:
                raise InvalidActionError(
                    "\(0_0)/ you need create a leader first!!!!!"
                )
            else:
                arg = command.split(",")
                if leagues.add_follower(
                        arg[0], arg[1], arg[2], arg[3], arg[4],
                        arg[5], arg[6], arg[7], arg[8]) is True:
                    print(
                        "(^o^)your Follower '{}' is created!(^o^)".format(
                            arg[0]
                        )
                    )
                else:
                    print(
                        "\(0o0)/ your Follower is not created ! \(@_@)/"
                    )

        except InvalidActionError as err:
            print(err)

    def do_display(self, command):
        league = self.leagues
        league.display_league()
        league.display_chars()

    def do_save(self, command):
        try:
            if command == "":
                raise InvalidInputError(
                    "(0_0)file name can not be empty(@_@)"
                )
            else:
                data = [self.leagues]
                with open(command + ".pickle", "wb") as save_file:
                    pickle.dump(data, save_file)
                print(
                    "(^o^)file saved as " + command + ".pickle (-o-)"
                )
        except InvalidInputError as err:
            print(err)

    def do_load(self, command):
        try:
            if command == "":
                raise InvalidInputError(
                    "(0_0)file name can not be empty(@_@)"
                )
            if not os.path.exists(command + ".pickle"):
                raise InvalidInputError(
                    "(0_0) file " + command + " does not exist (@_@)"
                )
            with open(command + ".pickle", "rb") as saved_game:
                data = pickle.load(saved_game)
            self.leagues = data[0]
            print(
                "($_$)character Sheet loaded from " + command + ".pickle (#_#)"
            )
        except InvalidInputError as err:
            print(err)


class InvalidActionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Invalid Action: " + self.value)


class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Invalid Input: " + self.value)


def main():
    control = Controller()
    control.cmdloop()


if __name__ == '__main__':
    main()
