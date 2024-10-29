from . import db

# Clase 'User' correctamente definida
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def __repr__(self):
        return f'<User {self.username}>'

# Clase 'Task' (antes 'user') correctamente definida
class Todo(db.Model):  # Cambié 'user' a 'Task' por claridad
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ForeignKey correcto
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default=False)

    def __init__(self, created_by, title, desc, state=False):
        self.created_by = created_by
        self.title = title
        self.desc = desc
        self.state = state

    def __repr__(self):
        return f'<Todo: {self.title}>'
