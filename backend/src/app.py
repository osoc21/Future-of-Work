from api import create_app
import os

app = create_app()

if __name__ == "__main__":
    PORT = os.getenv('FLASK_RUN_PORT')
    ENV = os.getenv('ENV')
    app.run(
        host='0.0.0.0',
        port=PORT if PORT else 4000
    )
