"""
A python script that takes a message and adds emojis after specific keywords to make it more expressive.
- make it case-insensitive(match "happy" or "Happy")
- handle punctuation(like commas or periods right after keywords)

"""
# get a dictionary
emoji_map = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😠",
    "surprised": "😲",
    "funny": "😂",
    "tired": "😴",
    "confused": "😕",
    "excited": "🤩",
    "bored": "😐",
    "coder": "💻",
    "python": "🐍",
    "coffee": "☕",
    "music": "🎵",
    "tea": "🍵"
}
    

# get user message
message = input("Enter your message: ")

updated_words = []

# process each word
for word in message.split():
    cleaned_word = word.strip(",.!?;:").lower()
    emoji = emoji_map.get(cleaned_word, "")
    if emoji:
        updated_words.append(f"{word}{emoji}")
    else:
        updated_words.append(f"{word}")

updated_message = " ".join(updated_words)
print("Enhanced Message:", updated_message)