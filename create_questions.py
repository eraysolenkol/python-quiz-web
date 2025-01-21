import sqlite3

conn = sqlite3.connect('./databases/main.db')
cursor = conn.cursor()

def insert_question(question, answer, choices):
    cur_date = cursor.execute('SELECT CURRENT_TIMESTAMP').fetchone()[0]
    cursor.execute('''
    INSERT INTO question (question, answer, choices, date_created)
    VALUES (?, ?, ?, ?)
    ''', (question, answer, choices, cur_date))
    conn.commit()

questions = [
    ("Python'da makine öğrenmesi için hangi kütüphane yaygın olarak kullanılır?", "TensorFlow", "Matplotlib, TensorFlow, Flask, Django"),
    ("Python’da veri ön işleme için kullanılan kütüphanelerden biri nedir?", "Pandas", "NumPy, Keras, PyTorch, Pandas"),
    ("Hangisi doğal dil işleme (NLP) için kullanılan bir kütüphanedir?", "NLTK", "Matplotlib, Seaborn, NLTK, OpenCV"),
    ("Python'da derin öğrenme modelleri için yaygın kullanılan bir framework hangisidir?", "PyTorch", "PyTorch, Pandas, Flask, Scikit-learn"),
    ("Makine öğrenmesinde 'etiketli veri' ile çalışan algoritmalar hangi sınıfa girer?", "Denetimli öğrenme", "Denetimsiz öğrenme, Denetimli öğrenme, Pekiştirmeli öğrenme, Derin öğrenme"),
    ("Python’da görselleştirme yapmak için hangi kütüphane kullanılır?", "Matplotlib", "NumPy, Matplotlib, TensorFlow, Scikit-learn"),
    ("Görüntü işleme için kullanılan popüler Python kütüphanesi nedir?", "OpenCV", "OpenCV, Seaborn, PyTorch, Pandas"),
    ("'Overfitting' ne zaman meydana gelir?", "Model eğitilen veriyi ezberlediğinde", "Model eğitilen veriyi ezberlediğinde, Model hiç öğrenmediğinde, Model çok fazla veri olduğunda, Model yanlış veriyle eğitildiğinde"),
    ("Python’da hangi kütüphane matematiksel işlemler için kullanılır?", "NumPy", "Flask, NumPy, Scikit-learn, OpenCV"),
    ("Hangisi Python’da 'pekiştirmeli öğrenme (Reinforcement Learning)' için bir kütüphanedir?", "Gym", "Gym, Pandas, Scikit-learn, Matplotlib")
]

for question, answer, choices in questions:
    insert_question(question, answer, choices)

conn.close()
