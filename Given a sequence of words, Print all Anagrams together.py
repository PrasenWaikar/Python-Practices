from collections import defaultdict # to create a dictionary
 
#taking the words as input list
words = [ "cat", "dog", "tac", "god", "act", "z" ]

# anagram dictionary
anagrams = defaultdict(list)

# this will check if the words are anagrams of eachother
for word in words:
  anagrams[''.join(sorted(word))].append(word)

# this loop will print all the anagrams together
for anagram in anagrams.values():
  print(' '.join(anagram))