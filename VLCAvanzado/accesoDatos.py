import xml.etree.ElementTree as ET



def libreriaXML(data, xmlns):
    tree = ET.parse(data)
    root = tree.getroot()

    listaCanciones = root.find("xmlns:trackList", xmlns)

    libreria = {track.find("xmlns:title", xmlns).text:
                    {
                        "artista": track.find("xmlns:creator", xmlns).text,
                        "album": track.find("xmlns:album", xmlns).text,
                        "location": track.find("xmlns:location", xmlns).text
                    }
                    for track in listaCanciones
    }
    return libreria





if __name__ == "__main__":
    '''
    libreria = {"California_Uber_Alles.mp3":
                    {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys",
                     "location": ".\\biblioteca\\California_Uber_Alles.mp3"},
                "Seattle_Party":
                    {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets",
                     "location": ".\\biblioteca\\Seattle_Party.flac"},
                "King_Kunta":
                    {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly",
                     "location": ".\\biblioteca\\King_Kunta.mp3"}
                }
    '''

    data = "libreria.xml"