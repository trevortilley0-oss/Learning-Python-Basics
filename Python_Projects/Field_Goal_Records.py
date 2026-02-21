def validate_field_goals():
    """
    Value returning function to validate field goals input between 1 and 150.
    Returns the validated field goals value.
    """
    while True:
        try:
            fg = int(input("Please enter the Field Goals made between 1 and 150:\n"))
            if 1 <= fg <= 150:
                return fg
            else:
                print("Invalid Field Goals Made. Please enter a value between 1 and 150:")
        except ValueError:
            print("Invalid Field Goals Made. Please enter a value between 1 and 150:")


def calculate_average(points_list):
    """
    Value returning function to calculate the average of field goals made.
    Returns the average as a float.
    """
    if len(points_list) == 0:
        return 0.0
    return sum(points_list) / len(points_list)


def main():
    # Introduction
    print("Let's analyze Points in Field Goals made records in Men's NCCA basketball tournaments over the NCAA Men's Basketball Tournament history.")
    print("-" * 70)
    
    # Get and validate number of players
    num_players = 0
    while num_players < 1 or num_players > 50:
        try:
            num_players = int(input("Please enter the number of players (between 1 and 50):\n"))
            if num_players < 1 or num_players > 50:
                print("Invalid number of players. Players entered must be between 1 and 50.")
        except ValueError:
            print("Invalid number of players. Players entered must be between 1 and 50.")
    
    # Initialize lists
    names = []
    teams = []
    years = []
    points = []
    
    # Collect data for each player
    for i in range(num_players):
        print(f"\n{'-' * 25}Player {i + 1} {'-' * 25}")
        
        # Get player name
        name = input("Please enter the Player's Name:\n")
        names.append(name)
        
        # Get team
        team = input(f"Please enter {name} team:\n")
        teams.append(team)
        
        # Get tournament year
        year = input("Please enter the tournament year:\n")
        years.append(year)
        
        # Get and validate field goals made
        fg_made = validate_field_goals()
        points.append(fg_made)
    
    # Display results
    print(f"\n{'-' * 18}Field Goals Made Records{'-' * 18}")
    print(f"{'Player Name':<20} {'Team':<15} {'Year':<6} {'FG Made':<10}")
    print()
    
    for i in range(num_players):
        print(f"{names[i]:<20} {teams[i]:<15} {years[i]:<6} {points[i]:<10}")
    
    # Calculate and display average
    average = calculate_average(points)
    print("-" * 60)
    print(f"NCAA Men's Top Field Goals Made Average {average:.1f}")


# Run the program
if __name__ == "__main__":
    main()