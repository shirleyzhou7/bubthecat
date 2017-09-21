import string
import csv
import time
import operator
from Readv3 import getUser, getMessage, getChannelname, getBannedUser, getBannedChannelname
from Readv3 import getslowmode, getr9k, getsubmode, getroomstatechannelname
from Readv3 import getOwner, getTurbo, getSub, getMod
from Socketv2 import openSocket, sendMessage
from Settingsv2 import HOST, PORT, PASS, IDENT
from datetime import datetime
from BubTheCat import processCommands

# Actually joins the rooms
s = openSocket()

### joinRoom(s)
readbuffer = ""


id = 0

# Sets how long the scraper will run for (in seconds)
starttime = time.time() + 7200

# Runs until time is up
while time.time() < starttime:
	
		# Pulls a chunk off the buffer, puts it in "temp"
		readbuffer = readbuffer + s.recv(1024).decode('utf-8')
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
	
		# Iterates through the chunk
		for line in temp:
			print(line)
			id = id + 1
		
			# Parses lines and writes them to the file
			if "PRIVMSG" in line:
				try:

					# Gets user, message, and channel from a line
					user = getUser(line)
					message = getMessage(line)
					channelname = getChannelname(line)
					owner = getOwner(line)
					mod = getMod(line)
					sub = getSub(line)
					turbo = getTurbo(line)
					
					# should parse message for commands
					processCommands(line, s)
					
					if owner == 1:
						mod = 1
		
					# Writes Message ID, channel, user, date/time, and cleaned message to file
					with open('outputlog.csv', 'a') as fp:
						ab = csv.writer(fp, delimiter=',')
						data = [id, channelname, user, datetime.now(), message.strip(), owner, mod, sub, turbo];
						ab.writerow(data)
								
				# Survives if there's a message problem
				except Exception as e:
					print("MESSAGE PROBLEM")
					print(line)
					print(e)
		
			# Responds to PINGs from twitch so it doesn't get disconnected
			elif "PING" in line:
				try:
					separate = line.split(":", 2)
					s.send(("PONG %s\r\n" % separate[1]).encode('utf-8'))
					print(("PONG %s\r\n" % separate[1]))
					print("I PONGED BACK")
				
				# Survives if there's a ping problem
				except:
					print("PING problem PING problem PING problem")
					print(line)
		
			# Parses ban messages and writes them to the file
			elif "CLEARCHAT" in line:
				try:
			
					# Gets banned user's name and channel name from a line
					user = getBannedUser(line)
					channelname = getBannedChannelname(line)
				
					# Writes Message ID, channel, user, date/time, and an indicator that it was a ban message.
					#	I use "oghma.ban" because the bot's name is oghma, and I figure it's not a phrase that's
					#	likely to show up in a message so it's easy to search for.
					with open('outputlog.csv', 'a') as fp:
						ab = csv.writer(fp, delimiter=',');
						data = [id, channelname, user, datetime.now(), "oghma.ban"];
						ab.writerow(data);
			
				# Survives if there's a ban message problem
				except Exception as e:
					print("BAN PROBLEM")
					print(line)
					print(e)
				

