current_movies = {}
current_movies['The Grinch'] = '11:00am'
current_movies['Rudolph'] = '1:00pm'
current_movies['Frosty the Snowman'] = '3:00pm'
current_movies['Christmas Vacation'] = '5:00pm'

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested showtime isnt playing")
else:
    print(movie, "is playing at", showtime)
