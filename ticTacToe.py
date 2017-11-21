def main():
	dict= {"1": "1" , "2":  "2", "3": "3", 
	"4": "4", "5":  "5", "6": "6", 
	"7": "7", "8": "8", "9": "9"}
	
	while True:
		player_turn(dict, "X") #this makes the player take a turn
		player_turn(dict, "O")
	
	return
	
def boardPrint(dict): 
	print(dict["1"] + ' | ' + dict["2"] + ' | ' + dict["3"])
	print("-" * 10) 
	print(dict["4"] + ' | ' + dict["5"] + ' | ' + dict["6"])
	print("-" * 10)
	print(dict["7"] + ' | ' + dict["8"] + ' | ' + dict["9"])
	print()
	return

def player_turn(dict, player):
	boardPrint(dict)
	var = input("What position would you like to place your character? ")
	
	while True:
		try:
			if int(var) in range(1,10) and len(var) == 1 and var != 0:
				if dict[var] == "X" or dict[var] == "O":
					var = input('Postion taken please try again :( ')
				else:
					dict[var] = player 
					
					break
		except:
			var = input("Bad character please try again!")
	return
	
main()
