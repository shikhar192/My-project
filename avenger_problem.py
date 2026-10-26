# Avengers Problem: Given a list of powers of avengers in which we divide them into two teams
# show which avenger team has more power and the difference in power between the two teams
N =list(map(int, input("enter powers:").split()))
powers = N
print(powers)
team_a_power =0 # iron man team
team_b_power =0 # captain america team

#sort the powers

powers.sort(key=lambda x: (abs(x),-x))
print(powers)
#assign avengers to teams alternatively
ironman_turn = True

for power in powers:
    if ironman_turn:
        team_a_power += power

    else:
        team_b_power += power

    ironman_turn = not ironman_turn

power_difference = abs(team_a_power - team_b_power)
print(power_difference)

print("iron man team power:", team_a_power)
print("captain america team power:", team_b_power)
