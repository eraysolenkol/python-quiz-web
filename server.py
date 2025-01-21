from flask import Flask, render_template, request
from api.views import api_bp 
from extensions import db
import os

app = Flask(__name__)

db_path = os.path.join(os.path.abspath(os.getcwd()), 'databases', 'main.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Veritabanı bağlantısını başlat
db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api')

# Eğer veritabanında Question tablosu yoksa oluştur
with app.app_context():
    from models import Question
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['GET'])
def quiz():
    return render_template('quiz.html', questions=Question.query.all())

@app.route('/submit', methods=['POST'])
def submit():
    questions = Question.query.all()
    correct_answers = 0
    total_questions = len(questions)

    for question in questions:
        user_answer = request.form.get(f'question{question.id}')
        if user_answer == question.answer:
            correct_answers += 1

    result = f'{total_questions} sorudan {correct_answers} tanesini bildin!! 🎉🎉'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
