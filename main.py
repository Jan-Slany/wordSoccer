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

used_words = []
score = 0

while True:

    if user_input in words:
        if not user_input in used_words:
            last_character = user_input[-1]

            used_words.append(user_input)
            user_input = input()

            if user_input.startswith(last_character):
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
