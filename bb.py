food=["pasta,pizza,rice,burger,kottu,"]
dryfoods=["soya","green gram","dhal","noodles",]

if "pasta" in food:
  food.remove("pasta",food)

print("after remove'pasta'", food)


food.append("french fries")
print("after append", food)

dryfoods.append("milk powder")
print("after append", dryfoods)

