from lxml import html
import requests
requests.packages.urllib3.disable_warnings()

competition = [328, 302, 509, 281, 515, 424, 327, 502]
leaderboard = []

def populate_leaderboard(competition):
	for team in competition:
		# SCRAPE PAGE
		url = 'https://www.avivacommunityfund.org/voting/project/view/17-'+str(team)
		
		page = requests.get(url, auth=('[username]','[password]'), verify=False)
		tree = html.fromstring(page.content)

		# GET INFO
		group = tree.xpath('//h2/text()')
		title = tree.xpath('//h1/text()')
		votes = tree.xpath('//span[@class="votes-count"]/text()')

		# CLEAN
		group = str(group[0]).strip()
		title = str(title[0]).strip()
		votes = str(votes[0]).strip()
		votes = votes.replace(",","")

		# ADD ITEM TO LEADERBOARD LIST
		item = [group, title, int(votes)]
		leaderboard.append(item)
	
	return leaderboard

#print("%d    PROJECT: %s   VOTES: %s" % group title votes)

def votes_update(leaderboard):
	# pull only votes from site, append to 
	return

def rank(l):
	l.sort(key=lambda x: x[2], reverse=True)
	return l

populate_leaderboard(competition)

#rank list
leaderboard = rank(leaderboard)

#write to file
file = open('rank.txt', 'w')
for item in leaderboard:
  file.write("%s\n" % item)

import pandas as pd
df = pd.DataFrame({'Project Name': [],
                   'Group':  [],
                    'Votes' : []})

# append items to DataFrame
i = 0
for item in leaderboard:
	df.loc[i] = item
	i += 1
	
print (df)
