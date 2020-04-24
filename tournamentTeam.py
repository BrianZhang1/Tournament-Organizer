n = int(input("Amount Of Teams: "))
matchups = [[], [], [], [], []]  # A list with 5 lists for each round
teams = [0, []]

for num in range(n):
    if not(num == 0):
        teams[1].append(num)  # Assigning teams to a list

for rounds in range(5):
    teams[1] = [teams[1][-1]] + teams[1][:-1]

    for team in range(int((len(teams[1])-1)/2)):
        matchups[rounds].append(teams[1][team + 1])
        matchups[rounds].append(teams[1][-team - 1])
    matchups[rounds].append(teams[0])
    matchups[rounds].append(teams[1][0])

matchupText = []

for rounds in range(5):
    tempString = ""
    for pair in range(int((len(teams[1]) + 1)/2)):
        tempString += "Team " + str(matchups[rounds][pair * 2]) + " vs. " + "Team " + str(matchups[rounds][pair * 2 + 1]) + " | "
    matchupText.append(tempString)
print("")
print("*****************************************************************************************")
print("Results:")
print("*****************************************************************************************")

for i in range(5):
    print("")
    print("Round " + str(i))
    print("*****************************************************************************************")
    print(matchupText[i])
    print("*****************************************************************************************")
