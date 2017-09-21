
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

sassythings = [""]

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
