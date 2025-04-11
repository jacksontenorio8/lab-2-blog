from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando um banco de dados em memória
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return "Post não encontrado", 404
    return render_template('post-detail.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post_id = len(posts) + 1
        posts.append({'id': post_id, 'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')