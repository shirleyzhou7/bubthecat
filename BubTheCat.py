
from Readv3 import getUser, getMessage, getChannelname, getBannedUser, getBannedChannelname
import time
import random

#start game
initgame = "Playing CAT LADY CRAZE. You're an up and coming young professional who just moved out into a new apartment in the middle of bustling downtown Boston. Oh. And you love cats. You want to raise as many as possible. Let's see how far you get before your life falls into disarray. ***type $getcat NAMEOFYOURCATHERE to raise your first cat!*** type $help to get a list of commands you can type!"
def getcat(name): 
	return "Congrats! You want to raise a(nother) cat!"+name+ " is so excited to move in with you!"

#cat class
class Cat(object):
	def init(self,name):
		self.name = name
		self.age =0
		self.health=10
		self.hunger = 8 #out of 10 which means full
		self.happiness=5 #where 5 is neutral under 5 is increasing unhappiness, over 5 is increasing happiness
		self.startTime = time.time()
	#def hunger(): 

#all the cats that you own
catList = []

#helpsection
helpMessage = " help: $help | get new cat: $getcat NAMEOFCATHERE | feed cat: $feed | pet cat: $pet"

	

def processCommands(line, sock):
	user = getUser(line)
	message = getMessage(line)
	channel = getChannelname(line)
	cat1 = Cat()

	#always check for how much time has passed to mark certain game points

	if "playCLC" in message:
		sock.send(("PRIVMSG #" + channel + " :" + initgame + "\r\n").encode('utf-8'))
	if "$getcat" in message:
		name = message.replace("$getcat", "")
		
		cat1.init(name)
		catList.append(cat1)
		# cat1.startTime = time.time()
		sock.send(("PRIVMSG #" + channel + " :" + getcat(cat1.name) + "\r\n").encode('utf-8'))

	if "$help" in message:
		sock.send(("PRIVMSG #" + channel + " :" + helpMessage + "\r\n").encode('utf-8'))

	#these commands only work while cat1 exists as an instance
	while isinstance(cat1, Cat):
		#feeding cat
		if "$feed" in message: 
			cat1.hunger+=1
			feedMsg = "You feed"+cat1.name+", his hunger is now" + cat1.hunger +" out of 10"
			if cat1.hunger==10:
				feedMsg += "Your cat is really really full. Please don't feed it anymore or he'll die from overbloating"
			sock.send(("PRIVMSG #" + channel + " :" + feedMsg + "\r\n").encode('utf-8'))

	
		if (time.time() - cat1.startTime) % 2 ==0: 
			#cat loses hunger pts every 5 seconds
			cat1.hunger -=1
			sock.send(("PRIVMSG #" + channel + " :" + cat1.name + "'s hunger is now at " + str(cat1.hunger) + "\r\n").encode('utf-8'))
		if 0 < cat1.hunger <=2:
			sock.send(("PRIVMSG #" + channel + " :" + cat1.name + 
				" is starving. :( Please feed it or death from starvation will follow" + "\r\n").encode('utf-8'))
		if cat1.hunger ==0:
			sock.send(("PRIVMSG #" + channel + " :" + cat1.name + 
			" has starved to death. You're an awful person" + "\r\n").encode('utf-8'))	
			cat1=""
			break
				
			
		


		
		






