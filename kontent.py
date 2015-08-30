import string
import sys
filename='pr_kon.csv'
words ={}
strip=string.whitespace+string.punctuation+string.digits +"\"'"
#for filename in sys.argv[1:]:
for line in open (filename):
    for word in line.lower ().split ():
        word=word.strip ()
        if len (word)> 4:
            words[word]=words.get (word,0)+1
for word in sorted (words):
    
    print ("'{0}', {1} ". format(word, words[word]))

  
