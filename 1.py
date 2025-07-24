from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Ласкаво просимо!</h1>
    <p>Це головна сторінка нашого сайту.</p>
    '''

@app.route('/about/')
def about():
    return '''
    <h1>Про нас</h1>
    <p>Ми — команда розробників, яка створює корисні веб-додатки.</p>
    '''

@app.route('/services/')
def services():
    return '''
    <h1>Наші послуги</h1>
    <ul>
        <li>Розробка сайтів</li>
        <li>SEO-оптимізація</li>
        <li>Підтримка проектів</li>
    </ul>
    '''

@app.route('/contact/')
def contact():
    return '''
    <h1>Контакти</h1>
    <p>Email: info@example.com</p>
    <p>Телефон: +380 99 123 4567</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
