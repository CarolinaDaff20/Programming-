import json

class MovieLibrary:   #se crea la classe per gestire la collezione di film tramite il file json
    class MovieNotFoundError(Exception):
        pass

    def __init__(self, json_file):                
        self.json_file=json_file        #esercizio 17
        try:
            with open(json_file, "r") as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Ups! Il file", {json_file}, "non e stato trovato.")
        
    def __update_json_file(self):               #salva le modifiche alla collezione di film dentro il file json
        with open(self.json_file, 'w') as file:
            json.dump(self.movies, file, indent=4)

        #esercizio 1
    def get_movies(self):                #restituisce l’intera collezione di film.
        return self.movies
    
        #esercizio 2
    def add_movie(self, title, director, year, genres):       #questa funzione affiunge un nuovo film alla collezione
        new_movie = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }
        self.movies.append(new_movie)
        self.__update_json_file()           # per aggiornare il file json 

        #esercizio 3
    def remove_movie(self, title):          #questa funzione rimuove un film dal titolo specificato
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return movie
            raise self.MovieNotFoundError("Ups! Il film", {title}, "non e stato trovato")          #se non trova il film solleva leccezione personalizata MovieNotFoundError
        
        #esercizio 4
    def update_movie(self, title, director=None, year=None, genres=None):            #questa funzione serve per aggiornare un film gia presente con le informaxione fornite
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                if director:
                    movie['director'] = director
                if year:
                    movie['year'] = year
                if genres:
                    movie['genres'] = genres
                self.__update_json_file()
                return movie
        raise self.MovieNotFoundError ("Ups! Il film", {title}, "non e stato trovato")      # se non trova il film solleva MovieNotFoundError
    
        #esercizio 5
    def get_movie_by_title(self, title):        #Questa funzione restituisce una lista con tutti i titoli dei film
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                return movie
        raise self.MovieNotFoundError ("Ups! Il film", {title}, "non e stato trovato")
    
        #esercizio 6
    def count_movies(self):             # questa serve per contare il numero totale di film nella collezione
        return len(self.movies)

        #esercizio 7
    def get_movie_by_title(self, title):        # restitusce un film in base al titolo, se non lo trova solleva MovieNotFoundError
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                return movie
        raise self.MovieNotFoundError ("Ups! Il film", {title}, "non e stato trovato")
    
        #esercizio 8
    def get_movies_by_title_substring(self, substring):             #restituisce il film che contengono una sottostringa nel titolo
        return [movie for movie in self.movies if substring.lower() in movie['title'].lower()]
    
        #esercizio 9
    def get_movie_by_year(self, year):              #restituisce tutti i film di un anno in specifico
        return [movie for movie in self.movies if movie ['year'] == year]
    
        #esercizio 10
    def count_movies_by_direcor(self, director):            #per contare il numeri di fil di un direttore in specifico
        return sum(1 for movie in self.movies if movie ['director'].lower() == director.lower())
    
        #esercizio 11
    def get_movies_by_genre(self, genre):           #restituisce i fil dello stesso genere
        return [movie for movie in self.movies if genre.lower() in [g.lower() for g in movie['genres']]]
    
        #esercizio 12
    def get_oldest_movie_title(self):           #restitusce il titolo del film piu vecchio
        return min(self.movies, key= lambda x: x['year'])['title']
    
        #esercizio 13
    def get_average_release_year(self):         #restituisce l'anno medio di uscita dei film
        return sum(movie['year'] for movie in self.movies) / len(self.movies)
    
        #esercizio 14
    def get_longest_title(self):            #restituisce il titolo piu lungo 
        return max(self.movies, key=lambda x: len(x['title']))['title']

        #esercizio 15
    def get_titles_between_years(self, start_year, end_year):           #restituisce i titoli dei film pubblicati tre due anni specifici
        return [movie['title'] for movie in self.movies if start_year <= movie ['year'] <= end_year]
    
        #esercizio 16
    def get_most_common_year(self):             #restituisce l'anno piu comune tra i film
        from collections import Counter
        year_count = Counter(movie['year'] for movie in self.movies)
        return year_count.most_common(1)[0][0]
    
        #esercizio 17 al inizio  
         
        #esercizio 18
    def remove_movies(self, title):             #serve per rimuovere un film dalla collezione in base al titolo scelto
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return movie
        raise self.MovieNotFoundError ("Ups! Il film", {title}, "non e stato trovato")
    
    def update_movie(self, title, director=None, year=None, genres=None):               #serve per modificare le informazioni di un film gia essistente nella collezione
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                if director:
                    movie['director'] = director
                if year:
                    movie['year'] = year
                if genres:
                    movie['genres'] = genres
                self.__update_json_file()
                return movie
        return self.MovieNotFoundError("Ups! Il film", {title}, "non e stato trovato")