from app1 import app, db
import os

# For Railway/Production deployment
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
else:
    # For gunicorn production server
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(f"Database initialization warning: {e}")
        pass
