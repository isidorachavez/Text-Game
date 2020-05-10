#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Submitted on Fri Oct 18, 2019

@author: Isidora Rose Chavez
"""


"""
DocString:
    
    A) Introduction:
        This storybook-game is about an adventure to get the Forbidden Treasure
        hidden up a castle. First round is a simple multiple-choice question that
        is based on the introduction of the guide, Arthur. It is followed by a 
        training game that is luck-based in damage. It is followed by the player
        choosing an elixir than can change his odds in winning.Last round depends 
        on the elixir of choice and the player battles it out with the boss.
    
        The Forbidden treasure game does not require skill ----but it may need 
        your patience.
        ~NO ANIMALS WERE HARMED IN THE MAKING OF THIS GAME~
        ______________________________________________________________________
        GAME SUMMARY:                                                          
    
        Round 1: Weapon Room - choosing of weapon
        Round 2: Dueling Room - practicing with weapon
        Round 2.5: Elixir choice - not really a game, 2 of the 3 bottles has 
        the life bonus 
        Round 3: Giant  - fighting against the boss, you either have 6 or 8 
        lives based on result of Round 2.5
        ______________________________________________________________________
    
    B) Known Bugs and/or Errors:
        None that I am aware of. However, player can get away with a space as 
        a name or job in setting of global variable.

