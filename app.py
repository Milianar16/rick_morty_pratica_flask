from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)

#rota

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)


    location_url = dict['location']['url']
    location_response = urllib.request.urlopen(location_url)
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    dict['location'] = location_dict

    episodes= []

    for episode_url in dict['episode']:
     episode_response = urllib.request.urlopen(episode_url)
     episode_data = episode_response.read()
     episode_dict = json.loads(episode_data)
     episodes.append(episode_dict)

    dict['episodes'] = episodes

    return render_template("profile.html", profile=dict)


@app.route("/locations")
def get_list_location():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    location_data = json.loads(data)

    locations = []

    for location in location_data["results"]:
        location_info = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"]
        }

        locations.append(location_info)

    return render_template("locations.html", locations=locations)

@app.route("/location/<id>")
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    location = json.loads(data)

    characters=[]

    for char_url in location['residents']:
        char_response = urllib.request.urlopen(char_url)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters.append(char_dict)

    location['characters'] = characters

    return render_template("location.html", location=location)



@app.route("/episodes")
def get_list_episode():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes=[]

    for episode in dict['results']:
        episode = {
            "id": episode["id"],
            "name":episode["name"],
            "air_date":episode["air_date"],
            "episode":episode["episode"]
        }

        episodes.append(episode)

    return render_template("episodes.html", episodes=episodes)

@app.route("/episode/<id>")
def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episode = json.loads(data)

    characters = []

    for char_url in episode['characters']:
        char_response = urllib.request.urlopen(char_url)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters.append(char_dict)
    episode['characters'] = characters


    return render_template("episode.html", episode=episode)

@app.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name":character ["name"],
            "status":character["status"],
            "location":character["location"],
            "type":character["type"]
        }
        characters.append(character)

    return {"characters":characters}


