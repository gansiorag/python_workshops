# Mito
Mito is a free Python package that allows the users to call a spreadsheet interface into their Jupyter environment. Every edit you make in the spreadsheet will generate the equivalent Python in the code cell below.
Mito is great for Python users who want to generate their syntax more quickly, without needing to go to Stack Overflow or google. It is also used by Excel users, who want to transition their skills to Python.
To install Mito, run these commands:<br><br>
python -m pip install mitoinstaller<br>
python -m mitoinstaller install<br><br>
Then open Jupyter Lab,<br><br>

 **python3 -m jupyter lab** <br><br>

 and this code should appear:<br><br>

**import mitosheet**<br>
**mitosheet.sheet()**<br><br>

Mito has lot’s of great functionality for exploratory data analysis, data cleaning, and data analysis, including:

    Generating graphs and the equivalent code
    Creating pivot tables
    Merging datasets together
    Using spreadsheet formulas
    Filtering and sorting datasets
    Looking at summary statistics
    Filling null values
    and much more!
full documentation - https://docs.trymito.io/getting-started/installing-mito