import requests
from collections import Counter

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"

response = requests.get(url)
response.raise_for_status()

text_data = response.text

text_data = text_data[:1000]
print(text_data)

print()
print()

print("String Tokenization")
print()
lst = []
word = ""

for char in text_data:
    if char != ' ':
        word += char
    else:
        if word:
            lst.append(word)
            word = ""

if word:
    lst.append(word)

#with punctuation
print("Tokens with punctuation:")
print(lst)

print()
print()

#after removing punctuation
print("Tokens without punctuation:")
punctuations = [".","?","!",",",";",":","—","–","-","(",")","[","]","{","}","'",'"',"...","\n","\t"]
lst_without_punctuations = []
string = ""

for char in text_data:
    if char not in punctuations and char != ' ':
        string += char
    else:
        if string:
            lst_without_punctuations.append(string)
            string = ""

if string:
    lst_without_punctuations.append(string)

print(lst_without_punctuations)

print()
print()

#total number of tokens without punctuation
print("Total number of tokens without punctuation:", len(lst_without_punctuations))

print()
print()

#most frequent token
freq = Counter(lst_without_punctuations)
most_common_token, count = freq.most_common(1)[0]

print("Most Frequent Token:", most_common_token)
print("Frequency:", count)