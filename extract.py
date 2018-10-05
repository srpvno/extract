# import libraries
from lxml import html
import requests

payload = 	{
				"username": "#",
				"password": "#",
				"CSRFToken": "#"
					}

# create session object
session_requests = requests.session()

# extract token from login page
login_url = "#"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='CSRFToken']/@value")))[0]

#perform login phase
result = session_requests.post(
	login_url,
	data = payload,
	headers = dict(referer=login_url)		
)

# set url variable
url = '#'
result = session_requests.get(
		url,
		headers = dict(referer = url)
)

# grab from and for
tree = html.fromstring(result.content)
# this will create a list of names:
names = tree.xpath('//div[@class="JobInfo__name"]/text()')

# this will create a list of phone numbers:
phone = tree.xpath('//div[@class="ContactInfo__dataContainer"]/text()')

print(names)
print(phone)
    
