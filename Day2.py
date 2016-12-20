mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

totalCost = int((1 + (tipPercent/float(100)) + (taxPercent/float(100))) * mealCost)

print "The total meal cost is %d dollars." %(totalCost)