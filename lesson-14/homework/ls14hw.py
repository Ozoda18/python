json_='{"name1":"John","surname1":"Doe","major":"english","name2":"Alice","surname2":"Smith","major":"math",}'
dict_obj=json.loads(json_)
from requests.exceptions import HTTPError
import requests
import json
import random
def load_json_file(path):
    with open(path) as f:
        dict_obj2=json.load(f)
    print(dict_obj2)
load_json_file('students.jon');

api_key = "YOUR_API_KEY"
city = "Tashkent,UZ"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
response = requests.get(complete_url)
if response.status_code == 200:
    data = response.json()
    main = data["main"]
    weather = data["weather"][0]
    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    description = weather["description"]
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")
else:
    print("City not found or API request failed.");



def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def create_book(title, author, year):
    books = load_books()
    new_id = max([book['id'] for book in books], default=0) + 1
    new_book = {"id": new_id, "title": title, "author": author, "year": year}
    books.append(new_book)
    save_books(books)
    print(f"Book '{title}' added successfully.")

def read_books():
    books = load_books()
    if books:
        for book in books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print("No books available.")

def update_book(book_id, title=None, author=None, year=None):
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            if title:
                book['title'] = title
            if author:
                book['author'] = author
            if year:
                book['year'] = year
            save_books(books)
            print(f"Book ID {book_id} updated successfully.")
            return
    print(f"Book with ID {book_id} not found.")

def delete_book(book_id):
    books = load_books()
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            save_books(books)
            print(f"Book ID {book_id} deleted successfully.")
            return
    print(f"Book with ID {book_id} not found.");

def fetch_movies_by_genre(genre, api_key):
    url = f"http://www.omdbapi.com/?s={genre}&apikey={api_key}&type=movie"
    response = requests.get(url)
    data = response.json()
    if data['Response'] == 'True':
        return data['Search']
    else:
        print("Error fetching movies:", data.get('Error', 'Unknown error'))
        return []

def recommend_movie(genre, api_key):
    movies = fetch_movies_by_genre(genre, api_key)
    if movies:
        movie = random.choice(movies)
        print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
        print(f"IMDB ID: {movie['imdbID']}")
    else:
        print("No movies found for this genre.")

def main():
    api_key = "your_api_key_here"  
    print("Welcome to the Movie Recommendation System!")
    print("Available Genres: Action, Comedy, Drama, Horror, Romance, Sci-Fi, Thriller")
    genre = input("Enter a genre: ").capitalize()
    recommend_movie(genre, api_key)

if __name__ == "__main__":
    main()






    
