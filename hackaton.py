hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_pos(number):
    pos_arr = ['winner!', '2nd place.', '3rd place.', 'th place.']
    if(number <= 3):
        return pos_arr[number-1]
    
    return f'{number}{pos_arr[3]}'

def get_score (team, tournament):
    counter = 0
    for e in tournament:
        counter += 1
        if(team == e):
            return f'{team} was the {get_pos(counter)}'


print(get_score("Team Kenzie", hackathon_1))
#Team Ateliware was winner!

print(get_score("Team Mirum", hackathon_2))
#Team Mirum was the 4th place.

print(get_score("Team Kenzie", hackathon_3))
#Team Kenzie was the 4th place.