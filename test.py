# Fun Loop Exercise: Smileys Pyramid

def print_smiley_pyramid(levels):
    for i in range(1, levels + 1):
        # Print spaces before smileys
        print(" " * (levels - i), end="")
        
        # Print smileys for each level
        for j in range(2 * i - 1):
            print("😊", end=" ")
        
        # Move to the next line for the next level
        print()

# Get user input for the number of levels
try:
    num_levels = int(input("Enter the number of levels for the smiley pyramid: "))
    
    # Ensure the input is positive
    if num_levels <= 0:
        print("Please enter a positive number.")
    else:
        # Call the function to print the smiley pyramid
        print_smiley_pyramid(num_levels)

except ValueError:
    print("Invalid input. Please enter a valid number.")
