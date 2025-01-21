from extensions import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    choices = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime)
    
    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def __repr__(self):
        return f'<Question {self.id}>'
