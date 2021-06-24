import json
import random
import numpy as np
import traceback
import re 
import requests

from datetime import date, datetime

from flask import redirect, url_for, send_from_directory, request, render_template, flash, Blueprint
from flask import current_app as app
from flask_security import current_user, login_required, roles_accepted

from lobe.db import get_verifiers, get_verifiers_and_admins
from lobe.models import (PostAward, User, VerifierIcon, VerifierFont, VerifierTitle,
                         VerifierQuote, VerifierProgression, Recording, db,
                         SocialPost, PostAward)
from lobe.forms import (DailySpinForm, VerifierIconForm, VerifierTitleForm,
                        VerifierQuoteForm, VerifierFontForm, PostLinkForm)

feed = Blueprint(
    'feed', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/feed/static')

@feed.route('/lobe_feed/', methods=['GET'])
@login_required
@roles_accepted('Greinir', 'admin')
def lobe_feed():
    posts = SocialPost.query.order_by(SocialPost.created_at)
    verifiers = sorted(
        get_verifiers_and_admins(),
        key=lambda v: -v.progression.weekly_verifies)
    return render_template(
        'lobe_feed.jinja',
        posts=posts,
        verifiers=verifiers,
        )
     
        
@feed.route('/feed/post_recording/<int:recording_id>/', methods=['GET'])
@login_required
@roles_accepted('Greinir', 'admin')
def post_recording_feed(recording_id):
    if current_user.progression.experience >= 100:
        recording = Recording.query.get(recording_id)
        post = SocialPost(current_user.id, recording_id=recording.id)
        db.session.add(post)
        db.session.commit()
        if post:
            flash("Upptaka hengd á vegg", category="success")
            current_user.progression.experience -= 100
            db.session.commit()
        else:
            flash("Ekki tókst að hengja upptöu á vegg", category="warning")
    else:
        flash("Ekki næg innistæða", category="warning")
    return redirect(url_for('feed.lobe_feed'))
    

@feed.route('/feed/delete_social_post/<int:post_id>/', methods=['GET'])
@login_required
@roles_accepted('Greinir', 'admin')
def delete_social_post(post_id):
    post = SocialPost.query.get(post_id)
    if current_user.id == post.user.id or current_user.is_admin():
        db.session.delete(post)
        db.session.commit()
        if post:
            flash("Fjarlægt af vegg", category="success")
        else:
            flash("Ekki tókst að fjarlægja af vegg", category="warning")
    return redirect(url_for('feed.lobe_feed'))
       

@feed.route('/feed/award_post/<int:post_id>/basic', methods=['GET'])
@login_required
@roles_accepted('Greinir', 'admin')
def basic_award_post(post_id):
    if current_user.progression.experience >= 50:
        post = SocialPost.query.get(post_id)
        award = PostAward(current_user.id, post, 50)
        db.session.add(award)
        db.session.commit()
        if award:
            current_user.progression.experience -= 50
            post.user.progression.experience += 50
            flash("Verðlaunað", category="success")
        else:
            flash("Ekki tókst að verðlauna", category="warning")
    else:
        flash("Ekki næg innistæða", category="warning")
    return redirect(url_for('feed.lobe_feed'))
        
@feed.route('/feed/award_post/<int:post_id>/super', methods=['GET'])
@login_required
@roles_accepted('Greinir', 'admin')
def super_award_post(post_id):
    if current_user.progression.experience >= 100:
        post = SocialPost.query.get(post_id)
        award = PostAward(current_user.id, post, 100)
        db.session.add(award)
        db.session.commit()
        if award:
            current_user.progression.experience -= 100
            post.user.progression.experience += 100
            flash("Verðlaunað", category="success")
        else:
            flash("Ekki tókst að verðlauna", category="warning")
    else:
        flash("Ekki næg innistæða", category="warning")
    return redirect(url_for('feed.lobe_feed'))
        
@feed.route('/feed/create/link/', methods=['GET', 'POST'])
@login_required
@roles_accepted('Greinir', 'admin')
def feed_create_link():
    form = PostLinkForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            video_id = validate_youtube_link(form.link.data)
            if video_id:
                post = SocialPost(current_user.id, link=video_id)
                db.session.add(post)
                db.session.commit()
                if post:
                    flash("Hlekkur hengdur á vegg", category='success')
                return redirect(url_for('feed.lobe_feed'))
            else:
                flash("Hlekkur ekki á réttu sniði, aðeins youtube myndbönd passa hér", category='warning')
                return redirect(url_for('feed.lobe_feed'))
        except Exception as error:
            app.logger.error('Error posting link: {}\n{}'.format(
                error, traceback.format_exc()))
            flash(
                "Villa kom upp við að hengja hlekk upp",
                category='warning')
    return render_template(
        'forms/model.jinja',
        form=form,
        type='create',
        action=url_for('feed.feed_create_link'),
        section='verification')


def validate_youtube_link(link):
    reg = re.search("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$", link)
    if reg:
        string = reg.group()
        id_reg = re.search("((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)", string)
        if id_reg:
            video_id = id_reg.group()
            r = requests.get(f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg')
            if r.status_code == 200:
                return video_id
    return False


@feed.route('/feed/send_banner/')
def send_banner():
    try:
        return send_from_directory(
            app.config['STATIC_DATA_DIR'],
            'banner.png')
    except Exception as error:
        app.logger.error(
            "Error sending a beernight image : {}\n{}".format(
                error, traceback.format_exc()))
    return ''