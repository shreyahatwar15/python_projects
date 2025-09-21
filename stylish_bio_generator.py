"""

A python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social mdeia profiles like Intagram or Twiter.
Save bio in txt format.

"""

import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession in one line: ").strip()
passion = input("Enter your passion: ").strip()
emoji = input("Enter your favourite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your Style: ")
print("1. Simple Lines")
print("2. Vertical Flair")
print("3. Emoji Sandwitch ")

style = input("Select 1, 2 or 3: ").strip()

def generate_bio(style):
    if style == "1":
        return f"\n{emoji} {name} | {profession} \n{passion}🤩 \n{website}📎"
    elif style == "2":
        return f"\n{emoji} {name} \n{profession} \n{passion}🤩 \n{website}📎"
    elif style == "3":
        return f"\n{emoji * 4} {name} - \n{profession} clear\n{passion}🤩 \n{website}📎"
    else:
        print("Select any of above")
        
bio = generate_bio(style) 

print("*" * 60)
print(f"\n Your stylish bio: \n")   
print(textwrap.dedent(bio))
print("*" * 60)

save = input("Do you want to save this file in text format? (y/n) ").lower()

if save == "y":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding ="utf-8") as f:
        f.write(bio)
    print("file saved")





