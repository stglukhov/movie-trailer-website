import media
import webbrowser
import fresh_tomatoes
# this section creates an instance of Movie class, parameters gives name,
# desc, trailer link and image link

mad_max = media.Movie(
	"Mad Max",
	"In a stark desert landscape where humanity is broken, \
	two rebels just might be able to restore order: \
	Max, a man of action and of few words,and Furiosa, \
	a woman of action who is looking to make it back to her childhood homeland.",
	"http://cdn1-www.superherohype.com/assets/uploads/gallery/mad-max-fury-road_1/mad-max-fury-road-poster2.jpg",
	"https://www.youtube.com/watch?v=hEJnMQG9ev8")

movies =[mad_max]

# this section creates web page with movies added above
fresh_tomatoes.open_movies_page(movies)
