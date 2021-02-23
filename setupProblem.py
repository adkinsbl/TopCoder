import argparse
import requests
import re
import os
import subprocess
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Create a directory and python script for TopCoder problems.")
parser.add_argument('-link')
parser.add_argument('-dir', default = '.')
args = parser.parse_args()

if args.link.startswith('http'):
	URL = args.link
else:
	URL = 'https://community.topcoder.com/stat?c=problem_statement&pm=' + args.link

print("Fetching page from URL: {0}".format(URL))

try:
	page = requests.get(URL)
except:
	print("Failed to retrieve problem from URL: {0}".format(URL))
else:
	problemNumber = re.search("\d+$", URL).group()
	soup = BeautifulSoup(page.content, 'html.parser')
	className = soup.find("td", text="Class:").find_next_sibling("td").text
	methodName = soup.find("td", text="Method:").find_next_sibling("td").text
	
	if args.dir == '.':
		path = os.path.join(os.getcwd(), problemNumber)
	else:
		path = os.path.join(args.dir, problemNumber)
		
	if not os.path.exists(path):
		print("Creating directory: {0}".format(path))
		os.mkdir(path, 0o666)
		
	pyScript = os.path.join(path,className + '.py')
	
	if not os.path.exists(pyScript):
		f = open(pyScript, "w")
		f.write("# URL:\"{0}\"\n\n".format(URL))
		f.write("class {0}:\n".format(className))
		f.write("\tdef {0}(self, ):".format(methodName))
		
		npp = 'C:\\Program Files (x86)\\Notepad++\\notepad++.exe'
		if os.path.exists(npp):
			print("Launching script in editor: {0}".format(pyScript))
			subprocess.Popen([npp, pyScript])
	else:
		print("A solution already exists at {0}".format(pyScript))