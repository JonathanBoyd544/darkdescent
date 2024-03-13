###### Easter Egg NPC 1 [Jack] ######

def incantation():
  a_string = input("Enter incantation: ").lower()
  matches = ["fire", "echo", "footsteps"]

  if all(x in a_string for x in matches):
    print("Unlocked!!")

  else:
    print("Wrong incantation. Please try again.")
    incantation()

print("Jack the adventurer is sitting in the corner of the room, carving tick marks into the wall. You can see there is alot of them. He has clearly been here awhile.\n")

greet = input("Would you like to talk with Jack? (Yes/No)\n>>> ").lower()
if greet.startswith("y"):
  interaction = input("You walk over to Jack and he looks up at you. He says, 'Oh, Hello! You scared me! I thought I was alone down here!'\n1) I'm sorry, I didn't mean to scare you. I just wanted to see if you were ok\n2) Ha! Your such a wimp! I was just standing here.\n>>> ")
  if interaction == "1":
    interaction2 = input("Jack looks at you with a sad expression on his face. 'He says, Its alright. I have just been alone down here for so long. I didn't expect to see anyone else.'\n1) How long have you been down here?\n2) Well it was nice meeting you. I hope you find your way out.\n>>> ")
    if interaction2 == "1":
      interaction3 = input("About 6 weeks. But I have no way to tell time so it could be much longer than that. I have given up all hope.\n1) Give Jack a return to village spell\n2) Wish him luck and continue on your adventure\n>>> ")
      if interaction3 == "1":
        print("You tell Jack you can return him to the village at the entrance of the dungeon. His face lights up with a smile. 'Thank you friend! Before I go, I leave you with this wisdom':\n\nIm not alive, but I can grow. I dont have lungs, but I need air.\nThe more you take, the more you leave behind\nI speak without a mouth and hear without ears. I have no body, but I come alive with the wind.\n\nYou thank Jack for the confusing wisdom and cast the spell on him. In a flash of light, Jack is gone")
        pass
        if interaction3 == "2":
          print("You wish Jack the best of luck and continue on your journey.")
          pass
  elif interaction == "2":
    print("Jack suddenly looks angry. Then He starts to cry. You dont care. you turn around and you suddenly feel a sharp pain in your chest. You look down and see a knife stabbing through your chest. He stabbed you! You turn around and he is gone. You take 15 damage")
    pass
  
  elif interaction == "3":
    pass


    

  
    
if greet.startswith("n"):
  pass
  print("passed")
  
incantation()

