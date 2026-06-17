# Take a sentence from the user and count how many words are present.

sentence = input("Enter a sentence: ")

# Splitting the sentence by whitespace to find words
words = sentence.strip().split()
word_count = len(words)

print("Total number of words:", word_count)
