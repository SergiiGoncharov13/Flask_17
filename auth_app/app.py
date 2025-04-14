from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from functools import wraps

from models import Users, db


app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)

# create db
with app.app_context():
    db.create_all()


# login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def index():
    return redirect(url_for('login'))


def admin_requered(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/admin')
@login_required
@admin_requered
def admin_panel():
    return f'<h1>Admin Panel</h1><p>Hello, {current_user.username} (Admin)</p>' # admin page


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!')
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        if Users.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('login'))

        new_user = Users(username=username, password=generate_password_hash(password), role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!')
        return redirect(url_for('login'))
    return render_template('login.html', register=True)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)

    