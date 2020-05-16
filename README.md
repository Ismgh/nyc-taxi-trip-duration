# NYC_Kaggle_Challenge
Making predictions of New York City Taxis' trip duration using Machine Learning (Challenge Provided by Kaggle). <br/>

# Usage : 
1- Download Train and Test sets from : https://www.kaggle.com/c/nyc-taxi-trip-duration/data <br/>
2- Include these files in your environement (Google Colab, Anaconda, Jupyter ...) <br/>
3- Install Required packages (Pandas, Scikit Learn, Geopandas, Numpy) <br/>
4- Download NYC Maps from https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm <br/>
5- Export Maps as shp (shape files, you must include are related files in single directory) <br/>
6- Launch and run IPYNB Notebooks.<br/>
7- Main file is used only for Linear Regression Notebook and the Extended Notebook.

# Advice for intensive usage :
While searching for the ideal combinations of hyperparameters in the RandomForestRegressor algorithm (or any other algorithm), you may use Scikit-Learn's CrossValidation algorithm, it may took longer time to execute in a normal machine, consequently, 
https://colab.research.google.com/ (Google colab) may be the best environement to execute your code without harming your machine's memory.

# The Best obtained Scores based on public score : 
*SVR* : **0.534529**, Better than **33.5 %** of competitors  <br/>
*Linear Regression* : **0.52138**, Better than **35 %** of competitors <br/>
*Random Forest Regressor* : **0.40647**, Better than **59 %** of competitors. 
