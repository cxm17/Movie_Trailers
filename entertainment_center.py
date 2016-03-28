import fresh_tomatoes
import media

carlitos_way = media.Movie("Carlito's Way", "A man's attempt to break from his past.", "http://t0.gstatic.com/images?q=tbn:ANd9GcR2DB0yFe0hPZoA0n2gGZPK3RmK94LW97pZ5G91SmV_2Ygib_tz","https://www.youtube.com/watch?v=l4l_iKUi71I")

rocky_3 = media.Movie("Rocky 3", "A lucky bum gets beaten by a Chicago legend!","http://blog.signalnoise.com/wp-content/uploads/2013/03/i_rocky31.jpg","https://www.youtube.com/watch?v=2FJp8WkudXg")

scarface = media.Movie("Scarface", "A man's rise and fall in the Miami underworld", "http://fontmeme.com/images/Scarface-Poster.jpg", "https://www.youtube.com/watch?v=7pQQHnqBa2E")

equilibrium = media.Movie("Equilibrium", "Gunkata!!!", "http://ia.media-imdb.com/images/M/MV5BMTkzMzA1OTI3N15BMl5BanBnXkFtZTYwMzUyMDg5._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=raleKODYeg0")

the_last_boy_scout = media.Movie("The Last Boy Scout", "A hero saves a group of people whom he should be indifferent toward!", "https://upload.wikimedia.org/wikipedia/en/0/0d/Last_boy_scout.jpg", "https://www.youtube.com/watch?v=WAGPeBs0G1I")

flash_gordon = media.Movie("Flash Gordon", "A football hero saves Earth!", "http://vignette3.wikia.nocookie.net/starwars/images/7/78/FlashGordon.jpg/revision/latest?cb=20150622225707", "https://www.youtube.com/watch?v=8EY8QsBH5OU")

movies = [carlitos_way, rocky_3, scarface, equilibrium, the_last_boy_scout, flash_gordon]
fresh_tomatoes.open_movies_page(movies)
