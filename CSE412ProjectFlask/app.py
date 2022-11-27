#app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "alanh"
 
DB_HOST = "localhost"
DB_NAME = "Testing"
DB_USER = "postgres"
DB_PASS = "password"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM everything"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)
 
@app.route('/add_person', methods=['POST'])
def add_person():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
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
        cur.execute("INSERT INTO everything (first_name, last_name, date_of_birth, party, gender, enthincity, religion, voterid, posid, entered_term, end_term, district, Class, senator_title, rep_title, office_address, website) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (first_name, last_name, date_of_birth, party, gender, enthincity, religion, voterid, posid, entered_term, end_term, district, Class, senator_title, rep_title, office_address, website))
        conn.commit()
        flash('Person Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<voterid>', methods = ['POST', 'GET'])
def get_employee(voterid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM everything WHERE voterid = %s', (voterid))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', everything = data[0])
 
@app.route('/update/<voterid>', methods=['POST'])
def update_student(voterid):
    if request.method == 'POST':
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
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE everything
            SET first_name = %s,
                last_name = %s,
                date_of_birth = %s
                party = %s,
                gender = %s,
                ethnicity = %s,
                religion = %s,
                voterid = %s,
                posid = %s,
                entered_term = %s,
                end_term = %s,
                district = %s,
                class = %s,
                senator_title = %s,
                rep_title = %s,
                office_address = %s,
                website = %s
            WHERE voterid = %s
        """, (first_name, last_name, date_of_birth, party, gender, ethnicity, religion, voterid, posid, entered_term, end_term, district, Class, senator_title, rep_title, office_address, website))
        flash('Person Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:voterid>', methods = ['POST','GET'])
def delete_student(voterid):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM everything WHERE id = {0}'.format(voterid))
    conn.commit()
    flash('Person Removed Successfully')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)
    app.run()
