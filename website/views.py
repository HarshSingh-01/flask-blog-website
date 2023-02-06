from flask import request, render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, Post
from . import db

views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    posts = Post.query.filter_by(public=True).all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        status = request.form.get('status')
        public = True if status else False
        # print([title, body, public])
        if len(title)==0:
            flash('Title can\'t be empty!', category='error')
        elif len(body)==0:
            flash('Content can\'t be empty!', category='error')
        else:
            new_post = Post(title=title, content=body, public=public, author=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash("Post Created!", category='message')
            return redirect(url_for('views.home'))
        
    return render_template("create_post.html", user=current_user)

@views.route('/posts/<username>')
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('User doesn\'t exist!', category='error')
        return redirect(url_for('views.home'))
    
    posts = Post.query.filter_by(author=user.id).all()
    return render_template('posts.html', posts=posts, user=current_user, username=username)


@views.route('/edit-post/<id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not post:
            flash('Post doesn\'t exist!', category='error')
        elif current_user.id != post.author:
            flash('You don\'t have permission to edit the post!', category='error')
        else:
            post.title = request.form.get('title')
            post.content = request.form.get('body')
            status = request.form.get('status')
            post.public = True if status else False
            # print([request.form.get('title'), request.form.get('body'), request.form.get('status')])
            db.session.commit()
            flash('Post has been edit!', category='success')
            return redirect(url_for('views.home'))
    return render_template('edit_post.html', post=post, user=current_user)

@views.route('/delete-post/<id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('Post doesn\'t exist!', category='error')
    elif current_user.id != post.author:
        flash('You don\'t have permission to delete the post!', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted!', category='success')

    return redirect(url_for('views.home'))