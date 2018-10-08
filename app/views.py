#coding:utf-8
from app import app
from flask import render_template,request
import pymysql
import datetime

@app.route('/')
@app.route('/index')
def index():
	return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
	w_name = request.form['w_name']
	w_annotation = request.form['w_annotation']
	w_initial = request.form['w_initial']
	print(w_initial)
	w_group = request.form['w_group']
	w_example = request.form['w_example']
	w_translation = request.form['w_translation']
	w_derivate = request.form['w_derivate']
	w_comment = request.form['w_comment']
	d_annotation = request.form['d_annotation']
	w_section = request.form['w_section']
	c_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(c_time)
	db = pymysql.connect("118.25.217.21","root","123456","english")
	cursor = db.cursor()
	sql = "insert into t_word(w_name, w_annotation, w_group, w_example, w_translation, w_derivate, w_comment, d_annotation, w_section, w_initial, c_time) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
	(w_name, w_annotation, w_group, w_example, w_translation, w_derivate, w_comment, d_annotation, w_section, w_initial, c_time)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()

	db.close()
	print(w_name,w_annotation,w_group,w_example,w_translation,w_derivate,w_comment,d_annotation,w_section)
	return render_template('login.html')