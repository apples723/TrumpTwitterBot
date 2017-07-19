#So my private twitter auth keys aren't on git.....
AllKeys = open('../keys.txt', 'r')
lines = []
for line in AllKeys:	
	lines.append(line)
AllKeys.close 

keys = dict(
	consumer_key = lines[0],
	consumer_secret = lines[1],
	access_token = lines[2],
	access_token_secret = lines[3],
)

