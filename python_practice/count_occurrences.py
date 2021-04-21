sentence = input("Sentence: ")
query = input("Word to look for in the senctence: ")
# Sanitize out inputs
sentence = sentence.lower().strip()
query = query.lower().strip()
num_occurences = sentence.count(query)
print(f"There are  {num_occurences} occurences of '{query}' in this sentence.")
