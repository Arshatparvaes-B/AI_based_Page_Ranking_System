# from flask import Flask, render_template, request, redirect, url_for
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import os

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/searchresults')
# def search():
#     return render_template('searchresults.html')

# @app.route('/search-submit', methods=['POST'])
# def search_query_submit():
#     if request.method == 'POST':
#         query = request.form['query']
#         return redirect(url_for('search', q=query))


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query', '')
        return redirect(url_for('search', q=query))

    search_query = request.args.get('q', '')
    print(f"Search query: {search_query}")
    return render_template('searchresults.html', search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
