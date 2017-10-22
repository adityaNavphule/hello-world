phrase = "dont't panic"
plist = list(phrase)
print(plist)
found =[]
#to be printed  - vowels in the phrase. 
vowels = ['a','e','i','o','u']
for letter in phrase:
	if letter in vowels:
		found.append(letter)
print(*found)
	    
    	

