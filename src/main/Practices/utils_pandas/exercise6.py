import os
import re
import pandas as pd
import numpy as np

# Helper function to print a visual delimiter
def number_of_spaces(number): return print('\n' * number)

def title_center_text(text, number): return print(f"{f'{text}':^{number}}")

def space_with_delimiter(number, delimiter): print(delimiter * number)

# Clean and format the movie data
def clear_string(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:

        outfile.write("ID::MOVIE TITLE::YEAR FILM::MOVIE GENRES\n")

        for line in infile:
            line = line.strip()
            if not line: continue

            parts = line.split('::')
            if len(parts) != 3: continue

            id_, name_year_movie, movie_genre = parts
            match_for_movie = re.search(r'\((\d{4})\)', name_year_movie)

            if not match_for_movie:
                movie_year = '1995'
                movie_name = name_year_movie
            else:
                movie_year = match_for_movie.group(1)
                movie_name = re.sub(r'\s*\(\d{4}\)', '', name_year_movie)

            output_line = f'{id_}::"{movie_name}"::{movie_year}::"{movie_genre}"'
            outfile.write(output_line + '\n')


# List all unique movie genres
def list_of_movie_genres(dataframe):
    dataframe['MOVIE GENRES'] = dataframe['MOVIE GENRES'].str.replace('"', '', regex=False)
    all_genres = dataframe['MOVIE GENRES'].str.split('|').explode().unique()
    genre_list = sorted(all_genres)

    space_with_delimiter(50, '=')
    title_center_text("Unique Genres in Movies", 50)
    space_with_delimiter(50, '=')
    for genre in genre_list: print(f"- {genre}")
    space_with_delimiter(50, '-')
    number_of_spaces(1)


# Count of movies per year
def movies_per_year(df):
    yearly_count = df.groupby('YEAR FILM').size()

    space_with_delimiter(50, '=')
    title_center_text("Number of Movies Per Year", 50)
    space_with_delimiter(50, '=')
    print(yearly_count)
    space_with_delimiter(50, '-')
    number_of_spaces(1)


# Percentage distribution of each genre
def genre_percentage(df):
    df['MOVIE GENRES'] = df['MOVIE GENRES'].str.replace('"', '', regex=False)
    exploded_genres = df['MOVIE GENRES'].str.split('|').explode()
    percentage = exploded_genres.value_counts(normalize=True) * 100

    space_with_delimiter(50, '=')
    title_center_text("Genre Percentage Distribution", 50)
    space_with_delimiter(50, '=')
    print(percentage.round(2).astype(str) + " %")
    space_with_delimiter(50, '-')
    number_of_spaces(1)


# Statistics using NumPy on number of genres per movie
def genre_stats_per_movie(df):
    df['GENRE COUNT'] = df['MOVIE GENRES'].str.split('|').apply(len)
    genre_counts = df['GENRE COUNT'].values

    total = np.sum(genre_counts)
    count = np.size(genre_counts)
    mean = np.mean(genre_counts)
    std_dev = np.std(genre_counts)

    space_with_delimiter(50, '=')
    title_center_text("Statistics: Number of Genres per Movie", 50)
    space_with_delimiter(50, '=')
    print(f"Total (Sum):           {total}")
    print(f"Count (Movies):        {count}")
    print(f"Mean Genres/Movie:     {mean:.2f}")
    print(f"Standard Deviation:    {std_dev:.2f}")
    space_with_delimiter(50, '-')
    number_of_spaces(1)


# Main function to execute all steps
def run_exercise_6():
    print("\nThe dataset folder contains 3 files: users, votes, and movies.")
    print("Write code to group and aggregate data to compute sum, count, ")
    print("mean and standard deviation using NumPy functions (np.sum).\n")

    base_path = os.path.dirname(__file__)
    input_file = os.path.abspath(os.path.join(base_path, "..", "..", "..", "..", "data", "movies_database.txt"))
    output_file = os.path.abspath(os.path.join(base_path, "..", "..", "..", "..", "data", "movies_database_modified.txt"))

    clear_string(input_file, output_file)
    df = pd.read_csv(output_file, sep=r"::", engine="python", encoding='utf-8')

    list_of_movie_genres(df)
    movies_per_year(df)
    genre_percentage(df)
    genre_stats_per_movie(df)