import yagmail
import random
import logging
try:
    yag = yagmail.SMTP(user='farhanmushtaque13@gmail.com',password = "idon'tlikeCoding$",soft_email_validation=False,smtp_ssl=False,smtp_starttls=True)
    messages = {
        curse_one:'never fails to make your day worse, no matter how bright. if you have found yourself thinking "geez, i am just too happy these days, i need to feel absolutely miserable", this is the game for you. also has cool skins',
        curse_two:"I hate this game, the matchmaking is horrible and I always play against radiants, and the agents are more broken the others, its the same thing that put an kid to fight with mike tyson... 10/10",
        curse_three:"actually a horrible game,worst matchaking possible, trash rules, no updates only cares about money and is just a boring, bad game overall. There are no ways to improve unless you play the game like your life depends on it and it is impossible to play 'for fun'. If you wanna be good at the game, get ready to play everyday to get a higher rank that doesnt reward you at all. The game is always bland without lots of updates and the same boring, expressionless charecters everyday. The ranking system makes no sense either like: why is there a draw option? Why are the afk penalties so short when you ruin a whole rank and game with it? Why do you only get 400 credits and shields when you have an afk teamate? Finally,how are you supposed to rank up when you lose 20 rr for being top frag, but gaining 13 rr when you win?",
        curse_four:"So the learning curve for this game is so brutal and honestly the play mechanics are so unforgiving, this game is trash. Even the better players of this game are not having fun from what they say in voice chat. Alot of players in game are toxic, and unless you want to put in hundreds of hours into aim training and learning how to pre aim in the maps you will never truly get much enjoyment out of this game. The little tricks for each character do not really change the fact that this is a Counterstrike clone. You can just play CS GO instead of this piece of counterfeit trash. I have no idea why this thing is so popular. I guess because they ripped off the graphics style from Overwatch and Apex. If you actually want to have fun at this game the time investment is so huge, you're better off playing something else that is actually fun from the start.",
        curse_five:'''
        "Revive me, Jett". It is worth agreeing with the poor selection of players, where there are Radiants on Silver, but game is funny
        ''',
        curse_six:'''
        One of the worst competetive shooters ever created but alright game. Game features: - Anti-cheat that mostly works yet it's capable of abusing your PC when you don't even play Valorant by using every possible % of your CPU and RAM - Probably tons of smurfs, cringe duos, toxics, crybabies, boosting services, and a lot of actually stupidity. - Rank system doesn't seem to be adjusted properly due matchmaking sometimes giving a solo ascendant atleast 1 plat in team during ranked. Also sometimes there's actually no difference in Diamond and Gold players even in overall stats, but atleast golds aren't playing in something considered "high-elo" - "Quality" gun control, spraying mostly rng, shooting while moving mostly rng, first bullet accuracy mostly rng. If you don't hit first 5 bullets just hide or die, spraying and praying while crouching is not working if you hit something it's just luck but most likely hurts eyes of everybody watching. - Abilities are mostly good, but beware that most new characters are overpowered for most of time, while Riot decides to nerf a character with lowest pickrate because dunno don't care. If you actually enjoy this game congrats, if you play for fun it can be a good time but in reality if you try your best on ranked, you most likely gonna get smashed (atleast on Diamond 1 - Immortal 1) by teammates not capable of talking, random dudes headshoting you while in the air, an random french man cusing at you in his native language, a random game crash, a random server issues, a random update that nerfs characters that don't need it. Riot focuses to not reward skilled players so much it actually hurts, if you want to hit immortal you need teammates and time to just play. (doesn't work if you play by using steering wheel without monitor.) I played this game for a long time and never can stay for long, i come back hoping for anything good but always leave, the gameplay just ****. The nice thing is community, for the half of the time it's toxics, smurfs, cringe edaters,creeps, random woman that screams at you, random man that screams at you in some random language, random child that does all of above but with irritating voice. Atleast the other half can grant you the nicest time of your life starting from having fun on all of the modes to even starting enjoy ranked even when losing due to nice atmosphere and having fun. In the end this gameplay for an competetive game ****, all that matters is your teammates and way you approach being abused by the broken gameplay. (edit: i don't want to start a topic about how broken are rating points in this game it's just not worth it. If you know how broken it's in League of Legends, it's broken here too, just don't care or do. I don't give a ****.)
    ''',
    curse_seven:'''
Worst Competitive Game i Have Ever Played in my life. BadGame Mechanic and Full of lifeless Smurfs
    ''',
    curse_eight:'''
550 Hours still Silver Hardstuck
    ''',
    curse_nine:'''
This game is trash. The developers of this game are the worst people on this planet and the recruiters that work at riot ****. I’m deleting everything riot and never touching anything riot again in my life!!! You **** as a company ran by Chinese. all Chinese like to do is COPY other things. LOL is a copy of DOTA and valorant is a copy of counter strike. FU riot scammers. Trash company
    ''',
    curse_ten:'''
my boyfriend makes me uwu every time he gets a kill and then posts it on tiktok
    ''',
    curse_eleven:'''
    This game is ****. You need no Aim, only Luck. Run and gun, smurfs, ping **** included
    ''',
    curse_twelve:'''
hope the game owner get cancer and dies with his **** mum in a hospital bed while shes crying her own eyesout ty<3 
    '''
        }
    list_messages = list(messages.values())
    rand_num = random.randrange(len(list_messages))
    yag.send(to='mdfarhanofficial@protonmail.com',subject='Valorant players frustrations about this game is at its peak',contents = str(list_messages[rand_num]))
    print('Email: email is successfully delivered')
except:
    print('Email: email failed to deliver')
