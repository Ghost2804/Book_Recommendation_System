from flask import Flask, render_template, request
import pickle
import numpy as np

# Load preprocessed data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

# Home page: Popular books
@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num-ratings'].values),
        rating=list(popular_df['avg-ratings'].values),
    )

# Recommendation page UI
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

# Recommendation logic
@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input']

    # Check if user input exists in the dataset
    if user_input in pt.index:
        # Retrieve similarity scores for the input book
        book_index = np.where(pt.index == user_input)[0][0]
        similar_books = sorted(
            list(enumerate(similarity_scores[book_index])),
            key=lambda x: x[1],
            reverse=True
        )[1:6]  # Top 5 recommendations (excluding the input book itself)

        recommendations = []
        for i in similar_books:
            book_title = pt.index[i[0]]
            book_info = books[books['Book-Title'] == book_title].iloc[0]
            recommendations.append([
                book_info['Book-Title'],
                book_info['Book-Author'],
                book_info['Image-URL-M'],
            ])

        return render_template('recommend.html', data=recommendations)
    else:
        # Handle case when the book is not found
        return render_template(
            'recommend.html',
            data=None,
            error=f"No results found for '{user_input}'. Please try another title."
        )

if __name__ == '__main__':
    app.run(debug=True)
