# Returns where a player is on the leaderboard based on their scores each time

def climbingLeaderboard(ranked, player):
    ranks = []
    for i in range(len(player)):
        result = len(ranked)+1
        for x in range(len(ranked)):
            if player[i] >= ranked[x]:
                result = x+1
                break
                # exits nested for loop
        ranks.append(result)
    return ranks
    
ranked = input("Scores on Leaderboard (decreasing order): ")
ranked = set(ranked.split())
ranked = list(map(int, list(ranked)))
ranked.sort(reverse = True)
player = input("Game scores (ascending order): ").split()
player = list(map(int, list(player)))

print(climbingLeaderboard(ranked, player))
