# **Stream Service Comparision Project**
An analysis of four streaming platforms.

## __Data Sources:__

### Kaggle
[Netflix|https://www.kaggle.com/datasets/octopusteam/full-netflix-dataset]
[Hulu|https://www.kaggle.com/datasets/octopusteam/full-hulu-dataset]
[Prime|https://www.kaggle.com/datasets/octopusteam/full-amazon-prime-dataset/data]
[AppleTV|https://www.kaggle.com/datasets/octopusteam/full-apple-tv-dataset]
[PriceHistory|https://www.kaggle.com/datasets/webdevbadger/streaming-service-prices/data]
https://www.kaggle.com/code/webdevbadger/streaming-service-prices-study#2.-Library-and-Settings 


## __Running the Program__
The following is a guide to running the project files locally: 
1. Fork the repository located [here|https://github.com/rkynhoff/Streaming_Service_Comparisons.git]
2. Clone the repository to your on your local machine
    - Git clone "repo url here"
3. Clone the repository to your local machine
4. Follow the steps to create and activiate a virtual environment using the "Virtual Environment Commands to create a virtual environment" instructions below, depending on your OS
    - This step should also include installing the requirements.txt file
5. You should now be able to run the program using the "STRM_SERV_COMP_V2.ipynb" file
6. Refer to the "Data_Dictionary.ipynb" file if needed
7. Helpful Hint: You may want to turn on Word Wrap as some of the cells contain notes that would require scrolling without Word Wrap enabled
    - To do this in VS Code:
        - Select File > Preferences > Settings
        - Type in Word Wrap in the search
        - Toggle Word Wrap to "on" if not already on
    - Jupyter Notebooks online (JupyterLab,JupyerLite, etc.)
        - Select File > Wrap Words
        - Choose to turn it on

## Virtual Environment Commands to create a virtual environment
| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |