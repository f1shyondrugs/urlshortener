from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<shortenedurl>')
def redirect(shortenedurl):
    if shortenedurl == '':
        return render_template('index.html')
    
    with open('static/urls.json') as f:
        data = json.load(f)
        return "<script>window.location.href = '" + data[shortenedurl] + "'</script>"
    
@app.route('/shorten', methods=['POST'])
def shorten():
    with open('static/urls.json') as f:
        data = json.load(f)
        data[request.form['shortenedurl']] = request.form['url']
    
    with open('static/urls.json', 'w') as f:
        json.dump(data, f)

    url = request.form['url']

    return {'url': url}

if __name__ == '__main__':
    app.run(debug=True)
