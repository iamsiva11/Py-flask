from flask import flask

app= Flask()

@app.route('/')
def index():
	return "Home Page"

@app.route('/page2')
def hello():
    return "Welcome to page 2"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hey there %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post id: %d' % post_id

if __name__ =="__main__":
	app.run(debug =True)