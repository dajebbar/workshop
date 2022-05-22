list_of_words = ["Hello", "there.", "How", "are", "you", "doing?"]
check_for = ["How", "are"]

# Multi-Element Membership Checking
c = all(w in list_of_words for w in check_for)
print(c)

v = any(w in list_of_words for w in check_for)

