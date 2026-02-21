def field_goals():
    while True:
        try:
            points = int(input("Please enter the field goals made (between 1 and 150): "))
            if 1 <= points <= 150:
                return points
            else: 
                print("Invalid input. Please enter a number between 1 and 150.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def average_points(fieldgoal_list):
    if len(fieldgoal_list) == 0:
        return 0
    return sum(fieldgoal_list) / len(fieldgoal_list)


def main():
    print("Let’s analyze Points in Field Goals made records in Men’s NCCA basketball tournaments over the NCAA Men’s Basketball Tournament history.")

    players = 0
    while players < 1 or players > 50:
        try:
            players = int(input("Please enter the number of players (between 1 and 50): "))
            if players < 1 or players > 50:
                print("Invalid input. Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    names=[]
    teams=[]
    years=[]
    fg=[]
    
    for i in range(players):
        print(f"\n{'-'*25}Player{i+1}{'-'*25}")

        name=input("Enter Player Name: ")
        names.append(name)

        team=input("Enter Team Name: ")
        teams.append(team)
    
        year=input("Enter Year of Tournament: ")
        years.append(year)

        fieldgoal=field_goals()
        fg.append(fieldgoal)

    print(f"\n{'-'*25}Field Goals Made Records{'-'*27}")
    print(f"{'Player Name':<20}{'Team Name':<20}{'Year':<20}{'Field Goals Made':<20}")
    print()

    for i in range(players):
        print(f"{names[i]:<20}{teams[i]:<20}{years[i]:<20}{fg[i]:<20}")

    print("-"*76)
    print(f"NCAA Men's Top Field Goals Made Average: {average_points(fg):.2f}")


if __name__ == "__main__":
    main()
