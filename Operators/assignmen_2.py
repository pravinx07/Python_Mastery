# Imagine you’re making a Movie Ticket Booking System 🎬:

# Price per ticket = 150

# User buys 4 tickets

# If total cost > 500, give 10% discount

# Print final bill amount


ticket_price = int(150)
noOfTickets = int(input("Enter number of tickets you want: "))

totalCost = noOfTickets * ticket_price
discount = totalCost * 0.10

if totalCost > 500:
     print("Total cost including discount is: " , totalCost - discount)
else:
     print("Total cost of tickets is:" , totalCost)
