import media
import webbrowser
import fresh_tomatoes
mad_max = media.Movie("Mad Max","fucking awesome","http://cdn1-www.superherohype.com/assets/uploads/gallery/mad-max-fury-road_1/mad-max-fury-road-poster2.jpg","https://www.youtube.com/watch?v=hEJnMQG9ev8")
#print mad_max.storyline

#mad_max.show_trailer()
movies =[mad_max]
fresh_tomatoes.open_movies_page(movies)
