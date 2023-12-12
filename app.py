from flask import Flask, request, jsonify
import requests
import json
from datetime import datetime
import awsgi

app = Flask(__name__)
BASE_URL = "https://app.ylytic.com/ylytic/test"

@app.route('/search', methods=['GET'])
def search_comments():
    # Get parameters from the request
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Make a request to the original API
    response = requests.get(BASE_URL)
    comments_data = response.json()

    # Filter comments based on search criteria
    filtered_comments = []
    for comment in comments_data['comments']:
        comment_date_str = comment['at'].replace('/', '')  # Remove unwanted characters
        comment_date = datetime.strptime(comment_date_str, "%a, %d %b %Y %H:%M:%S GMT")
        
        if (not search_author or search_author.lower() in comment['author'].lower()) and \
           (not at_from or datetime.strptime(at_from, "%d-%m-%Y").date() <= comment_date.date() <= datetime.strptime(at_to, "%d-%m-%Y").date()) and \
           (not int(like_from) or int(like_from) <= int(comment['like']) <= int(like_to)) and \
           (not int(reply_from) or int(reply_from) <= int(comment['reply']) <= int(reply_to)) and \
           (not search_text or search_text.lower() in comment['text'].lower()):
            filtered_comments.append(comment)

    return jsonify(filtered_comments)

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    app.run(debug=True)
