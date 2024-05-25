
from flask import Blueprint, render_template, request, redirect, url_for, flash
from managers import initialize_firebase, NavigationMenuManager, CategoryManager

# Initialize Firebase
db, auth = initialize_firebase()

# Initialize Managers
navigation_manager = NavigationMenuManager()
category_manager = CategoryManager(db)

navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/navigation')
def navigation():
    menu_items = navigation_manager.get_menu_items()
    categories = category_manager.get_categories()
    return render_template('navigation/navigation.html', menu_items=menu_items, categories=categories)

@navigation_bp.route('/navigation/view_category/<category>/<subcategory>')
def view_category(category, subcategory):
    
    categories = category_manager.get_categories()
    parent_category = categories.get(category)
    
    
    if not parent_category:
        return "Parent category not found", 404


    subcategory_details = parent_category.get('subcategories', {}).get(subcategory)
    
    
    if not subcategory_details:
        return "Subcategory not found", 404
    
    
    posts_snapshot = db.child("posts").order_by_child("category").equal_to(subcategory_details['title']).get()
    posts = posts_snapshot.val() if posts_snapshot.val() else {}
    
    
    return render_template('navigation/view_category.html', subcategory=subcategory_details, parent_category=parent_category, posts=posts)


@navigation_bp.route('/navigation/view_post/<string:post_id>')
def view_post(post_id):
    post = db.child("posts").child(post_id).get().val()
    replies = post.get('replies', {})
    return render_template('navigation/view_post.html', post=post, replies=replies)

