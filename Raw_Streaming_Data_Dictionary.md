### **Data Dictionary**
This is the data dictionary associated with the four original streaming service DataFrames. 				

| Field/Column  | Description | Source | Data Type | Example |
|:--------------|:------------|:-------|:----------|:--------|
| title | The name of the movie or tv show. | Original csv files  | text string | Breakfast at Tiffany's |
| type | The title content type, either "move" or "tv" | Original csv files | text string | movie |
| genres | Includes all available genres for the title. | Original csv files | text string  | Comedy, Drama, Romance |
| releaseYear | The year the movie or tv show was released according to the streaming platform. | Original csv files | int | 1961 |
| imdbId | The IMDb ID, if present, a unique value used in the URL of the IMDb content listing. | Original csv files | string | tt0054698 |
| imdbAverageRating | The average rating by customers on IMDb | Original csv files | float | 7.6 |
| imdbNumVotes | The total number of votes by customers on IMDb | Original csv files | int | 197447 |
| availableCountries | List of countries in which the title is available. | Original csv files | text string | CA, US |