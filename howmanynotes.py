amount = int(input("Enter the amount for withdrawal"))

hundred_note = (amount//100)
fifty_note = (amount%100)//50
ten_note = ((amount%100)%50)//10

print("Hundred notes:",hundred_note)
print("Fifty notes:",fifty_note)
print("Ten notes:",ten_note)