from flask import Blueprint, render_template, redirect, request, session, url_for
from auth.auth import login_required

home_bp = Blueprint('home_bp', __name__, static_folder='static', template_folder='templates')

images = [
    {
        'url': 'https://media.istockphoto.com/id/1854858577/photo/in-an-art-center-visitor-looks-at-the-artists-collection.webp?b=1&s=170667a&w=0&k=20&c=kO7iujCb6XNULpipLIemAhGcPrhJ5Jku4eNKpJevVdI=',
        'title': 'Image'
    },
    {
        'url': 'https://media.istockphoto.com/id/1440167941/photo/abstract-interior-design-3d-rendering-of-modern-showroom.webp?b=1&s=170667a&w=0&k=20&c=ZSFNEqB8mA8QtsgMNfPjwA8x1tK5YHzCWOInShfDgrM=',
        'title': 'Image'
    },
    {
        'url': 'https://media.istockphoto.com/id/1487468029/photo/empty-picturer-frame-on-wall.webp?b=1&s=170667a&w=0&k=20&c=wvaHhAf8BU71NCErsoWELRQxYJK7NGJ8enhxVjrUNAI=',
        'title': 'Image'
    },
    {
        'url': 'https://media.istockphoto.com/id/2056663893/photo/couple-in-virtual-reality-gallery.webp?b=1&s=170667a&w=0&k=20&c=Ek1y6M3kEW55Dd5a8a4ECQSQaJTqyfNreOEm_13PmvM=',
        'title': 'Image'
    },
    {
        'url': 'https://media.istockphoto.com/id/1455076848/photo/famous-uffizi-gallery-in-florence-italy.webp?b=1&s=170667a&w=0&k=20&c=DOLWPfZHDGvkVGnQxj38MuzmizLISgUUpYL6hwSnwyw=',
        'title': 'Image'
    },
    {
        'url': 'https://media.istockphoto.com/id/1421808392/photo/beautiful-paintings-on-wall-in-modern-art-gallery.webp?b=1&s=170667a&w=0&k=20&c=FzsV9tKI1RhwLivFgFXyaKujq5Cw5Fk7cZ3ebekef2E=',
        'title': 'Image'
    }
]

@home_bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('auth_bp.login'))
    
    return render_template('home.html')


@home_bp.route('/friends')
@login_required
def friends():
    return render_template('friends.html', images=images)
