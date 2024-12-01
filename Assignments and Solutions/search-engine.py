# Variable for search query
# a list that represents our database
# we will try to find matching keywords and then display the results containing those keywords

print()
print("Welcome to our Books Search Engine")
print("==================================")

# let's create a sample data base. (Later on, can be based on file or a proper database)
db = ["Python for Beginners", "Advanced JAVA", "C++ For Windows", "Pyhton book for Data Science", "C / C++ Fundamentals"]

# now creating a list of words that are not directly keywords
words_to_omit = ["or", "and", "the", "a", "an", "for", "in", "on"]

# take input from the user
query = input("Enter your search keywords >> ")

# convert the user input (query) into a list of keywords. So that we can look for each relevant keyword. 
query_list = query.split(' ')

# initialize an empty result list.
query_result = []

for keyword in query_list: # now let's search each keyword
    if keyword.lower() in words_to_omit: # checking if the keyword is in omission list, just pass to the next word 
        continue
    else: # this is where the algorithm begins
        for db_item in db: # now looping through the database's entries
            db_item_words = db_item.split(' ') # from each entry, we create a list of words contained in that entry
            for words_in_current_db_item in db_item_words: # now looping through all the words one by one from the current entry's words list.
                # the actual search begins 
                # we are matching current keyword with the current word being looped in the list of words of the current entry. 
                # for example, if my current keyword matches with the current word from the list of words of the current entry of the database
                if keyword.lower() in words_in_current_db_item.lower() and db_item not in query_result: # well before adding the book in the result, also making sure its not already there. 
                    query_result.append(db_item) 
                    query_result.sort() # finally sorting.

result_count = 0
if len(query_result) != 0:
    print()
    print(f"Displaying {len(query_result)} items: ")
    print("==========================")
    for result in query_result:
        print(f"{result_count + 1}. {result}")
        result_count += 1
else:
    print("No result found")

# later on more features will be added. 




