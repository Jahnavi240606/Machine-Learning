import re

str1 = "I am a great learner. I am going to have an awesome life."
str2 = "I work hard and shall be rewarded well."
combined_str = str1 + " " + str2
word_list = [w for w in re.split(r'[ .]+', combined_str) if w]
word_count = len(word_list)
print("Original String:")
print(combined_str)
print("\nList of Words:")
print(word_list)
print(f"\nCount of Words: {word_count}")
