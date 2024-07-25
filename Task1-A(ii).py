import demoji

# Load the demoji library
demoji.download_codes()

# Input string with emojis
text_with_emojis =input("Enter the with emojis:") #For ExAMPLE :"I love Python! 🐍❤️"

# Removing emojis from the text
text_without_emojis = demoji.replace(text_with_emojis, '')

print("Text without emojis:")
print(text_without_emojis)

# Replacing emojis with text descriptions
text_with_text_emojis = demoji.replace_with_desc(text_with_emojis)

print("Emojis replaced with text:")
print(text_with_text_emojis)




