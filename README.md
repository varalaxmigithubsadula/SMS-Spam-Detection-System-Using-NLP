# SMS Spam Detection System Using NLP

## Overview
An SMS spam detection system uses NLP techniques to analyze message text and classify it as spam or legitimate. It involves text preprocessing, feature extraction, and machine learning algorithms to identify spam patterns, ensuring secure and efficient communication.
SMS Spam Detection is a machine learning model that takes an SMS as input and predicts whether the message is a spam or not spam message. The model is built using Python and deployed on the web using Streamlit.

## Technology Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit

## Features
- Data collection
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Model building and selection
- Web deployment using Streamlit

### Data Collection
The SMS Spam Collection dataset was collected from Kaggle, which contains over 5,500 SMS messages labeled as either spam or not spam.
You can access the dataset from [here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)


You can access the dataset from [here](https://github.com/varalaxmigithubsadula/SMS-Spam-Detection-System-Using-NLP/blob/main/spam.csv)

### Data Cleaning and Preprocessing
Data cleaning and preprocessing prepare raw data by handling errors, removing duplicates, and standardizing formats. For text, it includes tokenization, stopword removal, and normalization to ensure reliable analysis or model training.
The data was cleaned by handling null and duplicate values, and the "type" column was label-encoded. The data was then preprocessed by converting the text into tokens, removing special characters, stop words and punctuation, and stemming the data. The data was also converted to lowercase before preprocessing.

### Exploratory Data Analysis
Exploratory Data Analysis (EDA) for an SMS spam detection system involves analyzing message lengths, word frequencies, and class distributions (spam vs. ham). Visualizations like word clouds and bar charts help identify key patterns and distinguish spam features.
Exploratory Data Analysis was performed to gain insights into the dataset. The count of characters, words, and sentences was calculated for each message. The correlation between variables was also calculated, and visualizations were created using pyplots, bar charts, pie charts, 5 number summaries, and heatmaps. Word clouds were also created for spam and non-spam messages, and the most frequent words in spam texts were visualized.

### Model Building and Selection
Model building for SMS spam detection uses algorithms like Naïve Bayes or SVM with features like TF-IDF. Selection is guided by metrics such as accuracy and F1-score for optimal performance.
Multiple classifier models were tried, including NaiveBayes, random forest, KNN, decision tree, logistic regression, ExtraTreesClassifier, and SVC. The best classifier was chosen based on precision, with a precision of 100% achieved.

### Web Deployment
Web deployment for an SMS spam detection system involves hosting the trained model on a server using frameworks like Flask or Django. Users can input messages via a web interface, and the system predicts spam or ham in real-time.
The model was deployed on the web using Streamlit. The user interface has a simple input box where the user can input a message, and the model will predict whether it is spam or not spam.

## Demo
To try out the SMS Spam Detection System Using NLP, visit [here](https://sms-spam-detection-system-using-nlp-speseqdtmdnrgekqjrgy7q.streamlit.app/).

## Usage
To use the SMS Spam Detection model on your own machine, follow these steps:

+ Clone this repository.
+ Install the required Python packages using 
```
pip install -r requirements.txt.
pip install streamlit
```
+ Run the model using 
```
 python -m streamlit run app.py
```
+ Visit http://localhost:8501 on your web browser to access the web app.

## Contributions
 If you find any issues or have any suggestions for improvement, please open an issue or a pull request on this repository.

