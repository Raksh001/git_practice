letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points ={}
for key,value in zip(letters,points):
  letter_to_points[key] = value
letter_to_points[""]= 0
# print(letter_to_points)

def score_word(word):
  point_total = 0

  for each_letter in word:
    # print(each_letter)
    if each_letter in letter_to_points.keys():
      value = letter_to_points.get(each_letter)
      point_total += value
    else:
      point_total += 0
  # print(point_total)
  return point_total

brownie_points = score_word("BROWNIE")

player_to_words = {"player1": {"BLUE", "TENNIS", "EXIT"},
"wordNerd": {"EARTH", "EYES", "MACHINE"}, "Lexi Con": {"ERASER", "BELLY", "HUSKY"}, "Prof Reader": {"ZAP", "COMA", "PERIOD"}}

player_to_points = {}

def update_point_totals():
  for player,words in player_to_words.items():
  # print(player, "!!!", words)
    player_points = 0
    for each_word in words:
      # print("Before", player_points)
      player_points += score_word(each_word)
    print("Final Points: for {} is {} ".format(player,player_points))

def play_word(player,word):
  # player_to_words[player] = word
  list_from_dict = list(player_to_words.items())
  list_from_dict.append({player: word})
  return list_from_dict

print(play_word("player1", "BASH"))