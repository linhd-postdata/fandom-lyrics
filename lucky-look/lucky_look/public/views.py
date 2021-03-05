# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
import os

import pandas as pd
from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    url_for, send_from_directory,
)
from werkzeug.utils import secure_filename

from lucky_look import settings
# from lucky_look.processing import add_tokens
from lucky_look.processing import clean_df, clear_pipeline
from lucky_look.public.forms import UploadForm
from lucky_look.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    return render_template("public/home.html")


@blueprint.route("/about/")
def about():
    """About page."""
    current_app.logger.info("Hello from the about page!")
    return render_template("public/about.html")


@blueprint.route("/upload/", methods=['GET', 'POST', ])
def upload():
    """Upload page."""
    form = UploadForm()
    current_app.logger.info("Hello from the upload page!")
    tables = None
    titles = None
    if request.method == "POST":
        if form.validate_on_submit():
            f = form.file.data
            filename = secure_filename(f.filename)
            df = pd.read_csv(f)
            df = clean_df(df, pos_output=form.pos, get_deps=form.deps,
                          get_ner=form.ner, get_lemmas=form.lemmas,
                          rm_punct=form.punct, rm_spaces=form.spaces,
                          rm_stopwords=form.stop)
            df.to_csv(os.path.join(blueprint.root_path, settings.UPLOAD_FOLDER, filename))
            # tables = [df.head(1).to_html(classes='data')]
            # titles = df.columns.values
            clear_pipeline(['stopwords', 'punct', 'filter_pos', 'spaces'])
            return redirect(url_for('.uploaded_file', filename=filename))
        else:
            flash_errors(form)
    return render_template("public/upload.html", form=form, tables=tables, titles=titles)


@blueprint.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(blueprint.root_path, settings.UPLOAD_FOLDER), filename)


@blueprint.route("/visualize/")
def visualize():
    """About page."""
    return render_template("public/visualize.html")
