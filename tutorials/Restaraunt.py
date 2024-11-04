class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + ' menu available from ' + str(self.start_time) + ' hours to ' + str(self.end_time) + ' hours'

    def calculate_bill(self, purchased_items):
        total = 0
        for each in purchased_items:
            total += each
        # print(total)


brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

brunch = Menu("brunch", brunch_items, 11, 16)
early_bird = Menu("early_bird", early_bird_items, 15, 18)
dinner = Menu("dinner", dinner_items, 17, 23)
kids = Menu("kids", kids_items, 11, 21)
arepas = Menu("arepas", arepas_menu, 10, 20)

class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return 'Franchise address: ' + str(self.address)

    def available_menus(self, time):
        updated_menu = []
        # for each in self.menus:
        #   if time >= each.start_time and time < each.end_time:
        #     updated_menu.append(each)
        # return updated_menu
        # return [each for each in self.menus if time >= each.start_time and time < each.end_time]
        updated_menu = []
        index = 0

        while index < len(self.menus):
            each = self.menus[index]
            if time >= each.start_time and time < each.end_time:
                updated_menu.append(each)
            index += 1
        return updated_menu


flagship_store = Franchise(address="1232 West End Road", menus=[brunch, early_bird, dinner, kids])
new_installment = Franchise(address="12 East Mulberry Street", menus=[brunch, early_bird, dinner, kids])
arepas_place = Franchise(address="189 Fitzgerald Avenue", menus=[arepas])

print(flagship_store.available_menus(17))


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


arepa = Business("Basta Fazoolin \' with my heart", [flagship_store, new_installment])
print(arepa.franchises[0].menus[2])