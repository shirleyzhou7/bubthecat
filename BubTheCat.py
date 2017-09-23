
from Readv3 import getUser, getMessage, getChannelname, getBannedUser, getBannedChannelname
import random

nice_things = ["$ is a gamer lord", 
	"you can do it $!", 
	"$ is amazing!", 
	"$ is incredible", 
	"I've simply never seen anything like $. Wow."]

sassy_things = ["Is that all you got?", 
	"You are so weak.", 
	"Is this your first time playing this game?", 
	"Did your keyboard become unplugged?", 
	"I've seen better."]

#start game
initgame = "Playing CAT LADY CRAZE. You're an up and coming young professional who just moved out into a new apartment in the middle of bustling downtown Boston. Oh. And you love cats. You want to raise as many as possible. Let's see how far you get before your life falls into disarray. *******start by typing $getcat to raise your first cat!******"
getcat = "Congrats! You want to raise a(nother) cat! What's his/her name? (type in name)"
#cat class
class Cat(object):
	def constructor(self,name):
		self.age =0
		self.health=10
		self.happiness=5 #where 5 is neutral under 5 is increasing unhappiness, over 5 is increasing happiness

#all the cats that you own
catlist = []

	

def processCommands(line, sock):
	user = getUser(line)
	message = getMessage(line)
	channel = getChannelname(line)

	#encourage says something nice about the user that called the command 
	if "!encourageme" in message:
		encouragement = random.choice(nice_things).replace("$", user)
		print(encouragement)
		sock.send(("PRIVMSG #" + channel + " :" + encouragement + "\r\n").encode('utf-8'))
	elif "!sassme" in message:
		sass = random.choice(sassy_things)
		sock.send(("PRIVMSG #" + channel + " :" + sass + "\r\n").encode('utf-8'))
		print(sass)

	if "catlady" in message:
		sock.send(("PRIVMSG #" + channel + " :" + initgame + "\r\n").encode('utf-8'))
	elif "$getcat" in message:
		sock.send(("PRIVMSG #" + channel + " :" + getcat + "\r\n").encode('utf-8'))
		cat1 = Cat(self,message)
		print(cat1.name)


		
		






