# **Streaming Service Comparision**

## Overview
This is my capstone project for CODE:You. The project analyzes four streaming services and their price histories to gain insights into content differences such as overall content amount, content types, genres, and more along with a comparison of price points. The goal of this project is to demonstrate a general knowledge of Python. 

![AppleTV+](https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Images/AppleTV.png | 250x250) ![Hulu](https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Images/Hulu.jpg | 250x250) ![Netflix](https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Images/Netflix.jpg | 250x250) ![PrimeVideo](Ihttps://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Images/Prime.png | 250x250)

## Data Sources:
Four of the datasets used in this project contain content information about each streaming service listed below, including title, content type, genre, release year, IMDb ID, and IMDb Average Rating, all of which came from kaggle.com. One dataset contains information related to pricing on each of the services for a specific timeframe noted as month-year. This dataset was manually derived. See details below 

- [Netflix](https://www.kaggle.com/datasets/octopusteam/full-netflix-dataset)<br>
- [Hulu](https://www.kaggle.com/datasets/octopusteam/full-hulu-dataset)<br>
- [Prime](https://www.kaggle.com/datasets/octopusteam/full-amazon-prime-dataset/data)<br>
- [AppleTV](https://www.kaggle.com/datasets/octopusteam/full-apple-tv-dataset)<br>
- [Streaming_Service_Pricing_Histories](https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Data/Streaming_Services_Pricing_Histories.csv)<br>
    - Manually Derived From: [Price_History_Reference.docx](https://github.com/rkynhoff/Streaming_Service_Comparisons/blob/main/Pricing_History_Reference.docx)

### Project Structure
---
This project is organized as follows:
- **Preliminary Data Exploration**: Jupyter notebooks or scripts to explore a dataset.
- **Preliminary Data Manipulation**: Using python for feature creation to differentiate the streaming service datasets. 
- **Data Cleaning & Preparation**: Using python and other packages to clean and prepare data for analysis. 
- **Analysis**: Using Python with the Pandas package to analyze the data. 
- **Visualizations**: Using Matplotlib and Seaborn to visualize my findings.
- **Summary**: Summary of analysis/findings. 

### Features Utilized for the Project
| Feature        | Description                           |
|----------------|---------------------------------------|
| Read FIVE data files| Used 4 CSV files from Kaggle & created one of my own. |
| Made 10 Seaborn Plots, 3 WordClouds, 1 Stacked Bar Chart & 1 Line Graph with Matplotlib| Made various plots to visually show my findings |
| Utilized a virtual environment | Created a venv for this project to keep my computer clean |
| Utilized Markdown & Commenting in my Jupyter Notebook | Included Markdown Language and commenting in my code to describe each section of my project & to define clear notes describing each code block. 

## **Getting Started**
The following is a guide to running the project files locally: 
1. If you want to save a copy on your GitHub, fork the repository located [here](https://github.com/rkynhoff/Streaming_Service_Comparisons.git), otherwise, move to step 2
2. In your command center or in the terminal of VS Code, clone the repository to your on your local machine: 'git clone https://github.com/rkynhoff/Streaming_Service_Comparisons.git'
    - Ensure your command center is opened to the folder in which you wish to save this repository
3. Follow the first three steps in the "Virtual Environment Instructions" to create and activiate a virtual environment, depending on your operating system (OS)
    - This step should also include installing the requirements.txt file
4. Explore the Juptyer notebooks and contents in the respective folders. 
5. Open the "STRM_SERV_COMP_V2.ipynb" file
6. In the toolbar, select "Run All" to run the program
7. Investigate the code blocks, comments, and markdown areas for insight into the program
8. Refer to the data dictionaries within the Jupyter Notebook located after the intitial DataFrames load and after the final cleaned DataFrame, or their respecitve ipynb files if needed
9. Helpful Hint: You may want to turn on Word Wrap as some of the cells contain comments/notes that would require scrolling without Word Wrap enabled
    - To do this in VS Code:
        - Select File > Preferences > Settings
        - Type in Word Wrap in the search
        - Toggle Word Wrap to "on" if not already on
    - Jupyter Notebooks online (JupyterLab,JupyerLite, etc.)
        - Select File > Wrap Words
        - Choose to turn it on
10. When you are finished perusing the repository, run the final line code for your OS from the Virtual Environment Instructions below

## Virtual Environment Instructions
Depending upon your OS, enter the commands below into your terminal to create, activate and install a virtual environment on your machine
Onlly use Deactivate when you are finished with the program
| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |

## **Dependencies**
- pandas and numpy for data manipulation and analysis
- matplotlib and seaborn for data visualization
- wordcloud for generating word cloud visuals
- PIL (Python Imagining Library) for image processing 