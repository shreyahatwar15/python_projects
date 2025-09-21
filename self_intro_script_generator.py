"""

Python script that interacts with the user and generates a personalized self- introduction. 
Add the current date at the end of the paragraph and wrap the printed message with a decorative border of stars(*)

"""

import datetime

name = input("What's your name? ").strip()
age = input("How old are you? ").strip()
city = input("Where are you from? ").strip()
profession = input("What's your profession? ").strip()
hobby = input("What's your hobby? ").strip()

introduction = (
    f"Hi, Good Morning!!\n I am {name}. I am {age} years old. I live in {city}.\n I work as a {profession}. I absolutely enjoy {hobby} in my free time.\n"
)

current_date = datetime.date.today().isoformat()
introduction += f"\n Logged on: {current_date}"

border = "*" * 100

self_introduction = f"\n{border}\n{introduction}\n{border}"

print(self_introduction)



