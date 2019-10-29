import sys, requests, argparse

parser=argparse.ArgumentParser(description='A simple web crawler made by Danilo Santos.')
parser.add_argument('url', help='URL to be crawled')
parser.add_argument('wordlist', help='paths that will be attempted to be reached')

args=parser.parse_args()

# Open the wordlist passed as a parameter
try:
	f=open(args.wordlist, 'r')
except FileNotFoundError:
	sys.exit('Error: file '+args.wordlist+' not found')

c=0

for line in f:
	line=line.rstrip()
	
	with requests.Session() as s:
		urlsourcecode=s.get(args.url+'/'+line)
		
		# Output only existing pages
		if(urlsourcecode.status_code!=404):
			print('[+] '+args.url+'/'+line+' (CODE:'+str(urlsourcecode.status_code)+')')
			
		c+=1
		
		if(c%100==0):
			print(c,'urls tested')

# Close input file
f.close()