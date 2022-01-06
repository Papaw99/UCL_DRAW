import sqlite3

class Team:
    def __init__(self, name, league, group):
        self.name = name
        self.league = league
        self.group = group

    def getName (self):
        return self.name
    
    def getLeague (self):
        return self.league

    def getGroup (self):
        return self.group    

    def setName (self, name):
        self.name = name

    def setLeague (self, league):
        self.league = league

    def setGroup (self, group):
        self.group = group 
    
    def addTeam (self, team):
        name = team.getName()
        league = team.getLeague()
        group = team.getGroup()

