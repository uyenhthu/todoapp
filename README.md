# todoapp
I wrote a simple To-Do List app from scratch, following the FlaskBlog demo--using Flask and some of its libraries like Flask-login for backend, SQL to store data, and some familiar frontend technologies (HTML + CSS + JS, no framework) introduced in Internet Seminar course by Jim Mahoney. 

Interactions:
  - Users can register and log in for an account. However, since I haven't set up cookies, the log-in information has not maintained with further actions yet.
  - Users can create a new list, whose data is inserted into List TABLE, by clicking on `New List` session in the nav bar.
  - When users click on the title of the created list, they can add new tasks with optional details to the list, whose data is also inserted into the Task TABLE.
  - Display the total number of lists by accessing the backend API.
  - Users can mark the task "done" by clicking the empty bullet points in front of the task.
        

Storage: Data is stored in a SQL file with 03 tables, of User, List, and Task, with two foreign keys.

Deploy: I followed [this source](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0) to deploy the app.

Primary references:
- [Flask App](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- [Flask Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)

Other sources:
- [To do List tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- [Heroku Deploy](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)

