# Make Pandas much faster by vectorization

Based on [Make Your Pandas Code Lightning Fast](https://youtu.be/SAFmrTnEHLg).

**Problem:**

Apply a logical condition across every row of a DataFrame.
Assign the result to a new column.

**Solutions:**

*Level 1 **Looping:***

- Define a function with the logic for rewarding for each row (i.e., person).
- Loop over each row of the DataFrame to apply the condition to obtain the value and assign it to a cell.

*Level 2: **Vectorization:***
- Apply the logical conditions to the whole DataFrame.
- Assign the default values to the column.
- Assign the Series of calculated values with condition.

The implementation is in `vectorize_conditions.ipynb` and `vectorize_conditions.py`. The notebook can be run on `MyBinder.org`.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cmg-git/pandas_triks/HEAD)
