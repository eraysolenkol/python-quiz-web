from flask import Blueprint
from models import Question

api_bp = Blueprint('api', __name__)

@api_bp.route('/questions', methods=['GET'])
def questions():
    all_questions = Question.query.all()
    return {
        'questions': [
            {
                'id': question.id,
                'question': question.question,
                'choices': question.choices,
                'answer': question.answer
            } for question in all_questions
        ]
    }
