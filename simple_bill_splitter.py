"""

A python script that helps split a bill evenly between friends.
- Round to 2 decimal places
- Print a decorative summary box

"""
# def get_float(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             return value
#         except ValueError:
#             print("Invalid input. Please enter a valid number. ")


people_num = int(input("How many people are in the group? "))
names = []

for i in range(1,people_num+1):
    name = input(f"Enter person name: #{i} ").strip()
    names.append(name)

total_bill = float(input("Enter the total bill amount in number only. "))
# total_bill = get_float("Enter the total bill amount in number only. ")

share = round(total_bill / people_num, 2)

print("\n" + "*" * 60)
print(f"Total bill amount: {total_bill}")
print(f"Each person shares: {share}")
for name in names:
    print(f"{name} owes: {share} rupees")
print("*" * 60 + "\n")







