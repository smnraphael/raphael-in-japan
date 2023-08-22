# RAPHAEL IN JAPAN
#### Video Demo:  https://youtu.be/lf4bS5IKqLo
#### Description: This is my final project for Harvard CS50x.

#### User experience:
This is a blog where I can post my pictures and an explanations for each of them about my life in Japan. I’m passioned about both programming and Japan so I wanted to mix these two things together for my final project

#### Technologies:
This is a full-stack website which means I took care of both the front-end and the back-end.

For the front-end, I used HTML/CSS, Bootstrap, and JavaScript. The HTML files use the template from Jinja. The layout.html is the main file containing all the links related to Bootstrap, Google Fonts, icons, etc. I also used Bootstrap for the containers and easiest responsiveness. The website is responsive until a certain breakpoint which looks good on computers and on tablets. JavaScript has been used to implement a Vanilla Tilt effect (parallax on the pictures).

For the backend, I used Python (Flask), and SQLite. Python is my favorite programming language so it was very pleasant to use my knowledge and apply it to create some back-end. SQLite is the approach taught in CS50x so I reused it and create my tables through the terminal.

This is a quick look of how the database looks like:
This table is for the users. It contains an ID, a username, a hashed password, a first name, and a last name.
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL);

This table is for the posts. It contains an ID, a user_id (linked to user ID), an image (encoded and decoded through base54), a title, a text, and a timestamp (maybe for future improvement of the UI, but used currently for ordering by most recent).
CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER NOT NULL, image BLOB, title TEXT NOT NULL, text TEXT NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users(id));

#### Functionalities:
- Sessions: There is a sessions functionality so anyone can register. The password is hashed in the database. It is not possible to create an account with an existing username. Then the users can login.
- Viewing: All users can see the posts ranked by the most recent from the database.
- Admin/Post: My account is Admin so I can add new posts via another link in the nav bar.
    - I can add picture (base64 encoding and decoding)
    - I can add title
    - I can add content
    - I can save this data to the database through the Post button.

#### Files:
- The file app.py is the file containing all the backend, it redirects to the correct page, save the data to the database and render it when needed.
- The templates folder contains all the HTML templates for each page of the site. The layout.html is the main file and the other file use Jinja syntax
- The static folder contains different folders:
    - The css folder contains the CSS file for the styles
    - The icon folder contains the tab icon for the browser and the icon to add a picture
    - The ing folder contains the image visible on the welcome page
    - The js folder contains a script to allow vanilla tilt effect for the pictures visible in homepage
- The env folder is the environment

Overview:
https://github.com/smnraphael/raphael-in-japan/assets/130636559/93b8870c-9577-4067-a6f0-59f3f9dbf2bd

Welcome:
<img width="1675" alt="1 - Welcome" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/df0435f7-1bc4-4cc2-b85d-ee19d4add4c5">

Register:
<img width="1675" alt="2 - Register" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/1a8ff641-848b-4552-b0fb-5f2caeaa97f8">

Registered:
<img width="1675" alt="3 - Registered" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/98ab4ba0-9a93-45fa-bc82-c2e12eec590d">

Login:
<img width="1675" alt="4 - Login" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/ab096323-2c6d-4095-8510-6ee065b9758c">

Post:
<img width="1675" alt="6 - Post" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/84c1c2ba-992e-4f63-b80d-39eda7b0f371">
<img width="1675" alt="7 - Post" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/a4665b58-3a2c-47b8-b15e-9edcd38ac1bd">

Home:
<img width="1675" alt="8 - Home" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/d148c4d5-a9db-4c99-af68-2156c7697acd">

Home (public user):
<img width="1675" alt="9 - Home public" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/dcc114a1-da6e-4892-996b-699581de659a">

Security:
<img width="1675" alt="10 - Security" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/64588b77-afd0-4b34-95fe-89d07daae7fb">

Parallax effect on images:
<img width="1675" alt="11 - Parallax" src="https://github.com/smnraphael/raphael-in-japan/assets/130636559/e7f7a069-0737-4467-b964-78e394d9d0ff">
