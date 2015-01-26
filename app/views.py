from flask import render_template, flash, redirect
from app import app 

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
		title = 'Home'
		)

@app.route('/about')
def about():
	return render_template("about.html",
		title = 'About'
		)

#################################################################################
######################
###################### POST SECCTIONS ###########################################
######################
#################################################################################

#1
@app.route('/books')
def books():
	return render_template("books.html",
		title = 'Books'
		)

#2
@app.route('/drinks')
def drinks():
	return render_template("drinks.html",
		title = 'Books'
		)

#3
@app.route('/sermons')
def sermons():
	return render_template("sermons.html",
		title = 'Sermons'
		)

#4
@app.route('/tobacco')
def tobacco():
	return render_template("tobacco.html",
		title = 'Tobacco'
		)

#5
@app.route('/meta')
def meta():
	return render_template("meta.html",
		title = 'Meta'
		)

#6
@app.route('/ideas')
def ideas():
	return render_template("ideas.html",
		title = 'Ideas'
		)

#7
@app.route('/games')
def games():
	return render_template("games.html",
		title = 'Games'
		)

#8
@app.route('/startups')
def startups():
	return render_template("startups.html",
		title = 'Startups'
		)

#9
@app.route('/inspiration')
def inspiration():
	return render_template("inspiration.html",
		title = 'Inspiration'
		)

#10
@app.route('/art')
def art():
	return render_template("art.html",
		title = 'Art'
		)

#11
@app.route('/humor')
def humor():
	return render_template("humor.html",
		title = 'Humor'
		)

#12
@app.route('/hedgehog')
def hedgehog():
	return render_template("hedgehog.html",
		title = 'Hedgehog'
		)

#######################################################################################
######################
###################### POST SUB SECTIONS ##############################################
######################
#######################################################################################

#12
@app.route('/books/thtaht')
def thtaht():
	return render_template("thtaht.html",
		title = 'The Hard Thing About Hard Things'
		)

