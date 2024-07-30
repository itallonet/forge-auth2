import os

from src import create_app

port = int(os.getenv('PORT', 50000)) 

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', port)))
