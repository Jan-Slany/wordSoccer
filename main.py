import random

print('''
 __          __           _                               
 \\ \\        / /          | |                              
  \\ \\  /\\  / /__  _ __ __| |  ___  ___   ___ ___ ___ _ __ 
   \\ \\/  \\/ / _ \\| '__/ _` | / __|/ _ \\ / __/ __/ _ \\ '__|
    \\  /\\  / (_) | | | (_| | \\__ \\ (_) | (_| (_|  __/ |   
     \\/  \\/ \\___/|_|  \\__,_| |___/\\___/ \\___\\___\\___|_|                                                                                                                   
           _   
          |.|        
          ]^[       
        /~`-'~\\    
       {<|%  |>}   -kick off
        \\|___|/    
       /\\    \\      
       |/>/|__\\    
      _|)   \\ |   
     (_,|    \\)   
     / \\     (|_  
  .,.\\_/,...,|,_)
    ''')

user_input = input()

file = open("words.txt", "r")
words = file.read().splitlines()

last_character = user_input[-1]

used_words = []
score = 0

while True:

    if user_input in words:
        if not user_input in used_words:
            # počítačem náhodně generované slovo
            computer_list = [index for index in words if index[0] == last_character]
            computer_word = random.choice(computer_list)
            print(computer_word)
            # poslední písmeno slova od počítače
            last_character = computer_word[-1]

            # použitá slova
            used_words.append(computer_word)
            used_words.append(user_input)
            user_input = input()

            if user_input.startswith(last_character):
                # poslední písmeno hráče
                last_character = user_input[-1]
                # přičtení bodu
                score += 1
            else:
                print("\nThis word is not starting with correct letter!\nYou'r score was: "+str(score))
                break
        else:
            print("\nThis word has already been used!\nYou'r score was: "+str(score))
            break
    else: 
        print("\nThis word is not in the list!\nYou'r score was: "+str(score))
        break
