from flask import Flask, request, send_from_directory
from flask import render_template

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/about')
def about():
    return "<h1?> Робототехника это круто</h1>"
@app.route('/templates/<path:path>')
def send_js(path):
    return send_from_directory('templates', path)

    
if __name__ == "__main__":
    app.run()