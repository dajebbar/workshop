capitals = [("USA", "Washington"), ("India", "Delhi"), ("France",
"Paris"), ("UK", "London")]

sorted_capitals = sorted(capitals, key=lambda x: x[-1], reverse=False)
print(sorted_capitals)