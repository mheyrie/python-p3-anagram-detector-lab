# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        
        word_ 
        sorted = sorted(self.word.lower())

        anagrams = []

        #iterating over list of words in word 
        for word in word_list:
            
            current_word_sorted = sorted(word.lower())

            
            if current_word_sorted == word_sorted and self.word.lower() != word.lower():
                anagrams.append(word)

        return anagrams


target_word = "Mary"
word_list = ['enlists']

anagram = Anagram(target_word)
matches = anagram.match(word_list)

print(matches)



