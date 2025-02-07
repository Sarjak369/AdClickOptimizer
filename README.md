
# AdClickOptimizer: Predictive System for Ad Click-Through Rates 🎯


A machine learning system to predict ad click-through rates (CTR) with **96% accuracy**, enabling advertisers to optimize ad placements and maximize revenue.

<img width="1404" alt="Home_Page_1" src="https://github.com/user-attachments/assets/2a762413-573b-43a5-92b5-9aa2c70335f1" />

<img width="1404" alt="Home_Page_2" src="https://github.com/user-attachments/assets/130cbd1a-f273-447e-aa44-3457b0d7c24f" />


## 📌 Overview
**AdClickOptimizer** leverages user behavior data to predict whether a user will click on an advertisement. Built with Python, Flask, and Scikit-learn, this project combines statistical analysis, feature engineering, and machine learning to deliver actionable insights for digital advertising campaigns.

## 🚀 Key Features
- **96% Accuracy**: Achieved using Random Forest and Linear Support Vector Classifier.
- **Time-Based Feature Engineering**: Extracted **month, day, hour, and weekday** from timestamps to capture temporal patterns.
- **Feature Selection**: Focused on human-centric features (`Daily Time Spent`, `Age`, `Area Income`, etc.) while omitting noisy categorical variables.
- **Flask Web App**: Real-time predictions via a user-friendly interface.
- **Comprehensive Analysis**: EDA, statistical tests (T-test, Mann-Whitney U), and correlation heatmaps.

  



<h2>🖱 User-Response-Prediction: What, why, and how ?</h2>

<img align = "right" src="https://miro.medium.com/max/960/1*hIPMAi6s0xF23Y8GWcPWWA.gif" style="width:300px;height:160px;"></img>    

- The online advertisement industry has become a multi-billion industry, and predicting ad **CTR** (click-through rate) is now central. Nowadays, different types of advertisers and search engines rely on modeling to predict ad CTR accurately.

- We will be predicting the ad click-through rate using the machine learning approach.

- **CTR**: It is the metric used to measure the percentage of impressions that resulted in a click.

- Paid search advertising is a popular form of **Pay per click (PPC)** advertising in which brands or advertisers pay (bid amount) to have their ads displayed when users search for specific keywords.

- How to calculate ad click prediction by performing machine learning modelling on a dataset. We have build a Logistic Regression model that would help us predict whether a user will click on an ad or not based on the features of that user. And hence calculate the probability of a user clicking on an ad.

- Using these probabilities, search engines could decide which ads to display by multiplying the possibilities with the bid amount and sorting it out.

<h2> ✒ Problem Statement</h2>

- Develop a machine learning algorithm that predicts if a particular user will click on an advertisement.


The data consists of **10** variables:

**'Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country', Timestamp' and 'Clicked on Ad'.**

- The primary variable we are interested in is ```'Clicked on Ad'```.

<i>This variable can have two possible outcomes: 0 and 1, where 0 refers to a user who didn't click the advertisement, while one refers to the scenario where a user clicks the ad.</i>

- We will see if we can use the other **9** variables to accurately predict the value **'Clicked on Ad'** variable. 

- We have also performed exploratory data analysis to see how **'Daily Time Spent on Site'** in combination with **'Ad Topic Line'** affects the user's decision to click on the ad.

## 📌 Overview
**AdClickOptimizer** leverages user behavior data to predict whether a user will click on an advertisement. Built with Python, Flask, and Scikit-learn, this project combines statistical analysis, feature engineering, and machine learning to deliver actionable insights for digital advertising campaigns.

## 🚀 Key Features
- **96% Accuracy**: Achieved using Random Forest and Linear Support Vector Classifier.
- **Time-Based Feature Engineering**: Extracted **month, day, hour, and weekday** from timestamps to capture temporal patterns.
- **Feature Selection**: Focused on human-centric features (`Daily Time Spent`, `Age`, `Area Income`, etc.) while omitting noisy categorical variables.
- **Flask Web App**: Real-time predictions via a user-friendly interface.
- **Comprehensive Analysis**: EDA, statistical tests (T-test, Mann-Whitney U), and correlation heatmaps.

## 📊 Results
### Model Performance Comparison

| Algorithm                               | Accuracy |
| :-------------------------------------  | :------- | 
| `LogisticRegression`                    | 95.33% |
| `RandomForestClassifier`                | 96% |
| `XGBClassifier`                         | 95% |
| `Linear Support Vector Classification`  | 95.33% |
| `k Nearest Neighbors Classifier`        | 95% |

<h2> ✔ How to Install and Use</h2>

- Install Python. Download my repo and change to directory of repo.
- To install the required packages and libraries, run this command in the project directory after cloning the repository:

**On command prompt, run**
```
pip install -r requirements.txt
```
**Running the app**

Go to this app's directory and run
```
python app.py
```


🌐 Usage

Input user details:

- Daily Time Spent (minutes)

- Age

- Area Income

- Daily Internet Usage

- Gender (0/1)

- Click PREDICT to get the probability of ad click (0 or 1).


<img width="1199" alt="Example_Input" src="https://github.com/user-attachments/assets/8318ea2d-4ee6-4e0c-9f22-35b1ed257d60" />

<img width="1115" alt="Example_Output" src="https://github.com/user-attachments/assets/1a2ce624-8683-4380-b049-8e1bc5c443c9" />



Optimize your ad strategy today! ✨



