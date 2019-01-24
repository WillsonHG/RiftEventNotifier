from urllib.request import urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client


shardDict = {
	1704 : 'Deepwood',
	1707 : 'Faeblight',
	1702 : 'Greybriar',
	1721 : 'Hailol',
	1708 : 'Laethys',
	1701 : 'Seastone',
	1706 : 'Wolfsbane'
	}

searchTerm = "Unstable Ashora"
print("Searching for " + searchTerm)
shardNames = ['Deepwood', 'Faeblight', 'Greybriar', 'Hailol', 'Laethys', 'Seastone', 'Wolfsbane']
shardUrls = []

for shard in shardDict:
	shardUrls.append("http://web-api-us.riftgame.com:8080/chatservice/zoneevent/list?shardId={0}".format(str(shard)))

i = 0
for url in shardUrls:
	html = urlopen(url).read()
	soup = BeautifulSoup(html, features="html.parser")

	for script in soup(["script", "style"]):
		script.extract()   

	text = soup.get_text()
	#test
	#print(text)

	if searchTerm not in text:
		print("Not on " + shardNames[i] + ".")
	else:
		#Account Sid and Auth Token from twilio.com/console
		account_sid = 'put yours here'
		auth_token = 'put yours here'
		client = Client(account_sid, auth_token)

		message = client.messages \
					.create(
						body=searchTerm + " is happening on " + shardNames[i] + "!",
						from_='+1',
						to='+1'
					)

		print("On " + shardNames[i] + ".")
	i += 1