"""

import random
from random import randint

#Introduction to set name and job
def start():
    global name
    global job
    print("""
                 ✧・ﾟ:* F O R B I D D E N  *  T R E A S U R E*:・ﾟ✧ 
                                    :*G A M E*:
            """)
    input("<press any key to play>\n")
    
    print(""" 
            Ahh a new challenger! My guess is that you are here to seek the 
            Forbidden Treasure. Tell me, what is your name?""")
    name=input("\n")
    
#This requires an input. However, player can get away with a space as a name:(
    while len(name) == 0:
        name=input("<please type a valid name>\n")
    
    print(f"""
            So {name}, what do you do? A smith, carpenter or maybe a minstrel?
            """)
    
#Any job is ok --- the ones mentioned are simply suggestions
    job=input("<enter a job>\n")
    
#This requires an input. However, player can get away with a space as a job:(
    while len(job) == 0:
        job=input("<please type a valid name>\n")
        
    print(f"""
            Okay {name} the {job}, let me tell you about myself:
                        1) I am Arthur, this castle's keeper and your guide today.
                        2) I have an immense love for mead and a terrible fear 
                        of snakes.
                        """)
    input("<press any key to nod>\n")
    
    print(f"""
            ARTHUR: Glad you understand! Oh just a few more things to remember:
                        1) You cannot proceed without me---only I know the way 
                        around here
                        2) The giant brute guards the last door---this is important 
                        to note when choosing your weapon
                        3) And again, I HATE SNAKES!!
                        """)
    input("<press any key to agree>\n")
    
    print("""
            ARTHUR: Alright. Let's enter the first door, shall we?
            """)
    stage_1()
    

#Transition to weapon room
def stage_1():
    print("*you and Arthur open the door*\n*door leads to a hallway*")
    input("<press any key to proceed>\n")
    
    print("*you and Arthur sees a room at the end of the hall*")
    input("<press any key to proceed>\n")
    
    print("""
            ARTHUR: Here we are---the weapons room! Make sure you equip 
            yourself well.
            """)
    weapon_room()

#No losing here except 'snake' option
def weapon_room():
    print("""
                What weapon are you to bring?
                  crossbow 
                  war axe
                  spear  
                  a snake---just because
                  """)

    weapon = input()
    weapon = weapon.lower()
    
#Wrong answer simply goes back to question again
#Correct answer is 'war axe' which leads to next stage
    if "war axe" in weapon:
        print("""
            ARTHUR: A war axe? Excellent choice!
            """)
        stage_3()
        
    elif "crossbow" in weapon:
        print("""
            ARTHUR: Are you sure? Remember, you'll be facing the giant brute.
            """)
        weapon_room()
        
    elif "spear" in weapon:
        print ("""
            ARTHUR:I don't think that will be too helpful.
            """)
        weapon_room()
    
    elif "snake" in weapon:
        print("""
            ARTHUR:@#!$ Are you kidding me?!
            """)
        bye()
        
    else:
        print ("Choose only among the choices!")
        weapon_room()

#Transition stage to Dueling Room
def stage_3():
    input("<press any key to check self out>\n")
    
    print(f"""
                                    ✧・ﾟ:*(◕ヮ◕)*:・ﾟ✧
            ARTHUR: Looking good, {name}. Now let's get moving to the room of duels.
            """)
    input("<press any key to walk down the hall>\n")
    
    print("*you and Arthur reaches the end of a hall and find another room*")
    input("<press any key to go in>\n")

#Another global variable, job, appears   
    print(f"""
            ARTHUR: Aah the dueling room! Being a {job} won't help you here at all.
            We shall train together and put your skills to the test!
            """)
    input("<press any key to nod>\n")
    
    print(f"""
             ARTHUR: Before we start you must know:
                1) Right beats left, left beats middle amd middle beats right
                2) We will finish training once you reduced my health to 0. 
                However, if after our training your health is below 0, you will 
                have to go home----you need to recover!
                3) Do your best, {name}!
                """)
    input("<press any key to start training>\n")
    duel_room()

#While loop is used until objective is met---to defeat Arthur
def duel_room():
    
    Arthur=4
    You=4

    print(f"""
                        ARTHUR'S STARTING HEALTH:{Arthur}
                        YOUR STARTING HEALTH:{You}""")
    while Arthur > 0:
        swing=input("<choose 'a' for left, 'd' for right, 's' for middle>\n")
        swing=swing.lower()
#Arthur's swings are randomized
        a_swing=random.choice("ads")
        if "a" in swing:
            if a_swing == 'a':
                    You -= 0
                    Arthur -= 0
                    print("~Arthur blocks with left~")
                    print("*you received 0 damage*")
                    print("*you dealt 0 damage*")
            elif a_swing == 'd':
                    You -= 0
                    Arthur -= 1
                    print("~Arthur swings right~")
                    print("*you received 0 damage*")
                    print("*you dealt 1 damage*")
            elif a_swing == 's':
                    You -= 1
                    Arthur -= 0
                    print("~Arthur hacks in the middle~")
                    print("*you received 1 damage*")
                    print("*you dealt 0 damage*")
                
        elif "d" in swing:
            if a_swing == 'a':
                    You -= 1
                    Arthur -= 0
                    print("~Arthur swings left~")
                    print("*you received 1 damage*")
                    print("*you dealt 0 damage*")
            elif a_swing == 'd':
                    You -= 0
                    Arthur -= 0
                    print("~Arthur blocks with right~")
                    print("*you received 0 damage*")
                    print("*you dealt 0 damage*")
            elif a_swing == 's':
                    You -= 0
                    Arthur -= 1
                    print("~Arthur hacks in the middle~")
                    print("*you received 0 damage*")
                    print("*you dealt 1 damage*")
        elif "s" in swing:
            if a_swing == 'a':
                    You -= 0
                    Arthur -= 1
                    print("~Arthur swings left~")
                    print("*you received 0 damage*")
                    print("*you dealt 1 damage*")
            elif a_swing == 'd':
                    You -= 1
                    Arthur -= 0
                    print("~Arthur swings right~")
                    print("*you received 1 damage*")
                    print("*you dealt 0 damage*")
            elif a_swing == 's':
                    You -= 0
                    Arthur -= 0
                    print("~Arthur blocks the middle~")
                    print("*you received 0 damage*")
                    print("*you dealt 0 damage*")
        else:
            print("Choose only 'a','d' or 's'!")
            
        print(f"""   
                        ___________________________
                       |ARTHUR'S REMAINING HEALTH:{Arthur}
                       |YOUR REMAINING HEALTH:{You}    
