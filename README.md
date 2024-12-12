# Book Recommendation System

## Project Overview
This project is a **Book Recommendation System** built to help users discover books based on their interests. It uses data from the [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) available on Kaggle.

## Development Process
1. **Data Understanding and Preparation**:
   - The dataset was first analyzed using the `Analysis.ipynb` file to understand the structure and clean the data.
   - The processed data was then converted into `.pkl` files for efficient usage in the Flask application.

2. **Implementation in Flask**:
   - The Flask framework was used to build the backend logic for handling user interactions and generating book recommendations.
   - HTML and CSS were used for designing the frontend interface.

3. **Technologies Used**:
   - **Flask**: Backend framework for handling routes and server logic.
   - **HTML/CSS**: For creating the frontend and styling the application.
   - **AI/ML Algorithms**: For generating book recommendations.

## Features
- Book recommendation functionality based on user preferences.
- Simple and user-friendly interface.
- Powered by Flask for backend operations.

## Project Structure
The main structure of the project includes the following:

```
├── app.py
├── requirements.txt
├── templates
│   ├── index.html
│   ├── recommendation.html
├── static
│   ├── [CSS/JS files or other static assets]
├── Analysis.ipynb
├── [Additional files, if applicable]
```

### Explanation:
- **`app.py`**: The main Flask application file where all routes and backend logic are defined.
- **`templates/`**: Contains the HTML files (‘index.html’ and ‘recommendation.html’). These files are stored in the `templates` directory so Flask can properly locate and render them.
- **`static/`**: Contains any static files such as CSS, JavaScript, or images used in the project.
- **`Analysis.ipynb`**: Jupyter Notebook used for analyzing and preprocessing the dataset.
- **`requirements.txt`**: A file listing all the Python dependencies needed to run the project.

## Setup and Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-link>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd <project-folder>
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## Folder Details
- **`templates/index.html`**: The home page where users can interact with the system.
- **`templates/recommendation.html`**: Displays the recommended books based on user inputs.

## Contribution
Feel free to contribute to the project by submitting issues or pull requests. Feedback and suggestions are always welcome!

