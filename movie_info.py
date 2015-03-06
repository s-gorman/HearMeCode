#(Princess Bride, PG, 2, 8.2, Adventure/Comedy/Family)
#(Beauty and the Beast, G, 3, 8.1, Animation/Family/Fantasy)
#(The Little Mermaid, G, 3, 7.6, Animation/Family/Fantasy)
#(Ghostbusters, PG, 1, 7.8, Comedy/Fantasy/Sci-Fi)
#(The Breakfast Club, R, 3, 7.9, Comedy/Drama)

movie_titles = ['Princess Bride', 'Beauty and the Beast', 'The Little Mermaid', 'Ghostbusters', 'The Breakfast Club']
parental_rating = ['PG', 'G', 'G', 'PG', 'R']
bechdel_rating = [2, 3, 3, 1, 3]
imbd_rating = [8.2, 8.1, 7.6, 7.8, 7.9]
genre = ['Adventure/Comedy/Family', 'Animation/Family/Fantasy', 'Animation/Family/Fantasy', 'Comedy/Fantasy/Sci-Fi', 'Comedy/Drama']

movie_info = zip(movie_titles, parental_rating, bechdel_rating, imbd_rating, genre)
print movie_info
