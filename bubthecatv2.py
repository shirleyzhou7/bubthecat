
from Readv3 import getUser, getMessage, getChannelname, getBannedUser, getBannedChannelname
#import time
import random


#start game
initgame = "You're playing Cat Lady Craze! You love cats. Let's see how successfully you can raise one. ***type $getcat NAMEOFYOURCATHERE to raise your first cat!*** type $help to get a list of commands you can type!"
playList = [" rolls around on your carpet and sheds fur everywhere", " feels really exhilirated after playing with you", " twitches its tail"]
petList =["purrs in happiness", "rubs against your leg", "rolls around on the carpet"]
def send_msg(msg):
    return sock.send(("PRIVMSG #" + channel + " :" + msg + "\r\n").encode('utf-8'))
  

#helpsection
helpMessage = " help: $help | get new cat: $getcat NAMEOFCATHERE | feed cat: $feed | pet cat: $pet | work: $work | play with cat: $play | ignore cat: $ignore"  
#initvar()
def processCommands(line, sock):
    global name, money, hunger, happiness
    
    user = getUser(line)
    message = getMessage(line)
    channel = getChannelname(line)
    
    cat = False
    
    if "playCLC" in message:
        money = 100
        sock.send(("PRIVMSG #" + channel + " :" + initgame + "\r\n").encode('utf-8'))
    if money ==30:
        moneymsg = "You only have $30 yet. might want to think about getting a job... or going to work"
        sock.send(("PRIVMSG #" + channel + " :" + moneymsg + "\r\n").encode('utf-8')) 
    if not cat:
        if "$getcat" in message:
            hunger = 8
            happiness = 5
            name = message.replace("$getcat", "")
            cat = True
            getcat = "Congrats! You're raising a(nother) cat!"+name+ " is so excited to move in with you!"
            sock.send(("PRIVMSG #" + channel + " :" + getcat + "\r\n").encode('utf-8'))

    if "$help" in message:
        sock.send(("PRIVMSG #" + channel + " :" + helpMessage + "\r\n").encode('utf-8'))  

    #always check for how much time has passed to mark certain game points
    
    if "$work" in message:
        money+=5
        workmsg= "good for you, you decided to get off your butt and go earn some money at work. you now have "+ str(money)+" dollars."
        sock.send(("PRIVMSG #" + channel + " :" + workmsg + "\r\n").encode('utf-8'))
    
    #these commands only work while cat exists as an instance
    
    if "$feed" in message: 
        print("feeding")
        hunger+=1
        print(hunger)
        money -= 5
        feedMsg = "You feed"+name+", his hunger is now " + str( hunger) +" out of 10"
        if hunger==10:
            feedMsg += "Your cat is really really full. Please don't feed it anymore or he'll die from overbloating"
        sock.send(("PRIVMSG #" + channel + " :" + feedMsg + "\r\n").encode('utf-8'))
    if "$play" in message: 
        print("playing")
        hunger-=1
        print(hunger)
        playMsg = "You're playing with "+name+"." + name+ random.choice(playList)+"."
        sock.send(("PRIVMSG #" + channel + " :" + playMsg + "\r\n").encode('utf-8'))

    if "$pet" in message:
        print("petting")
        happiness+=1
        petMsg = "You pet "+ name +". "+name+ random.choice(petList)+"."
        sock.send(("PRIVMSG #" + channel + " :" + petMsg + "\r\n").encode('utf-8'))

    if "$ignore" in message:
        happiness -= 1
        sock.send(("PRIVMSG #" + channel + " :" + "You ignore " + name+ petMsg + "\r\n").encode('utf-8'))
    if 0 < hunger <=2:
        sock.send(("PRIVMSG #" + channel + " :" + name + 
            " is starving. :( Please feed it or death from starvation will follow" + "\r\n").encode('utf-8'))
    if hunger ==0:
        sock.send(("PRIVMSG #" + channel + " :" + name + 
        " has starved to death. You're an awful person. Please type 'playCLC' to play again." + "\r\n").encode('utf-8')) 
        cat = False
        name = ""
        happiness = 5
        hunger = 8
        return ""
    if happiness == 0:
        sock.send(("PRIVMSG #" + channel + " :" + name + " was so very sad...." + 
        name + " has died from depression. Please type 'playCLC' to play again." + "\r\n").encode('utf-8')) 
        cat = False
        name = ""
        happiness = 5
        hunger = 8
        return ""
        
    
                
            
        


        
        