_______________________|___________________________""")

#Less than 1 life causes Arthur to stop the training
        if You < 1:
            break
        
#First, it checks your health. If < 1 then you have to recover
    if You < 1:
        print(f"""
            ARTHUR: Are you ok, {name}? You look tired and must go home.
            """)
        input("<press any key to breath>\n")
        print("""
        
        
                    *you collapse*(X___X)
                    """)
        input("<press any key to recover>\n")
        replay ()

#Second, it checks if your health is > 1 it checks Arthur's if < 1. This should be the case because:
#if Arthur < 1, it will stop the loop above then check if you are < 1. If you are not < 1 then you should be able to trigger Arthur < 1 as this was aready met
    elif Arthur < 1:
        print("""
            ARTHUR: Well done! You are ready!
            """)
        input("<press any key to celebrate> \n *you get 2 health points and 1 attack* ✧( ^◡^)✧ \n")
        print(f"""
            ARTHUR: Hoho. Don't celebrate just yet, {name}.
            """)
        input("<press any key to proceed>\n")

#This is a win and you proceed
        stage_4()
        

#Transition for choosing of elixir
def stage_4():
    
    print("""
            ARTHUR: Muster your courage. You see that lair? He's there.
            """)
    input("<press any key>\n")
    
    print("""
            ARTHUR: He has a health of 8 and you must kill him before he kills
            you. But don't worry I have an elixir for you.
            """)
        
    input("<press enter as Arthur goes through his pocket>\n")
    print("""
            ARTHUR: Uhh..woops I think I got 'em' all mixed up. Just choose one 
            from these. It could be the elixir of life!
            """)
    elixir_choose()

#Elixir choice determines if you get added health
def elixir_choose():

#Choice is only 1, 2 or 3 but effect is random
    elixir=input("<choose 1 or 2 or 3 to drink>\n")
    if "1" in elixir or "2" in elixir or "3" in elixir:
        print("*you drank the elixir*")
    else:
        print("Choose only 1, 2 or 3!")
        elixir_choose()
#Whatever the choice was, effect is random. 2 out of 3 gives added health points
    power= random.choice('xyz')

#Player does not see what is generated. Only x and y are desirable 
    if power == "x":
        print("*you got extra 2 health points*")
        input("<press any key to proceed>ᕙ(⇀‸↼‶)ᕗ\n")
        win()
    elif power == "y":
        print("*you got extra 2 health points*")
        input("<press any key to proceed>ᕙ(⇀‸↼‶)ᕗ\n")
        win()       
    elif power == "z":
        print("""
            ARTHUR: So that's where my mead went!! Let me have some! 
            *gets the remaining elixirs*""")
        input("<press any key>\n")
        print("""
            ARTHUR: Those weren't mead...But I do feel stronger!! Sorry about 
            that.""")
        lose()

#Elixir choice x and y lead to this
def win():
    print("""
            ARTHUR: So strong! You should be able to defeat the giant now!
            """)
    input("<press any key to flex>\n")
    print("""
    
    *out of nowhere*
    
                :#####:::'########:'::#####:: ##::::'##: ########:
              '##... ##:: ::.##..:: :##...##: ###:'::##: ::.##..::
               ##:::..::: :::##:::: :##:::##: ####:::##: :::##::::
               ##:: ####: :::##:::: ######### #####::##: :::##::::
               ##::: ##:: ::.##:::: ##...::## ##::##:##: ::.##::::
               ##::: ##:: :::##:::: ##:::::## ##:::####' :::##::::
              . ######::: ########: ##:::::## ##::::###. :::##::::
           
           ARTHUR: LOOK OUT!""")

#u is player's life. From 6 it is upgraded to 8
    g = 8
    u = 8
    
#Loop will go on until giant is alive
    while g > 0:
        hit=input("<choose 'a' for left, 'd' for right, 's' for middle>\n")
        hit=hit.lower()

#Giant's damage is randomized 
        g_hit=random.choice("ads")
        if u < 1:
            break
        if "a" in hit:
            if g_hit == 'a':
                u -= 0
                g -= 0
                print("~Giant blocks with left~")
                print("*you received 0 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 'd':
                u -= 0
                g -= 2
                print("~Giant swings right~")
                print("*you received 0 damage*")
                print("*you dealt 2 damage*")
            elif g_hit == 's':
                u -= 2
                g -= 0
                print("~Giant hacks in the middle~")
                print("*you received 2 damage*")
                print("*you dealt 0 damage*")
                
        elif "d" in hit:
            if g_hit == 'a':
                u -= 2
                g -= 0
                print("~Giant swings left~")
                print("*you received 2 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 'd':
                u -= 0
                g -= 0
                print("~Giant blocks with right~")
                print("*you received 0 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 's':
                u -= 0
                g -= 2
                print("~Giant hacks in the middle~")
                print("*you received 0 damage*")
                print("*you dealt 2 damage*")
        elif "s" in hit:
            if g_hit == 'a':
                u -= 0
                g -= 2
                print("~Giant swings left~")
                print("*you received 0 damage*")
                print("*you dealt 2 damage*")
            elif g_hit == 'd':
                u -= 2
                g -= 0
                print("~Giant swings right~")
                print("*you received 2 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 's':
                u -= 0
                g -= 0
                print("~Giant blocks the middle~")
                print("*you received 0 damage*")
                print("*you dealt 0 damage*")
        else:
            print("Choose only 'a','d' or 's'!")

#Health is displayed based on damage dealt by each           
        print(f"""   
                        ___________________________
                       |GIANT'S REMAINING HEALTH:{g}
                       |YOUR REMAINING HEALTH:{u}    
