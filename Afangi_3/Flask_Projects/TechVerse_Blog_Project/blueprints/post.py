from flask import Blueprint, render_template, g, request, redirect, url_for, flash
import uuid
import datetime
from managers import initialize_firebase

post_bp = Blueprint('post', __name__)

# Initialize Firebase
db, auth = initialize_firebase()

@post_bp.route('/view_post/<post_id>', methods=['GET', 'POST'])
def view_post(post_id):
    post_details = db.child("posts").child(post_id).get().val()
    if not post_details:
        return "Post not found", 404
    replies = post_details.get('replies', {})

    if request.method == 'POST' and g.user:
        reply_content = request.form.get('content')
        reply_id = str(uuid.uuid4())
        reply = {
            "reply_content": reply_content,
            "reply_author_id": g.user['user_id'],
            "reply_author_email": g.user['user_email'],
            "timestamp": datetime.datetime.now().isoformat()
        }
        db.child("posts").child(post_id).child("replies").child(reply_id).set(reply)
        return redirect(url_for('post.view_post', post_id=post_id))

    return render_template('navigation/view_post.html', post=post_details, post_id=post_id, replies=replies)

@post_bp.route('/edit_post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post_details = db.child("posts").child(post_id).get().val()
    if not post_details:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')

        db.child("posts").child(post_id).update({
            "title": title,
            "content": content,
            "category": category,
            "last_updated": datetime.datetime.now().isoformat()
        })
        flash('Post updated successfully', 'success')
        return redirect(url_for('post.view_post', post_id=post_id))

    return render_template('post/edit_post.html', post=post_details)

@post_bp.route('/delete_post/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    post_details = db.child("posts").child(post_id).get().val()
    if not post_details:
        return "Post not found", 404

    if request.method == 'POST':
        db.child("posts").child(post_id).remove()
        flash('Post deleted successfully', 'success')
        return redirect(url_for('home'))

    return render_template('post/delete_post.html', post=post_details)
