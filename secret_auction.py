from replit import clear
#HINT: You can call clear() to clear the output in the console.
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_big = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_big:
      highest_big = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_big}")
while not bidding_finished:
  name = input("Enter your name: ")
  price = int(input("How much is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? 'y' or 'n'  \n").lower()
  if should_continue == 'n':
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == 'y':
    clear()