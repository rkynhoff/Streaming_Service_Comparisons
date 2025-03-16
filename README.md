# **Streaming Service Comparision**

## Overview
This is my capstone project for CODE:You. The project analyzes four streaming services and their price histories to gain insights into content differences such as overall content amount, content types, genres, and more in comparison to price points. The goal of this project is to demonstrate a general knowledge of Python. 

## __Data Sources:__
Four of the datasets used in this project contains conent information about each streaming service listed below, including title, content type, genre, release year, IMDb ID, and IMDb Average Rating. One dataset contains information related to pricing on each of the services from for a specific timeframe. 

### Kaggle
- [Netflix](https://www.kaggle.com/datasets/octopusteam/full-netflix-dataset)<br>
- [Hulu](https://www.kaggle.com/datasets/octopusteam/full-hulu-dataset)<br>
- [Prime](https://www.kaggle.com/datasets/octopusteam/full-amazon-prime-dataset/data)<br>
- [AppleTV](https://www.kaggle.com/datasets/octopusteam/full-apple-tv-dataset)<br>
- [Streaming_Service_Pricing_Histories](https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Data/Streaming_Services_Pricing_Histories.csv)<br>
    - Manually Derived From: [Price_History_Reference.docx]|(https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Pricing_History_Reference.docx)

### Project Structure
---
This project is organized as follows:
- **Preliminary Data Exploration**: Jupyter notebooks or scripts to explore a dataset.
- **Preliminary Data Manipulation**: Using python for feature creation to differentiate the streaming service datasets. 
- **Data Cleaning & Preparation**: Using python and other packages to clean and prepare data for analysis. 
- **Analysis**: Using Python with the Pandas package to analyze the data. 
- **Visualizations**: Using Matplotlib and Seaborn to visualize my findings.

### Features Utilized for the Project
| Feature        | Description                           |
|----------------|---------------------------------------|
| Read FIVE data files| Used 4 CSV files from Kaggle & created one of my own. |
| Made # Plots | Made various plots to visually show my findings |
| Utilized a virtual environment | Created a venv for this project to keep my computer clean |
| Utilized Markdown & Commenting in my Jupyter Notebook | Included Markdown Language and commenting in my code to describe each section of my project & to define clear notes describing each code block. 

## **Getting Started**
The following is a guide to running the project files locally: 
1. If you want to save a copy on your GitHub, fork the repository located [here](https://github.com/rkynhoff/Streaming_Service_Comparisons.git), otherwise, move to step 2
2. In your command center, clone the repository to your on your local machine: 'git clone https://github.com/rkynhoff/Streaming_Service_Comparisons.git'
3. Install the necessary dependencies: 'pip install requirements.txt'
4. Follow the steps to create and activiate a virtual environment using the "Virtual Environment Commands to create a virtual environment" instructions below, depending on your OS
    - This step should also include installing the requirements.txt file
5. You should now be able to run the program using the "STRM_SERV_COMP_V2.ipynb" file
6. Explore the Juptyer notebooks or scripts in the respective folders. 
7. Refer to the "Data_Dictionary.ipynb" file if needed
8. Helpful Hint: You may want to turn on Word Wrap as some of the cells contain notes that would require scrolling without Word Wrap enabled
    - To do this in VS Code:
        - Select File > Preferences > Settings
        - Type in Word Wrap in the search
        - Toggle Word Wrap to "on" if not already on
    - Jupyter Notebooks online (JupyterLab,JupyerLite, etc.)
        - Select File > Wrap Words
        - Choose to turn it on

## **Dependencies**
- pandas and numpy for data manipulation and analysis
- pysprark and SparkSession for distributed computing and big data processing
- matplotlib and seaborn for data visualization
- wordcloud for generating word cloud visuals
- PIL (Python Imagining Library) for image processing 

## Virtual Environment Instructions
| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |