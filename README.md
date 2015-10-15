# Django MovieLens 1M Database Website

### A Website to see Top Movies, Movie Info, and User Info from the MovieLens 1M Database

* `localhost/` shows the top 20 movies
* `localhost/movies/movie_id` for each movie's page
* `localhost/raters` for each rater's page

### System Requirements

* You will need to have **Python&nbsp;3** installed on your machine or have access to a Python&nbsp;3 interpreter. See [Python's site](https://www.python.org/) for details.

* Copy this repo to your computer; the below assumes you have kept the default folder name as `movieratings`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* You will need to download the [MovieLens 1M](http://files.grouplens.org/datasets/movielens/ml-1m.zip) dataset. Unzip the downloaded file and move the folder into `movieratings/movieratings` (the same directory as `manage.py`). It should be named `ml-1m`.

* This app is set up to run on PostgreSQL. I have set it up to have a database named `movieratings` with a user of `movieratings` and a password of `password`. The database name, user, and password can all be configured to your preferences in the `movieratings/movieratings/movieratings/settings.py` file. If you do not have PostgreSQL on your machine, follow [these instructions](https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md).

* **To load the data**, you will need to run some shell commands. Navigate to the `movieratings/movieratings` folder and confirm that you see the `manage.py` file. Then run the following lines **in order** (the last two each take a very long time):
```
$ python manage.py ml_to_json
$ python manage.py migrate
$ python manage.py loaddata users movies ratings
$ python manage.py make_raters_users
$ python manage.py update_movies
```

* **Running the site** requires more command line. Navigate to `movieratings/movieratings` and enter `python manage.py runserver` This will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.

### Movie Pages
Located at `localhost/movies/movie_id`, where `localhost` is the location of your django server and `movie_id` is the actual movie id in the database.

### Rater Pages
Located at `localhost/raters/rater_id`, where `localhost` is the location of your django server and `rater_id` is the actual movie id in the database.

### Top 20 Page
Located at `localhost/`, where `localhost` is the location of your django server. Shows the top 20 movies by average rating, but you can choose to show the top 20 most rated movies.
