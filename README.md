# Human Study User Interface
This web app is developed for human study in Computer Vision research, especially for GAN related tasks.
We implemented:
1. __Just Noticeable Difference (JND)__: show user an image for one second and ask real/fake
2. __A/B Test__: Given reference images, ask user whether query 1 or query 2 has better quality.
---
## How to start
This web app is implemented by Django. ([A nice tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) for anyone who is interested to read.)
### Lanuch Website
```
python manage.py runserver 0.0.0.0:8000
```

### Populate Question Pool
#### Manually
One way to do so is to manually add question as the superuser. 
First log as the superuser. Create superuser by:
```
python manage.py createsuperuser
```
Then go to [0.0.0.0:8000/admin]() to change question pools. You may also need to link answers to their associated questions.
#### Automatically
We are working writing a scrpt to do this. TBD.

### Collect the statistics
Your users's report will be saved in the linked database. All you need to do is read the count of answers of every question, and evaluate according. We are working on developing a script which can do this automatically.

---
We borrowed some .css styles from https://github.com/akashgiricse/lets-quiz
