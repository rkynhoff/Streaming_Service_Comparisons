### **Data Dictionary**
This is the data dictionary associated with final dataframe, streaming_clean.					

| Field | Description | Source |  Data Type | Example |
|:------|:------------|:-------|:---------- |:--------|
| Title | The name of the movie or tv show. | From the original csv files| text string | Breakfast at Tiffany's |
| Content_Type | The title content, either "movie" or "tv." | Renamed from the original service platform dataframes. | text string | movie |
| Combined_Genres | Includes all available genres in alphabetical order. | Renamed from the original service platform dataframes. | text string | Comedy, Drama, Romance |
| Release_Year | The year the movie or tv show was released according to the streaming platform.  | Renamed from the original service platform dataframes. | int | 1961 |
| IMDb_ID | The IMDb ID, if present, a unique value used in the URL of the IMDb content listing. | Renamed from the original service platform dataframes. | text string | tt0054698 |
| IMDb_Avg_Rating | The average rating by customers on IMDb  | Renamed from the original service platform dataframes. | float | 7.6|
| IMDb_Votes_Count | The total number of votes by customers on IMDb | Renamed from the original service platform dataframes. | int | 197447 |
| Service_Name | The streaming platform name. | Created field based on the service from which the data came. | text string | AppleTV |
| Genre_1 | The first genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | Comedy |
| Genre_2 | The second genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | Drama |
| Genre_3 | The third genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | Romance |
| Genre_4 | The fourth genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | NaN | 
| Genre_5 | The fifth genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | NaN |
| Genre_6 | The sixth genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | NaN |
| Genre_7 | The seventh genre in the Combined_Genres field, if present. | Created field from splitting the genres field from the original file into individual columns. | text string | NaN | 