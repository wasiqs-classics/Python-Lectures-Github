# Variable for search query
# a list that represents our database
# we will try to find matching keywords and then display the results containing those keywords

print()
print("Welcome to our Books Search Engine")
print("============================")

db = ["Python for Beginners", "Advanced JAVA", "C++ For Windows", "Pyhton book for Data Science", "C / C++ Fundamentals"]
words_to_omit = ["or", "and", "the", "a", "an", "for", "in", "on"]

query = input("Enter your search keywords >> ")

query_list = query.split(' ')

query_result = []

for keyword in query_list:
    if keyword.lower() in words_to_omit:
        continue
    else:
        for db_item in db:
            db_item_words = db_item.split(' ')
            for words_in_current_db_item in db_item_words:
                if keyword.lower() in words_in_current_db_item.lower() and db_item not in query_result:
                    query_result.append(db_item)

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




