#app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = 'secret key'
 
DB_HOST = "localhost"
DB_NAME = "CSE412ProjectDatabase"
DB_USER = "postgres"
DB_PASS = "password"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM everything"
    cur.execute(s) # Execute the SQL
    listPersons = cur.fetchall()
    return render_template('index.html', listPersons = listPersons)

 
@app.route('/add_person', methods=['POST'])
def add_person():
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST':
            state_name = request.form['state_name']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            date_of_birth = request.form['date_of_birth']
            party = request.form['party']
            gender = request.form['gender']
            ethnicity = request.form['ethnicity']
            religion = request.form['religion']
            voterid = request.form['voterid']
            posid = request.form['posid']
            entered_term = request.form['entered_term']
            end_term = request.form['end_term']
            district = request.form['district']
            Class = request.form['class']
            senator_title = request.form['senator_title']
            rep_title = request.form['rep_title']
            office_address = request.form['office_address']
            website = request.form['website']
            cur.execute("INSERT INTO everything (state_name, first_name, last_name, date_of_birth, party, gender, ethnicity, religion, voterid, posid, entered_term, end_term, district, Class, senator_title, rep_title, office_address, website) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (state_name, first_name, last_name, date_of_birth, party, gender, ethnicity, religion, voterid, posid, entered_term, end_term, district, Class, senator_title, rep_title, office_address, website))
            #conn.commit()
            flash('Person Added successfully')
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))
    return redirect(url_for('Index'))


@app.route('/edit_person/<voterid>', methods=['GET'])
def edit_person(voterid):
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = """SELECT * FROM everything WHERE voterid = %s"""
        cur.execute(query, (voterid,))
        data = cur.fetchall()
        cur.close()
        return render_template('edit.html', everything = data[0])
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))
 
    return "Failed."


@app.route('/update/<voterid>', methods=['POST'])
def update_person(voterid):
    if request.method == 'POST':
        state_name = request.form['state_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        party = request.form['party']
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        religion = request.form['religion']
        posid = request.form['posid']
        entered_term = request.form['entered_term']
        end_term = request.form['end_term']
        district = request.form['district']
        Class = request.form['class']
        senator_title = request.form['senator_title']
        rep_title = request.form['rep_title']
        office_address = request.form['office_address']
        website = request.form['website']
         
        try:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            query = """UPDATE everything SET state_name = %s, first_name = %s, last_name = %s, date_of_birth = %s, party = %s, gender = %s, ethnicity = %s, religion = %s, posid = %s, entered_term = %s, end_term = %s, district = %s, class = %s, senator_title = %s, rep_title = %s, office_address = %s, website = %s WHERE voterid = %s"""
            aTuple =  (state_name, first_name, last_name, date_of_birth, party, gender, ethnicity, religion, posid, entered_term, end_term, district, Class, senator_title, rep_title, office_address, website, voterid)
            cur.execute(query, aTuple)
            flash('Person Updated Successfully')
            #conn.commit()
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
        return redirect(url_for('Index'))

@app.route('/delete/<voterid>', methods = ['POST', 'GET'])
def delete_person(voterid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("DELETE FROM everything WHERE voterid = %s", (voterid,))
    #conn.commit()
    flash('Person Removed Successfully')
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
