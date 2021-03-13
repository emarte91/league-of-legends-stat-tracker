import requests

api_key = ""
summoner_name = str.title("")  # input("Enter in a summoner name: ")


def get_encrypted_summoner_id():
    """
    Fetches encrypted ID from summoner name.
    Needed for further requests.
    """
    id_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(id_url)
    results_json = response.json()
    encrypted_id = results_json['id']
    return encrypted_id


def get_champion_mastery():
    encrypted = get_encrypted_summoner_id()
    mastery_url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + \
                  encrypted + "?api_key=" + api_key
    response = requests.get(mastery_url).json()  # stores response json format
    top_three_champs = [response[0], response[1], response[2]]
    champion_id = {266: "Aatrox",
                   412: "Thresh",
                   23: "Tryndamere",
                   79: "Gragas",
                   69: "Cassiopeia",
                   136: "Aurelion Sol",
                   13: "Ryze",
                   78: "Poppy",
                   14: "Sion",
                   1: "Annie",
                   202: "Jhin",
                   43: "Karma",
                   111: "Nautilus",
                   240: "Kled",
                   99: "Lux",
                   103: "Ahri",
                   2: "Olaf",
                   112: "Viktor",
                   34: "Anivia",
                   27: "Singed",
                   86: "Garen",
                   127: "Lissandra",
                   57: "Maokai",
                   25: "Morgana",
                   28: "Evelynn",
                   105: "Fizz",
                   74: "Heimerdinger",
                   238: "Zed",
                   68: "Rumble",
                   82: "Mordekaiser",
                   37: "Sona",
                   96: "Kog'Maw",
                   55: "Katarina",
                   117: "Lulu",
                   22: "Ashe",
                   30: "Karthus",
                   12: "Alistar",
                   122: "Darius",
                   67: "Vayne",
                   110: "Varus",
                   77: "Udyr",
                   89: "Leona",
                   126: "Jayce",
                   134: "Syndra",
                   80: "Pantheon",
                   92: "Riven",
                   121: "Kha'Zix",
                   42: "Corki",
                   268: "Azir",
                   51: "Caitlyn",
                   76: "Nidalee",
                   85: "Kennen",
                   3: "Galio",
                   45: "Veigar",
                   432: "Bard",
                   150: "Gnar",
                   90: "Malzahar",
                   104: "Graves",
                   254: "Vi",
                   10: "Kayle",
                   39: "Irelia",
                   64: "Lee Sin",
                   420: "Illaoi",
                   60: "Elise",
                   106: "Volibear",
                   20: "Nunu",
                   4: "Twisted Fate",
                   24: "Jax",
                   102: "Shyvana",
                   429: "Kalista",
                   36: "Dr. Mundo",
                   427: "Ivern",
                   131: "Diana",
                   223: "Tahm Kench",
                   63: "Brand",
                   113: "Sejuani",
                   8: "Vladimir",
                   154: "Zac",
                   421: "Rek'Sai",
                   133: "Quinn",
                   84: "Akali",
                   163: "Taliyah",
                   18: "Tristana",
                   120: "Hecarim",
                   15: "Sivir",
                   236: "Lucian",
                   107: "Rengar",
                   19: "Warwick",
                   72: "Skarner",
                   54: "Malphite",
                   157: "Yasuo",
                   101: "Xerath",
                   17: "Teemo",
                   75: "Nasus",
                   58: "Renekton",
                   119: "Draven",
                   35: "Shaco",
                   50: "Swain",
                   91: "Talon",
                   40: "Janna",
                   115: "Ziggs",
                   245: "Ekko",
                   61: "Orianna",
                   114: "Fiora",
                   9: "Fiddlesticks",
                   31: "Cho'Gath",
                   33: "Rammus",
                   7: "LeBlanc",
                   16: "Soraka",
                   26: "Zilean",
                   56: "Nocturne",
                   222: "Jinx",
                   83: "Yorick",
                   6: "Urgot",
                   203: "Kindred",
                   21: "Miss Fortune",
                   62: "Wukong",
                   53: "Blitzcrank",
                   98: "Shen",
                   201: "Braum",
                   5: "Xin Zhao",
                   29: "Twitch",
                   11: "Master Yi",
                   44: "Taric",
                   32: "Amumu",
                   41: "Gangplank",
                   48: "Trundle",
                   38: "Kassadin",
                   161: "Vel'Koz",
                   143: "Zyra",
                   267: "Nami",
                   59: "Jarvan IV",
                   81: "Ezreal"
                   }
    print("Top 3 Champions")
    for champ in top_three_champs:
        champion_name = champion_id.get(champ['championId'])
        champion_level = champ['championLevel']
        mastery_points = champ['championPoints']
        print(champion_name + f" Mastery Level {champion_level} {mastery_points} Mastery Points")


def get_game_stats():
    encrypted = get_encrypted_summoner_id()
    stats_url = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encrypted + "?api_key=" + api_key
    response = requests.get(stats_url).json()
    rd = response[0]  # response is returned as a single element list formatted as a dict. This makes it a dict
    wins = rd['wins']
    losses = rd['losses']
    winrate = int(wins * 100 / (wins + losses))
    print(summoner_name + f" \nRank: {rd['tier']} {rd['rank']} {rd['leaguePoints']} LP \n{wins} Wins  {losses} Losses\nWin rate: {winrate}%")


def temp_menu():
    x = 2 #int(input('Choose an option \n1. Champion Mastery Info\n2. Ranked Stats\n:: '))
    if x == 1:
        get_champion_mastery()
    elif x == 2:
        get_game_stats()


temp_menu()
"""
Things to add 
ladder rank #1020323 top 21%
"""
