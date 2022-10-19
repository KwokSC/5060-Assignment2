#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


def get_genre_correlation_matrix(spotify):
    y_dict = {}
    index = 0
    genre_matrix = np.zeros([14,14])
    spotify_genre = spotify['genre']
    genre_list = []
    
    for genre in spotify_genre:
        if genre.find(', ')>0:
            genres = genre.split(', ')
            for i in range(len(genres)):
                if y_dict.get(genres[i]) is None:
                    genre_list.append(genres[i])
                    y_dict[genres[i]] = index
                    index += 1
            for i in range(len(genres)):
                for j in range(len(genres)):
                    a = y_dict.get(genres[i])
                    b = y_dict.get(genres[j])
                    genre_matrix[a][b] += 1
        else:
            if y_dict.get(genre) is None:
                genre_list.append(genre)
                y_dict[genre] = index
                index += 1
            c = y_dict.get(genre)
            genre_matrix[c][c] += 1
    
    genre_list = np.array(genre_list).reshape(-1,1)
    genre_matrix = np.column_stack((genre_list, genre_matrix))
    return pd.DataFrame(genre_matrix, columns = y_dict.keys())

