# A simple book search engine that allows users to search for books by keywords.

# Welcoming message
print()
print("Welcome to our Books Search Engine")
print("==================================")

# Create a sample database of book titles. 
# Later, this can be replaced by data from a file or an actual database.
db = [
    "Python for Beginners",
    "Advanced JAVA",
    "C++ For Windows",
    "Python book for Data Science",
    "C / C++ Fundamentals"
]

# Define a list of words to omit during the search (common words that don't add value to the search).
words_to_omit = ["or", "and", "the", "a", "an", "for", "in", "on"]

# Take the search query input from the user.
query = input("Enter your search keywords >> ")

# Split the user's query into a list of individual keywords.
query_list = query.split(' ')

# Initialize an empty list to store matching search results.
query_result = []

# Loop through each keyword from the user query.
for keyword in query_list:
    # Ignore words from the omission list.
    if keyword.lower() in words_to_omit:
        continue  # Skip to the next keyword.
    else:
        # Loop through each book title in the database.
        for db_item in db:
            # Split the current book title into individual words for detailed matching.
            db_item_words = db_item.split(' ')
            
            # Loop through the words in the current book title.
            for word_in_db_item in db_item_words:
                # Check if the current keyword matches part of the current word in the book title.
                # Also ensure the book isn't already added to the results.
                if keyword.lower() in word_in_db_item.lower() and db_item not in query_result:
                    query_result.append(db_item)  # Add the matching book title to the result list.
                    query_result.sort()  # Sort the results alphabetically.

# Display the results to the user.
if query_result:
    print()
    print(f"Displaying {len(query_result)} items:")
    print("==========================")
    # Display each matching book title.
    for index, result in enumerate(query_result, start=1):
        print(f"{index}. {result}")
else:
    # Inform the user if no matches were found.
    print("No results found.")
