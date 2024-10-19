# Numpy-Diagonal
## Diagonal Matrix Printer

**This Python program prints an `N x M matrix (2D array)` where the main diagonal elements are 1.0s, and all other elements are 0.0s. The matrix is printed with specific formatting to ensure proper alignment using NumPy.**

### Table of Contents

- Description
- Features
- Input Format
- Output Format
- Usage
- Sample Input/Output
- Installation
- License
- Description

**This program takes two space-separated integers, N and M, as input, where:**
    ``N represents the number of rows.``
    ``M represents the number of columns.``

***It then generates and prints an `N x M matrix` with 1.0 on the diagonal and 0.0 elsewhere. The matrix is formatted in compliance with NumPy's legacy print style (legacy='1.13') for proper alignment of the output.***

#### Features

Handles any valid matrix dimensions (N x M).
Ensures the matrix is printed in the correct format with aligned spacing.
Uses NumPy for efficient matrix operations and generation.


#### Input Format

**A single line containing two space-separated integers:**
    N: The number of rows in the matrix.
    M: The number of columns in the matrix.

#### Output Format

**The program prints an N x M matrix where:**
    1.0 represents the elements on the main diagonal.
    0.0 represents all other elements.


## Usage

- Run the program.
- Provide the matrix dimensions (N and M) as input.
- The program will print the resulting matrix in the specified format.


### Example Usage:
```
$ python diagonal_matrix.py
```
### Sample Input/Output

#### Sample Input 1:
`3 3`

#### Sample Output 1:
```
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
#### Sample Input 2:
`4 5`

#### Sample Output 2:
```

[[ 1.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.]
 [ 0.  0.  0.  1.  0.]]

```

### Installation

Install `NumPy` if you haven't already:
`pip install numpy`

Download or clone this repository.
Run the script:

`python diagonal_matrix.py`
