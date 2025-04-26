#imports
from app import myapp_obj, db
from app.models import User

# Create dummy test account on app start
with myapp_obj.app_context():
    test_user = User.query.filter_by(email="test@example.com").first()
    if not test_user:
        user = User(
            first_name="Test",
            last_name="User",
            dob="2000-01-01",  # Must match the string format in your model
            email="test@example.com",
            password="password123"
        )
        db.session.add(user)
        db.session.commit()

myapp_obj.run(debug=True)

