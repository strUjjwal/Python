import random
list_of_dict =  \
    [
        {"Name": "Narendra Modi", "Follower Count": 90, "Description": "Prime Minister", "Country": "India"},
        {"Name": "Christiano Ronaldo", "Follower Count": 250, "Description": "FootBaller", "Country": "Portugal"},
        {"Name": "Lionel Messi", "Follower Count": 210, "Description": "FootBaller", "Country": "Spain"},
        {"Name": "NASA", "Follower Count": 50, "Description": "Space Agency", "Country": "USA"},
        {"Name": "ISRO", "Follower Count": 5, "Description": "Space Agency", "Country": "India"},
        {"Name": "Virat Kohli", "Follower Count": 190, "Description": "Cricketer", "Country": "India"},
        {"Name": "Barack Obama", "Follower Count": 100, "Description": "Politician", "Country": "USA"},
    ]
flag = True
score = 0
while flag is True:
    i1 = random.randint(0, 6)
    i2 = random.randint(0, 6)
    while i1 == i2:
        i2 = random.randint(0, 6)

    print("Who is more popular?")
    print(f'"1": Name:{list_of_dict[i1]["Name"]}, Description:{list_of_dict[i1]["Description"]}, Country:{list_of_dict[i1]["Country"]}\n')
    print(f'"2": Name:{list_of_dict[i2]["Name"]}, Description:{list_of_dict[i2]["Description"]}, Country:{list_of_dict[i2]["Country"]}\n')
    ans = int(input("Enter your answer:"))
    if list_of_dict[i1]["Follower Count"] > list_of_dict[i2]["Follower Count"]:
        if ans == 1:
            print("Correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            flag = False
    elif list_of_dict[i1]["Follower Count"] < list_of_dict[i2]["Follower Count"]:
        if ans == 2:
            print("Correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            flag = False
    print(f"Score = {score}")