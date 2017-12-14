from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class CustomFlask(Flask):
    """what the fuc is redefining this?"""
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(

    ))

app = CustomFlask(__name__)
app.config.from_pyfile('db.cfg')
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    done = db.Column(db.Boolean)

    def __init__(self, title):
        self.title = title

    def get_dict(self):
        return {
            """defining shit"""
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example')
def example():
    message = "Hello Flask!"
    return render_template('exmaple.html', message=message)

@app.route('/more')
def more():
    return render_template('more.html')

def initialize_database():
    app.logger.info('Database not created')

@app.route('/sqlalchemy')
def sqlalchemy():
    pass

@app.route('/sqlalchemy/get', methods=['GET'])
def sqlalchemy_get():
    pass

@app.route('/sqlalchemy/new', methods=['POST'])
def sqlalchemy_new():
    pass

@app.route


if __name__ = '__main__':
    app.run(debug=True)