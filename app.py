from flask import Flask, render_template, request, jsonify, url_for, redirect
from courses_data import COURSES
import os

app = Flask(__name__)

PDF_MAPPING = {
    "Programming for Problem Solving": "data_structures.pdf",
    "Data Structures": "data_structures.pdf",
    "Digital Electronics": "data_structures.pdf",
    # Add more mappings as needed
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/notes')
def notes():
    branch = request.args.get('branch')
    semester = request.args.get('semester')

    if not branch or not semester:
        return render_template('notes.html')
    
    try:
        semester = int(semester)
        courses = COURSES.get(branch, {}).get(semester, [])
        return render_template('search_results.html', 
                             courses=courses, 
                             branch=branch, 
                             semester=semester)
    except ValueError:
        return render_template('notes.html', error="Invalid semester value")
    
@app.route('/pdf_viewer/<subject>')
def pdf_viewer(subject):
    pdf_file = PDF_MAPPING.get(subject)
    
    if pdf_file and os.path.exists(os.path.join('static', 'pdfs', pdf_file)):
        return render_template('pdf_viewer.html', subject=subject, pdf_file=pdf_file)
    return render_template('pdf_viewer.html', subject=subject, pdf_file=None)

    
@app.route('/pyq')
def pyq():
    branch = request.args.get('branch')
    semester = request.args.get('semester')
    year = request.args.get('year')

    if not branch or not semester:
        return render_template('pyq.html')
    
    try:
        semester = int(semester)
        courses = COURSES.get(branch, {}).get(semester, [])
        return render_template('search_results.html', 
                             courses=courses, 
                             branch=branch, 
                             semester=semester,
                             year=year,
                             page_type='pyq')
    except ValueError:
        return render_template('pyq.html', error="Invalid semester value")
    
@app.route('/study_guide')
def study_guide():
    return render_template('study_guide.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html') 



if __name__ == '__main__':
    app.run(debug=True)

