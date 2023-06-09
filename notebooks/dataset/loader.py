import os

def load_dataset():
    directory = os.path.dirname(__file__)
    emails = os.listdir(directory)
    email_bodies = {}
    for em in [em for em in emails if em.endswith(".txt")]:
        with open(directory + "/" + em, 'r') as email_body:
            email_bodies[em] = email_body.read()
    return email_bodies