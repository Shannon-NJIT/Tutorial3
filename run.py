import os
from blog_api.app import create_app

if __name__ == '__main__':
    env_name = os.getenv('Development')
    app = create_app(env_name)
    app.run(debug=True)