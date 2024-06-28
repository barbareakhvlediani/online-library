
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Book, Borrow
import datetime

main_bp = Blueprint('main', __name__,
                    template_folder='templates', url_prefix='/')


@main_bp.route('/books')
def book_details():
    books = Book.query.distinct().all()
    return render_template('main/book_details.html', books=books)


@main_bp.route('/home')
def index():
    print('shemovida')
    return render_template('main/index.html')


@main_bp.route('/borrow_book/<int:book_id>', methods=['POST'])
@login_required
def borrow_book(book_id):
    book = Book.query.get_or_404(book_id)
    if Borrow.query.filter_by(book_id=book_id, user_id=current_user.id, return_date=None).first():
        flash('You have already borrowed this book.', 'warning')
        return redirect(url_for('main.book_details'))
    else:
        borrow = Borrow(user_id=current_user.id, book_id=book_id, borrow_date=datetime.datetime.now(datetime.UTC))
        db.session.add(borrow)
        db.session.commit()
        flash(f'You have borrowed the book: {book.title}', 'success')
        return redirect(url_for('main.index'))
