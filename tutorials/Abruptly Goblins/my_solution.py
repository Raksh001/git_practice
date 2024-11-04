gamers = []
gamer = {"name" : "availability"}

def add_gamer(gamer, gamers_list):
    # print(gamer)
    if gamer.get('name') and gamer.get('availibility'):
        gamers_list.append(gamer)
        print(gamer)
    # return gamers_list

kimberly = {"name": "Kimberly Warner", "availability": ["Mondays", "Tuesdays", "Fridays"]}
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
add_gamer(kimberly, gamers)
print(gamers)

def build_daily_frequency_table():
    count_availability = 0
    gamers.keys()
    return
