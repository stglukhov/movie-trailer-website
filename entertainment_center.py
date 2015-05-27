import media
import webbrowser
import fresh_tomatoes
#this section creates an instance of Movie class, parameters gives name, desc, trailer link and image link
mad_max = media.Movie("Mad Max","fucking awesome",
"http://cdn1-www.superherohype.com/assets/uploads/gallery/mad-max-fury-road_1/mad-max-fury-road-poster2.jpg",
"https://www.youtube.com/watch?v=hEJnMQG9ev8")

movies =[mad_max]

#this section creates web page with movies added above
fresh_tomatoes.open_movies_page(movies)
