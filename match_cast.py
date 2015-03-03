#!/usr/bin/env python
import argparse
import sys

from imdb import IMDb


args = None


def parse_args():
    global args

    parser = argparse.ArgumentParser()
    parser.add_argument('first_movie')
    parser.add_argument('second_movie')
    args = parser.parse_args()


def main():
    imdb = IMDb()
    # Get 2 movies
    first_movie = confirm_movie(imdb, args.first_movie)
    second_movie = confirm_movie(imdb, args.second_movie)
    imdb.update(first_movie)
    imdb.update(second_movie)

    print("Comparing '{}' and '{}'".format(first_movie["title"], second_movie["title"]))

    # Compare cast
    in_both = []
    for first_movie_person in first_movie["cast"]:
        for second_movie_person in second_movie["cast"]:
            if first_movie_person["name"] == second_movie_person["name"]:
                in_both.append(first_movie_person)


    for person in in_both:
        print(person["name"])


def confirm_movie(imdb, movie_name):
    return imdb.search_movie(movie_name)[0]



if __name__ == '__main__':
    parse_args()
    main()