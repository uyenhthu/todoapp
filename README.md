# todoapp
I did a pretty simple To-Do List app, primarily following the FlaskBlog demo--using Flask and some of its libraries like Flask-login for backend, SQL to store data, and some familiar frontend technologies (HTML + CSS + JS, no framework) introduced in Internet Seminar course by Jim Mahoney. 

Interactions:
  - User: can register and log in for an account. But my problem with the log-in session right now is that it cannot be kept along with further different actions with the user, because I haven't set up cookies yet. 
  - Supposedly, every user can create their own lists, which hasn't worked right now. But basically, user can create new list, whose data is inserted to List TABLE, by clicking at New List session in the nav bar.
  - When users click on the title of the created list, they can add new tasks with optional details to the list, whose data is also inserted into the database, but to the Task TABLE.
  - Display the total number of lists by accessing backend API, which follows your tutorial.     
  - I wanted to have the user be able to mark their tasks as completed, but it didn't really work. It is now only working for the first task listed. 
        

Storage: Data is stored in a SQL file with 03 tables, of User, List, and Task, with two foreign keys.

Deploy: I followed [this source](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0) to deploy the app which requires me to have a github account; However, I got stuck in creating a virtual environment and installing the dependencies something /pip install -r requirements.txt/


Primary references:
- [Flask App](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- [Flask Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
- Jim's work
- Stacy's assistance

Other sources:
- [To do List tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- [Heroku Deploy](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)

