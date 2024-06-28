from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user, login_required
from ..extensions import admin, db
from ..models import User, Book
from flask_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
    column_exclude_list = ['password']
    can_create = True
    can_edit = True
    can_delete = True
    page_size = 50


class BookAdminView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    column_searchable_list = ['title', 'author']
    column_filters = ['genre']


admin_bp = Blueprint('admin', __name__)

admin.init_app(admin_bp)


admin.add_view(UserAdminView(User, db.session))
admin.add_view(BookAdminView(Book, db.session))


@admin_bp.route('/')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('admin/manage_books.html')