_______________________|___________________________""")
#Loop breaks too if your life is below 1
        if u < 1:
            break
#You die if loop breaks and your health < 1   
    if u < 1:
        print(f"""
            ARTHUR: {name}!! NOOooooo!!!
            """)
        input("<press any key>\n")
        print("""
        
                          XxYOU DIEDxX
              
              """)
        input("<press any key to see epitaph>\n")
        print(f"""
        
                ~In the loving memory of {name}.
                        the greatest {job}~
                             ______
                       _____/      \\_____
                      |  _     ___   _   ||
                      | | \     |   | \  ||
                      | |  |    |   |  | ||
                      | |_/     |   |_/  ||
                      | | \     |   |    ||
                      | |  \    |   |    ||
                      | |   \. _|_. | .  ||
                      |                  ||
                .................................
        """)

#You can replay
        replay()
    
#Proceeds to winning stage if your life is not < 1 and Giant is dead
    elif g < 1:
        stage_5()

#Elixir choice z leads to this
def lose():
    print("""
            ARTHUR: It's okay. You can still defeat the giant.
            """)
    input("<press any key to flex>\n")
    print("""
    
    *out of nowhere*
    
                :#####:::'########:'::#####:: ##::::'##: ########:
              '##... ##:: ::.##..:: :##...##: ###:'::##: ::.##..::
               ##:::..::: :::##:::: :##:::##: ####:::##: :::##::::
               ##:: ####: :::##:::: ######### #####::##: :::##::::
               ##::: ##:: ::.##:::: ##...::## ##::##:##: ::.##::::
               ##::: ##:: :::##:::: ##:::::## ##:::####' :::##::::
              . ######::: ########: ##:::::## ##::::###. :::##::::
           
           ARTHUR: LOOK OUT!""")

#Your life stays at 6   
    g = 8
    u = 6
    while g > 0:
        hit=input("<choose 'a' for left, 'd' for right, 's' for middle>\n")
        hit=hit.lower()
        g_hit=random.choice("ads")
        if u < 1:
            break
        if "a" in hit:
            if g_hit == 'a':
                u -= 0
                g -= 0
                print("~Giant blocks with left~")
                print("*you received 0 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 'd':
                u -= 0
                g -= 2
                print("~Giant swings right~")
                print("*you received 0 damage*")
                print("*you dealt 2 damage*")
            elif g_hit == 's':
                u -= 2
                g -= 0
                print("~Giant hacks in the middle~")
                print("*you received 2 damage*")
                print("*you dealt 0 damage*")
                
        elif "d" in hit:
            if g_hit == 'a':
                u -= 2
                g -= 0
                print("~Giant swings left~")
                print("*you received 2 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 'd':
                u -= 0
                g -= 0
                print("~Giant blocks with right~")
                print("*you received 0 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 's':
                u -= 0
                g -= 2
                print("~Giant hacks in the middle~")
                print("*you received 0 damage*")
                print("*you dealt 2 damage*")
        elif "s" in hit:
            if g_hit == 'a':
                u -= 0
                g -= 2
                print("~Giant swings left~")
                print("*you received 0 damage*")
                print("*you dealt 2 damage*")
            elif g_hit == 'd':
                u -= 2
                g -= 0
                print("~Giant swings right~")
                print("*you received 2 damage*")
                print("*you dealt 0 damage*")
            elif g_hit == 's':
                u -= 0
                g -= 0
                print("~Giant blocks the middle~")
                print("*you received 0 damage*")
                print("*you dealt 0 damage*")
        else:
            print("Choose only 'a','d' or 's'!")
#Health is displayed based on damage dealt by each             
        print(f"""   
                        ___________________________
                       |GIANT'S REMAINING HEALTH:{g}
                       |YOUR REMAINING HEALTH:{u}    
