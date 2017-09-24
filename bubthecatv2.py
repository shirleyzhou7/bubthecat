
from Readv3 import getUser, getMessage, getChannelname, getBannedUser, getBannedChannelname
import time
import random


#start game
initgame = "Playing CAT LADY CRAZE. You're an up and coming young professional who just moved out into a new apartment in the middle of bustling downtown Boston. Oh. And you love cats. You want to raise as many as possible. Let's see how far you get before your life falls into disarray. ***type $getcat NAMEOFYOURCATHERE to raise your first cat!*** type $help to get a list of commands you can type!"

#def initvar():
   

#helpsection
helpMessage = " help: $help | get new cat: $getcat NAMEOFCATHERE | feed cat: $feed | pet cat: $pet"  
#initvar()
def processCommands(line, sock):
    cat = False
    name = ""
    age =0
    health=10
    hunger = 8 #out of 10 which means full
    happiness=5 #where 5 is neutral under 5 is increasing unhappiness, over 5 is increasing happiness

    user = getUser(line)
    message = getMessage(line)
    channel = getChannelname(line)

    #always check for how much time has passed to mark certain game points
    if "playCLC" in message:
        sock.send(("PRIVMSG #" + channel + " :" + initgame + "\r\n").encode('utf-8'))
    if "$getcat" in message:
        name = message.replace("$getcat", "")
        cat = True
        startTime = time.time()
        getcat = "Congrats! You're raising a(nother) cat!"+name+ " is so excited to move in with you!"
        sock.send(("PRIVMSG #" + channel + " :" + getcat + "\r\n").encode('utf-8'))

    if "$help" in message:
        sock.send(("PRIVMSG #" + channel + " :" + helpMessage + "\r\n").encode('utf-8'))

    #these commands only work while cat exists as an instance
    while cat:
        
        #feeding cat
        if "$feed" in message: 
            print("feeding")
            hunger+=1
            feedMsg = "You feed"+name+", his hunger is now" + hunger +" out of 10"
            if hunger==10:
                feedMsg += "Your cat is really really full. Please don't feed it anymore or he'll die from overbloating"
            sock.send(("PRIVMSG #" + channel + " :" + feedMsg + "\r\n").encode('utf-8'))


        if (time.time() - startTime) % 4 ==0: 
            print("4 sec passed")
            #cat loses hunger pts every 5 seconds
            hunger -=1
            sock.send(("PRIVMSG #" + channel + " :" + name + "'s hunger is now at " + str(hunger) + "\r\n").encode('utf-8'))
        if 0 < hunger <=2:
            sock.send(("PRIVMSG #" + channel + " :" + name + 
                " is starving. :( Please feed it or death from starvation will follow" + "\r\n").encode('utf-8'))
        if hunger ==0:
            sock.send(("PRIVMSG #" + channel + " :" + name + 
            " has starved to death. You're an awful person" + "\r\n").encode('utf-8')) 
            cat = False
            break

        
                
            
        


        
        






