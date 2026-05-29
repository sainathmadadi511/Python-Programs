

current_movies = { 'Bahubali' : '11:00am',
'KGF' : '12:00pm',
'Dragon' : '1:00pm'}

for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")
showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie is not playing")
else: 
    print(movie, 'is playing at', showtime)
