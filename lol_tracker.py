import requests

api_key = ""


def get_encrypted_summoner_id():
    summoner_name = "dominicanpapi69" # turn this into an input
    id_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(id_url)
    results_json = response.json()
    encrypted_id = results_json['id']
    return encrypted_id


def get_champion_mastery():
    encrypted = get_encrypted_summoner_id()
    mastery_url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + encrypted + "?api_key=" + api_key
    response = requests.get(mastery_url)
    response_results = response.json()
    highest_mastery_champion = response_results[0] #stored as dict
    champion_level = str(highest_mastery_champion['championLevel'])
    if highest_mastery_champion['championId'] == 11:
        print("Master Yi: Mastery Level " + champion_level)
    #elif champion_id == "2":
    #    print("Olaf: Mastery Level " + champion_level)


get_champion_mastery()

# Work in progress
