# 15. Sports Management
# Player
# CricketPlayer
# Captain(CricketPlayer)

# Add captain-specific functionality.

class Player:
    def play(self):
        print("Player is playing")

class CricketPlayer(Player):
    def batting(self):
        print("Cricket player is batting")

class Captain(CricketPlayer):
    def captaincy(self):
        print("Captain is leading the team")

c = Captain()

c.play()
c.batting()
c.captaincy()