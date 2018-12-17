# ukrenergo

Create virtualenv and active venv: 
```sh
mkdir energo
cd energo
python3 -m venv venv
source ./venv/bin/activate
```

Get project:
```sh
git clone https://github.com/py-py/energo.git
```

Use next code lines for initing project and adding fake data:
```sh
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py add_superuser
$ python manage.py fake_users
$ python manage.py fake_articles
$ python manage.py fake_comments
```

**Requirements:**
- using Boostrap4 styles;
- using JQuery for ajax request;
- using Boostrap js file for modal window;

**Using:**

1.Add script on pages where need to use COMMENT service;
```
<script src='http://localhost:8000/static/comment/comment.js'></script>
```
2.Add tag div with id="idCommentButton" on page where need to use COMMENT service;
```
<div id="idCommentButton"></div>
```