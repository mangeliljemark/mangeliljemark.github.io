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
    
    def print_players_by_attribute(self):
        open('spelare.txt', 'w').close()
        open('lag.txt', 'w').close()
        open('position.txt', 'w').close()
        open('total.txt', 'w').close()
        open('round.txt', 'w').close()
        open('goals.txt', 'w').close()
        open('cs.txt', 'w').close()
        playerfile = open('spelare.txt', 'a')
        teamfile = open('lag.txt', 'a')
        posfile = open('position.txt', 'a')
        tot_file = open('total.txt', 'a')
        round_file = open('round.txt', 'a')
        goals_file = open('goals.txt', 'a')
        cs_file = open('cs.txt', 'a')
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
        playerFile = open("players.txt", "r+")
        list = playerFile.readlines()
        playerFile.close()
        for player in list:
            player = player.rstrip('\n').split(',')
            self.playerList.append(Player(player[0].strip(), player[1].strip(), player[2].strip(), int(player[3].strip()), int(player[4].strip()), int(player[5].strip()), int(player[6].strip())))

    
    def sort_on_points(self):
        self.playerList.sort(key = lambda x: x.tot_points, reverse = True)

    def save_points(self):
        open('players.txt', 'w').close()
        playerFile = open("players.txt", "a")
        self.sort_on_points()
        for player in self.playerList:
            string = player.name + ',' + player.team + ',' +  player.pos + ',' + str(player.tot_points) + ',' + str(player.round_points) + ',' + str(player.goals) + ',' + str(player.cs) + '\n'
            playerFile.write(string)
        playerFile.close()


    def add_loop(self):
        namn = input('Spelarnamn (avbryt med #, inga å, ä, ö): ')
        while namn != '#':
            lag = input('Spelarens lag (inga å, ä, ö): ')
            pos = input('Position (GK, DEF, MID, ANF): ')
            self.add_player(namn, lag, pos)
            print('\n')
            namn = input('Spelarnamn (avbryt med #, inga å, ä, ö): ')

    def add_points(self, name, team, goals):
        for player in self.playerList:
            if player.name == name and player.team == team:
                player.goals += goals
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

    def add_cs(self, lag):
        for player in self.playerList:
            if player.team == lag:
                if player.pos == "GK" or player.pos == "DEF":
                        player.tot_points += 4
                        player.round_points += 4
                elif player.pos == "MID":
                    player.tot_points += 1
                    player.round_points += 1


    def mainloop(self):
        self.load_players()
        print('Gjorda mål')
        namn = input('Målskytt (avbryt med #): ')
        while namn != '#':
            lag = input('Lag: ')
            goals = input('Antal mål: ')
            self.add_points(namn, lag, goals)
            namn = input('Målskytt (avbryt med #): ')
        
        print('Hållna nollor')
        lag = input('Lag (avbryt med #): ')
        while lag != '#':
            self.add_cs(lag)
            lag = input('Lag (avbryt med #): ')
        
        print('Sorterar på totala poäng')
        self.sort_on_points()

        self.print_players_by_attribute()
        self.save_points()


        
m = Main()
m.add_loop()
