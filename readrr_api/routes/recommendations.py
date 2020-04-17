import os
import json
import random
import pickle

import requests
from flask import Flask, request, jsonify
from readrr_tools.gb_funcs import retrieve_details
from readrr_tools.gb_search import GBWrapper
# may need cross origin resource sharing (CORS)

# instantiate api from wrapper
api = GBWrapper()

# load model dependencies
with open('knn_model.pkl', 'rb') as model:
    knn = pickle.load(model)

with open('compressed_matrix.pkl', 'rb') as matrix:
    compressed = pickle.load(matrix)

with open('book_titles.pkl', 'rb') as books:
    titles = pickle.load(books)


def get_recommendations(book_name, title_reference=titles,
                        matrix=compressed, model=knn, topn=5):
    """Returns a list of recommendations based on book title"""
    recommendations = []
    distances, indices = model.kneighbors(
        matrix[titles.index(book_name)].reshape(1, -1),
        n_neighbors=topn+1
    )
    for neighbor in indices[0]:
        title = title_reference[neighbor]
        recommendations.append(title)

    return recommendations


@recomendations.route('/recommendations/<int:userid>', methods=['GET'])
def recommend():
    """
    Provide recommendations based on user bookshelf.

    userid - integer user id
    """

    # This could probably just get sent straight to us by web
    shelf_endpoint = 'https://api.readrr.app/api/'\
                     'datasciencetogetasecretand'\
                     'pineapplepizzaandbrocolli/'

    user_data_url = (shelf_endpoint + userid)
    response = requests.get(user_data_url)
    user_books = response.json()

    # select a random favorite book from which to recommend books
    favorites = []

    for book in user_books:
        if book['favorite']:
            favorites.append(book['title'])

    # if there are no favorites, recommend based on first book
    if len(favorites) >= 1:
        target_book = random.choice(favorites)
    else:
        target_book = user_books[0]['title']

    # if book is not in known titles, recommend an alternative
    try:
        recommended_titles = get_recommendations(target_book)

    except ValueError:
        target_book = "#GIRLBOSS"
        recommend_titles = get_recommendations(target_book)

    neighbors = get_recommendations(target_book)
    output_recs = []

    for book in neighbors:
        book_data = api.search(book)
        target_data = book_data['item'][0]
        target_json = retrieve_details(target_data)
        output_recs.append(target_json)

    output = {'based_on': target_book,
              'recommendations': output_recs}

    return jsonify(output)
