from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Borrow
from app.extensions import db
from .forms import LoginForm, RegistrationForm

user_bp = Blueprint('user', __name__, template_folder='templates',
                    url_prefix='/user')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print('authorized')
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        print('validuria')
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            print()
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('user/login.html', form=form)
    print('aravaliduria an GET request')
    return render_template('user/login.html', form=form)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('user.login'))

    return render_template('user/register.html', form=form)


@user_bp.route('/profile')
@login_required
def profile():
    # borrows = Borrow.query.filter_by(user_id=current_user.id).all()
    return render_template('user/profile.html')


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
