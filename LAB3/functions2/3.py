def category_of_movies(x):
    for dictionary in movies:
        for key in dictionary:
            if dictionary["category"] == x:
                print(dictionary["name"])
                break