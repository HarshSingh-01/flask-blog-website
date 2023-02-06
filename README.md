# Blog Website
The project website’s front end is written on HTML, CSS and Bootstrap. Backend is written on Flask. Database used in this project is SQLite. The user can create his blogs, can edit them as well as able to delete them. There a public blog checkbox is also added in this, If the checkbox is checked that means the blog will get published publicly otherwise the blog will be private. The newly created blogs will get display first.

For user authentication the flask_login module used. While creating password by the user, the password gets hashed in the backend. This ensures the protection of the password.

## How to use <br/>
### 1. Clone repostitory <br/>
```sh
git clone https://github.com/HarshSingh-01/flask-blog-website.git
cd flask-blog-website
```

### 2. Create a virtual enviroment <br/>

##### Windows 
```sh
py -3 -m venv venv
```

##### MacOS/Linux
```sh
python -m venv venv
```

### 3. Activate virtual enviroment <br/>
```sh
. venv/bin/activate
```

### 4. Install dependencies <br/>
```sh
pip install -r requirements.txt
```

### 5. Run app <br/>
```sh
python app.py
```

The app will run on:
[http://localhost:3000/](http://localhost:3000/)

You can change the port number in <strong>app.py</strong> file.

Press: Ctrl + C to close the server.

### 6. Deactivate virtual environment <br/>
```sh
deactivate
```

## Conclusion
In this blog website . The user can create their profile for blog posting. Views other people blogs, can post their own blogs, edit and delete them also. Their passwords hashed before getting stored in database. Users profile is protected as much they want. Public and private blogging feature is also added in this website. Website is ready to deploy on the server and can run in local machine.

This is a complete project and open source for everyone.



