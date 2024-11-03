# Script to show possible wins for each bet up to the specified number of rollovers
def calculate_payout(amount, odds):
    """
    Calculate the payout based on bet amount and odds.
    
    Args:
    - amount (float): The initial bet amount
    - odds (float): The decimal odds for the bet
    
    Returns:
    - payout (float): The potential return if the bet wins
    """
    return amount * odds

# Example usage
amount = float(input("Enter the initial bet amount: "))
odds = float(input("Enter the decimal odds: "))
num_rollovers = int(input("Enter the number of times you'd like to bet (rollover): "))

print("\n--- Possible Wins for Each Bet ---")
for i in range(1, num_rollovers + 1):
    payout = calculate_payout(amount, odds)
    print(f"Bet {i}: Potential Payout = ${payout:.2f}")
    # Use the winnings as the next bet amount for compounding
    amount = payout
