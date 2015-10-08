# Django MovieLens 1M Database Website

<!-- ### A Website to see Top Movies, Movie Info, and User Info from the MovieLens 1M Database

* `localhost/top_20` shows the top 20 movies
* `localhost/movies` shows all of the movies
* `localhost/users` shows all of the users -->

### System Requirements

* You will need to have **python&nbsp;3** installed on your machine or have access to a Python&nbsp;3 interpreter. See [Python's site](https://www.python.org/) for details.

* Copy this repo to your computer; the below assumes you have kept the default folder name as `movieratings`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* You will need to download the [MovieLens 1M](http://files.grouplens.org/datasets/movielens/ml-1m.zip) dataset. Unzip the downloaded file and move the folder into `movieratings/movieratings` (the same directory as `manage.py`). It should be named `ml-1m`.

* **To load the data**, you will need to run some shell commands. Navigate to the `movieratings/movieratings` folder and confirm that you see the `manage.py` file. Then run the following lines:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell
>>> from lensview.models import *
>>> load_all_ml_data()
>>> exit()
```

* **Running the site** requires more command line. Navigate to `movieratings/movieratings` and enter `python manage.py runserver` This will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.

<!-- ### User Pages
* **Recommended.** This mode will show you recommendations specific to your tastes by analyzing what others who have similar preferences have rated highly. The movies that you have already seen are filtered out. There is a menu system that allows you to select the number of results and the minimum number of overlapping movie ratings with other users from which to make the recommendations.
* **Popular.** This mode will help you explore popular movies you haven't seen.

### Top 20 Popular Movies
This mode lets you explore movies based on user ratings. There is a menu system to allow you to specify the number of results and the minimum number of user ratings. -->
