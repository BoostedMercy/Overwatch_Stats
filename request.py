import requests
import json

# Written by Matt
print("Testing the commits")


def getAll(plt, svr, tag):  # Grabs all possible stats about a player (Large file size)
    r = requests.get(f"https://ow-api.com/v1/stats/{plt}/{svr}/{tag}/complete")

    prof = r.json()  # Prof aka profile.
    if len(prof) == 1:  # The Dictionary Length is 1 if there is an error code.
        return "Profile Not Found!"
    else:
        return prof


def getHero(plt, svr, tag, hero):  # Shows all stats about a players hero (includes separate ranks for roles)
    heroes = ["Ashe", "Bastion", "Doomfist", "Genji", "Hanzo", "Junkrat", "McCree", "Mei", "Pharah", "Reaper",
              "Soldier 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker", "D.va", "Orisa", "Reinhardt",
              "Roadhog", "Sigma", "Winston", "Wrecking-ball", "Zarya", "Ana", "Baptiste", "Brigitte", "Lucio", "Mercy",
              "Moira", "Zenyatta"]
    Valid = False
    for h in heroes:
        if h.lower() == hero:
            Valid = True
            r = requests.get(f"https://ow-api.com/v1/stats/{plt}/{svr}/{tag}/heroes/{hero}")
            prof = r.json()
            if len(prof) == 1:
                return "Profile Not Found!"
            else:
                if prof["quickPlayStats"]["careerStats"] == "null":  # Stats show as null if private
                    return "Private Profile"
                else:
                    return prof
    if not Valid:
        return "Not a valid Hero"


def leaderBoard():
    with open("TestData.json", "r") as j:
        z = json.load(j)
        statBoard = []
        for player in range(len(z)):
            if len(statBoard) == 0:
                statBoard.append([z[str(player)]["name"], z[str(player)]["rating"]])
            else:
                completed = False
                for item in range(len(statBoard)):
                    try:
                        plr = str(player)
                        if statBoard[item][0] == z[str(player)]["name"]:
                            statBoard.pop(item)
                        elif statBoard[item][1] < z[str(player)]["rating"] and not completed:
                            statBoard.insert([z[plr]["name"], z[plr]["rating"]], item)
                            completed = True
                    except KeyError:
                        pass
                if not completed:
                    statBoard.append([z[str(player)]["name"], z[str(player)]["rating"]])

        return statBoard  # statBoard[row][column]


def SaveData(data):
    if type(data) != str:  # Checking an error hasn't occurred (Private profile, server down, etc.)
        with open("TestData.json", "r") as j:
            try:
                CurrentDict = json.load(j)
                Saved = False
                for x in range(len(CurrentDict)):
                    if data["name"] == CurrentDict[str(x)]["name"]:  # Checks if user is already in the database
                        Saved = True
                        CurrentDict[str(x)] = data  # If so, replace that slot.
                if not Saved:
                    CurrentDict[str(len(CurrentDict))] = data
            except json.decoder.JSONDecodeError:
                print("Empty Dict... Creating JSON Structure ")
                CurrentDict = {0: data}

        with open("TestData.json", "w") as j:
            json.dump(CurrentDict, j, indent=4)
    else:
        print(data)


# For testing and is also an example of how to use functions in cmdline.
goodTag = False
while not goodTag:
    inputTag = input("Input your battletag: ")
    temp = inputTag.split("#")
    try:
        linkTag = (temp[0] + "-" + temp[1])  # Converting the # into an -, which the API uses
        goodTag = True
    except IndexError:
        print("Invalid Format")

SaveData(getAll("pc", "eu", linkTag))  # Saves the data from the getAll command to the json file.
leaderBoard()  # Displays leaderboard of saved users, ordered by SR
