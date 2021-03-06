import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for, current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from sqlalchemy import text
from app.db.models import Transaction
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transactions = Blueprint('transactions', __name__,
                  template_folder='templates')


@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])
def transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html', data=data, pagination=pagination)
    except TemplateNotFound:
        abort(404)


@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    log = logging.getLogger("csvupload.log")
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        list_of_transactions = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                # for debugging:
                # print (row)
                list_of_transactions.append(Transaction(row['AMOUNT'], row['TYPE'],))

        current_user.transactions = list_of_transactions
        db.session.commit()

        log.info('A CSV Transaction CSV Was Uploaded')
        return redirect(url_for('transactions.transactions_browse'))

    try:

        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)

@transactions.route('/transactions/current', methods=['GET'])
def current_balance():
    sql = text('SELECT SUM(amount) AS current_balance FROM transactions')
    result = db.engine.execute(sql)
    balance = [row[0] for row in result]
    rv = str(balance[0])
    if rv == 'None':
        return '0'
    # else
    return str(balance[0])