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
    def add_points(self, player, team, goals, cs):
        for player in self.playerList:
            if player.name == player and player.team == team:
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
        
    def add_player(self, player, team, pos):
        playerFile = open('players.txt', 'a', 'utf-8')
        player = player + ' '*int(30-len(player))+ ','
        team = team + ' '*int(20-len(team))+ ','
        pos = ' '*int(5-len(pos)) + pos + ' '*int(5-len(pos))+ ','
        string = player + team + pos + '  0  ,' + '  0  ,' + '  0  ,' + '  0  \n'
        playerFile.write(string)

    def load_players(self):
        playerFile = open("players.txt", "r", 'utf-8')
        list = playerFile.readlines().rstrip('\n')
        playerFile.close()
        for player in list:
            player = player.split(',').strip()
            self.playerList.append(Player(player[0], player[1], player[2], player[3], player[4], player[5], player[6]))

    
    def sort_on_points(self):
        self.playerList.sort(key = lambda x: x.tot_points, reverse = True)

    def save_points(self):
        playerFile = open("players.txt", "w", 'utf-8')
        for player in self.playerList:
            playerFile.write(player.name + "," + player.team + "," + player.pos + "," + player.tot_points + "," + player.round_points + "," + player.goals + "," + player.cs + "\n")
        playerFile.close()

    def mainloop(self):
        print('Vad vill du göra?')
        val = input('1. Lägg till spelare \n 2. Lägg till poäng\n')
        if val =='1':
            namn = input('Spelarnamn (max 30 bokstäver): ')
            lag = input('Spelarens lag: ')
            pos = input('Position: ')
            while namn != '#':
                self.add_player(namn, lag, pos)
                print('\n')
                namn = input('Spelarnamn (max 30 bokstäver, avbryt med #): ')
                lag = input('Spelarens lag: ')
                pos = input('Position: ')

        if val == '2':
            self.load_players()
            namn = input('Spelarnamn: ')
            lag = input('Spelarens lag: ')
            while namn != '#':
                goals = input('Antal mål: ')
                nollan = input('Hållen nolla? (1 eller 0): ')
                self.add_points(namn, lag, int(goals), int(nollan))
                print('\n')
                namn = input('Spelarnamn (avbryt med #): ')
                lag = input('Spelarens lag: ')
            self.sort_on_points()
            self.save_points()
m = Main()
m.mainloop()