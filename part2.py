# Smart School Day Planner

print("=== Smart School Day Planner ===")

print("Answer 3 quick questions and I will plan your day!\n")

day = input("What day is it? (Monday to Sunday): ").strip().capitalize()

weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()

homework = input("Is your homework done? (yes / no): ").strip().lower()
if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type    : First day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day type    : Last school day. Return library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Stay focused!")
else:
    print("Day type    : Day not recognised. Please check the spelling.")
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done!") 
if weather == "rainy" and weather == "cloudly":
 print("weather tip : pack your umberalla - it may get wet outside.")
