hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_pos(number):
    if(number == 1):
        return '1st'
    if(number == 2):
        return '2nd'
    if(number == 3):
        return '3rd'
    return f'{number}th'

def get_score (team, tournament):
    counter = 0
    for e in tournament:
        counter += 1
        if(team == e):
            return f'{team} was the {get_pos(counter)}'


print(get_score("Team Ateliware", hackathon_1))
#Team Ateliware was the 2nd

print(get_score("Team Mirum", hackathon_2))
#Team Mirum was the 4th

print(get_score("Team Kenzie", hackathon_3))
#Team Kenzie was the 4th