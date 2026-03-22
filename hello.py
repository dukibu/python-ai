print("Hello, World!")
#print("I'm learning Python for AI")
#print("My name is dukibu")
#print("Today is a great day to code!") 
import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

print("Hello, GitHub!")
print("Hello, GitHub from VSCode!")