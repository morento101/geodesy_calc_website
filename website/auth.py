from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message
from website import mail


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash('Ви Вже Автоизовані')
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Успішна авторизація", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Неправильний пароль", category="error")
        else:
            flash("Такий користувач не існує", category="error")

    return render_template("auth.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if current_user.is_authenticated:
        flash('Ви Вже Зареєстровані')
        return redirect(url_for('views.home'))
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Такий користувач уже існує", category='error')
        elif len(email) < 17:
            flash('Пошта повинна бути завдовжки мінімум 18 знаків', category="error")
        elif len(password1) < 7:
            flash('Пароль повинен бути завдовжки мінімум 8 знаків', category="error")
        elif password1 != password2:
            flash('Паролі повинні бути однаковими', category="error")
        else:
            new_user = User(email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit() 
            flash('Аккаунт успішно створенно', category="success")
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Скинути Пароль', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f"""Щоб скинути пароль, перейдіть по цбому посиланню:
{url_for('auth.reset_token', token=token, _external=True)}
    
Якщо робили запит на скинення паролю - проігноруйте це повідомлення.
"""

    mail.send(msg)


@auth.route('/reset-password', methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        flash('Ви Вже Автоизовані')
        return redirect(url_for('views.home'))
    if request.method == "POST":
        email = request.form.get('reset_request')
        if email:
            user = User.query.filter_by(email=email).first()
            if user:
                send_reset_email(user)
                flash('Вам На Пошту Був Відпраленний Лист Із Подальшими Інструкціями', category='success')
                return redirect(url_for('auth.login'))
            else:
                flash('Користувача З Такою Електронною Пощтою Не Існує', category='error')
        else:
            flash('Введіть Електронну Пошту', category='error') 
    return render_template('reset/reset_request.html', user=current_user)



@auth.route('/reset-password/<token>', methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        flash('Ви Вже Автоизовані')
        return redirect(url_for('views.home'))
    user = User.verify_reset_token(token)
    if not user:
        flash('Час, Для Скидування Паролю, Вичерпаний', category='error')
        return redirect(url_for('auth.reset_request'))  
    if request.method == "POST":
        password1 = request.form.get('reset_password') 
        password2 = request.form.get('reset_password_confirm') 
        if password1 and len(password1) > 8:
            if password1 == password2:
                new_password = generate_password_hash(password1, method='sha256')
                user.password = new_password
                db.session.commit()
                flash('Пароль Успішно Зміненно', category='success')
                return redirect(url_for('auth.login'))
            else:
                flash('Паролі Повинні Бути Однакові', cayegory='error')  
        else:
            flash('Пароль Повинен Бути Завдовжики 8 Символів', category='error')
    return render_template('reset/reset_token.html', user=current_user)
