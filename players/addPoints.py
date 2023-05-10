class Player:
    def __init__(self, name, team, pos, tot_points, round_points, goals, cs):
        self.name = name
        self.team = team
        self.pos = pos
        self.tot_points = tot_points
        self.round_points = round_points
        self.goals = goals
        self.cs = cs
        
class Main:
    def __init__(self):
       self.playerList = list() 

    def add_points(self, name, team, goals, cs):
        for player in self.playerList:
            print(player.name == name)
            print(player.team == team)
            if player.name == name and player.team == team:
                print('points!')
                player.goals += goals
                player.cs += cs
                if goals > 0:
                    if player.pos == "M" or player.pos == "DEF":
                        player.tot_points += goals * 6
                        player.round_points += goals * 6
                    elif player.pos == "MID":
                        player.tot_points += goals * 5
                        player.round_points += goals * 5
                    else:
                        player.tot_points += goals * 4
                        player.round_points += goals * 4
                if cs > 0:
                    if player.pos == "GK" or player.pos == "DEF":
                        player.tot_points += 4
                        player.round_points += 4
                    elif player.pos == "MID":
                        player.tot_points += 1
                        player.round_points += 1
        else:
            print("Player not found")
    
    def print_players_by_attribute(self):
        self.sort_on_points()
        open('playerfile.txt', 'w').close()
        open('teamfile.txt', 'w').close()
        open('posfile.txt', 'w').close()
        open('totpofile.txt', 'w').close()
        open('roundfile.txt', 'w').close()
        open('goalsfile.txt', 'w').close()
        open('csfile.txt', 'w').close()
        playerfile = open('playerfile.txt', 'a')
        teamfile = open('teamfile.txt', 'a')
        posfile = open('posfile.txt', 'a')
        tot_file = open('totpofile.txt', 'a')
        round_file = open('roundfile.txt', 'a')
        goals_file = open('goalsfile.txt', 'a')
        cs_file = open('csfile.txt', 'a')
        for player in self.playerList:
            playerfile.write(player.name + '\n')
            teamfile.write(player.team + '\n')
            posfile.write(player.pos + '\n')
            tot_file.write(player.tot_points + '\n')
            round_file.write(player.round_points + '\n')
            goals_file.write(player.goals + '\n')
            cs_file.write(player.cs + '\n')
        playerfile.close()
        teamfile.close()
        posfile.close()
        tot_file.close()
        round_file.close()
        goals_file.close()
        cs_file.close()


        
    def add_player(self, player, team, pos):
        playerFile = open('players.txt', 'a')
        string = player + ',' + team + ',' +  pos + ',0,0,0,0\n'
        playerFile.write(string)
        playerFile.close()

    def load_players(self):
        playerFile = open("players.txt", "r")
        list = playerFile.readlines()
        playerFile.close()
        for player in list:
            player = player.rstrip('\n').split(',')
            self.playerList.append(Player(player[0].strip(), player[1].strip(), player[2].strip(), int(player[3].strip()), int(player[4].strip()), int(player[5].strip()), int(player[6].strip())))

    
    def sort_on_points(self):
        self.playerList.sort(key = lambda x: x.tot_points, reverse = True)

    def save_points(self):
        playerFile = open("players.txt", "w")
        for player in self.playerList:
            string = player.name + ',' + player.team + ',' +  player.pos + ',0,0,0,0\n'
            playerFile.write(string)
        playerFile.close()

    def mainloop(self):
        self.load_players()
        print('Vad vill du göra?')
        val = input('1. Lägg till spelare \n 2. Lägg till poäng\n')
        if val =='1':
            namn = input('Spelarnamn (max 30 bokstäver): ')
            lag = input('Spelarens lag: ')
            pos = input('Position: ')
            while namn != '#':
                self.add_player(namn, lag, pos)
                print('\n')
                namn = input('Spelarnamn (max 30 bokstäver, avbryt med #, inga å, ä, ö): ')
                lag = input('Spelarens lag (inga å, ä, ö): ')
                pos = input('Position (GK, DEF, MID, ANF): ')

        if val == '2':
            self.load_players()
            namn = input('Spelarnamn (inga å, ä, ö): ')
            lag = input('Spelarens lag (inga å, ä, ö): ')
            while namn != '#':
                goals = input('Antal mål: ')
                nollan = input('Hållen nolla? (1 eller 0): ')
                self.add_points(namn, lag, int(goals), int(nollan))
                print('\n')
                namn = input('Spelarnamn (avbryt med #,1 inga å, ä, ö): ')
                lag = input('Spelarens lag (inga å, ä, ö): ')
            self.sort_on_points()
            self.save_points()
m = Main()
m.mainloop()