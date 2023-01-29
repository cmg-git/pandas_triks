#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:32:22 2023

@author: cghiaus

Problem:
Apply a logical condition across every row of a DataFrame.
Assign the result to a new column.

Solutions:

Level 1 Looping:
    Define a function with the logic for rewarding for each row (i.e., person).
    Loop over each row of the DataFrame to apply the condition and
    obtain the value of a cell.

Level 2 Vectorization:
    Apply the logical conditions to the whole DataFrame.
    Assign the default values to the column.
    Assign the Series of calculated values with condition.

Based on:
"Make Your Pandas Code Lightning Fast"
https://youtu.be/SAFmrTnEHLg

Example
=======
The problem:
Given a population for which each person has the characteristics:
    age, time_in_bed, percent_sleeping, favorite_food, hate_food

create a new column with their favorite food or hate food as a reward.

Reward logic:
    IF  (they were in bed for more than 1 hour
         AND if they slept for more than 10 %)
    OR
        if they are over 90 years old,
    THEN
        give them their favorite food.
    ELSE
        give them their hate food.
"""

import numpy as np
import pandas as pd


def generate_data(size=10_000):
    """
    Generates DataFrame with random data:
        index, age, time_in_bed, percent_sleeping, favorite_food, hate_food

    Parameters
    ----------
    size : int > 0
        n° of samples in the DataFrame.

    Returns
    -------
    None.

    """
    df = pd.DataFrame()
    df['age'] = np.random.randint(0, 100, size)
    df['time_in_bed'] = np.random.randint(0, 9, size)
    df['percent_sleeping'] = np.random.rand(size)
    df['favorite_food'] = np.random.choice(
        ['+pizza', '+tacos', '+ice-cream'], size)
    df['hate_food'] = np.random.choice(
        ['-brocolli', '-potato', '-eggs'], size)
    return(df)


def reward(person):
    """
    Implements the logical condition for each row.
    Returns the value tu be assigned to the column in df.

    Parameters
    ----------
    person : Series
        row for a person in the DataFrame.

    Returns
    -------
    person['favorite_food'] OR person['hate_food'] : value from row
    'favorite_food' or 'hate_food' of df
    """

    condition = ((person['time_in_bed'] > 1
                  ) and (person['percent_sleeping'] > 0.1)
                 ) or person['age'] >= 90

    if condition:
        return person['favorite_food']
    else:
        return person['hate_food']


size = 10   # n° of samples in the DataFrame
df = generate_data(size)

"""
LEVEL 1: Looping
****************

Loop over each row of the df and apply the condition given in the function.
For each row, assign the result to a cell of the df.
"""
df_loop = df

for index, person in df_loop.iterrows():
    df_loop.loc[index, 'reward'] = reward(person)


"""
LEVEL 2: Vectorization
*************

Instead of looping on each row,
apply the logical conditions to the whole DataFrame.
"""

df_vector = df

condition = ((df_vector['time_in_bed'] > 1
              ) & (df_vector['percent_sleeping'] > 0.1)
             ) | (df_vector['age'] >= 90)

df_vector['reward'] = df_vector['hate_food']
df_vector.loc[condition, 'reward'] = df_vector['favorite_food']


"""
Check if the two df are equal
"""
print("Are the two DataFrames equal? ", df_loop.equals(df_vector))
