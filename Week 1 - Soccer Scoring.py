container = [x.strip().split() for x in open("commentary.txt", "r")]
team1, foo, team2 = container.pop(0)
teams = [line[0] for line in container]
team1Count = teams.count(team1)
team2Count = teams.count(team2)
if team1Count > team2Count:
    print(team1, team1Count)
    print(team2, team2Count)
else:
    print(team2, team2Count)
    print(team1, team1Count)

