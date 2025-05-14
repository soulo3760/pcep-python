import requests

url ='https://api.github.com/users/soulo3760'
response =requests.get(url)
data = response.json()
#beautify the jsonoutput

#print(data)

#list comprehension
#dict comprehension

followers = data.get('followers')
print(followers)

# name = data.get('name')
# print(name)
if response.status_code == 200:
	data = response.json()
	profile = {
	'user': data.get('login'),
	'name': data.get('name'),
	'updated_at':data.get('updated_at')
	}
	for key,value in profile.items():
		print(f'{key}:{value}')






###docstring
'''profile = 
{

name
user#login
IDENTIFIER#id
Num_followers#followers
num_following#following
date_created#created_at
Last_update#updated_at
Num_repo#public_repos
num_gists#public_gists	
}
'''
