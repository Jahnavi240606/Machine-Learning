import re
sentence1 = "I am a great learner. I am going to have an awesome life."
sentence2 = "I work hard and shall be rewarded well."
sentence3 = sentence1 + " " + sentence2
word_list = re.split(r'[ .]+', sentence3)
word_list = [word for word in word_list if word]
exclude_words = {"I", "Am", "to", "and"}
filter_words = [word for word in word_list if word not in exclude_words and len(word) <= 6]
words_count = len(filter_words)
print("Original Word List:")
print(word_list)
print("\nFilter Word List:")
print(filter_words)
print(f"\nLength of Filtered Word List: {words_count}")