_______________________|___________________________""")
#Loop also ends when your life is <1
        if u < 1:
            break
#You die if loop breaks and your health < 1            
    if u < 1:
        print(f"""
            ARTHUR: {name}!! NOOooooo!!!
            """)
        input("<press any key>\n")
        print("""
        
                          XxYOU DIEDxX
              
              """)
        input("<press any key to see epitaph>\n")
        print(f"""
        
                ~In the loving memory of {name}.
                      the greatest {job}~
                             ______
                       _____/      \\_____
                      |  _     ___   _   ||
                      | | \     |   | \  ||
                      | |  |    |   |  | ||
                      | |_/     |   |_/  ||
                      | | \     |   |    ||
                      | |  \    |   |    ||
                      | |   \. _|_. | .  ||
                      |                  ||
                .................................
        """)
        replay()
    elif g < 1:
        stage_5()
    
#Winning stage!! This means you are lucky mostly.        
def stage_5():
    print(f"""
            ARTHUR: WOW I did not expect that!!
            You did it,{name} ! You really deserve that  ･*. ☆ﾟtreasure!☆ﾟ. * ･
            """)
    input("<press any key to unlock the final door>\n")
    print("""
                ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    
                   _   _   _   _   _   _   _   _        
                  / \ / \ / \ / \ / \ / \ / \ / \   
                 ( T | R | E | A | S | U | R | E )
                  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                  
                ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
 
            ARTHUR: There it is!! And it's all yours!""")
    input("<press any key to pick up treasure>\n")
    print(f"""
            ARTHUR: You should celebrate! Here, take this extra gift from me:
                            ✧・ﾟ:*fancy bottle of mead*:・ﾟ✧
            """)
    input("<press any key to accept>\n")

#You win but you can still replay
    print("""
           
            ARTHUR: Will you come and visit me again, friend?""")
    replay()
    
def replay():
#This outlining of replay option is made to make it visible to players
    print("""
______________
REPLAY OR NOT?|
______________|__________________________________
    """)
    replay=input("<press y to replay>\n")
#Makes response uniform by lowercasing    
    replay=replay.lower()
#Goes back to start of game    
    if "y" in replay:
        start()
#Otherwise exits
    else:
        print("""
            ARTHUR: Alright, good luck on your next quest then!""")
        exit(0)    
    
#No chance of replay    
def bye():
    print("""
            ARTHUR: STAY AWAY FROM MY CASTLE!!""")
    print("*Arthur kicks you out of the castle*")
    input("<press any key>\n")
    print("~Better luck on your next quest!~")
    exit(0)
    
    
    
start()

