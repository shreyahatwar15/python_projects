"""
A python script that allows you to maintain a daily learning journal. Each entry will be saved into a '.txt' file along with a timestamp.
- add a optional rating (1-5) for how productive the day was.
- show a confirmation message after saving the entry.
- make sure the format is clean and easy to read when opening the file.

"""
import datetime

entry = input("What did you learn today? ").strip()
rating = input("Rate your productivity today(1-5, optional) ").strip()

# %I:%M %p for 12-hour format with AM/PM, %H:%M:%S for 24-hour format
date_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")

journal_entry = f" 📅Date: {date_time}\n Entry: {entry}\n"

if rating in ["1", "2", "3", "4", "5"]:
    journal_entry += f"Productivity Rating: {rating}/5"  
journal_entry += "\n" + "-" * 40 + "\n"

with open("learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)

print("Your entry has been saved. Keep up the great work!")


#tabkey
# filename = "learning_journal.txt"
# with open(filename, "a") as file:
#     file.write(f"Date: {date_time}\n")
#     file.write(f"Entry: {entry}\n")
#     if rating in ['1', '2', '3', '4', '5']:
#         file.write(f"Productivity Rating: {rating}/5\n")
#     file.write("-" * 40 + "\n")
# print("Your entry has been saved. Keep up the great work!")

