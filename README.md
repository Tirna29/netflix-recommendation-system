# netflix-recommendation-system
# Data preprocessing:     
Instead of removing the undesired attributes, null values were replaced with empty strings as it would help in 
creating a model that is less prone to errors. As for the cast attribute, only the top 3 cast members are chosen for consistency around 
the cast attribute. To deal with the cast with the same first name, the space between first and last names were removed for the names to be unique. 

# Data Analysis:
1. Word Cloud Analysis: For the listedIn(Genre) attribute, this data visualization technique was used to infer the common words in different
   genres. In this technique, the word's size indicates its frequency compared to other words.

2. Bar Graph for top 20 countries: The counties with NaN values were marked as "Unkown" for this analysis. A dictionary was created for the number 
of shows in each country. This data was then plotted using a bar graph for the top 20 countries that produce shows/movies.

3. Count Plot Rating Frequency: This analysis provides the count of various ratings given to shows. This analysis was performed to understand the
   ratings better while developing the recommendation systems. For example, 'R' rated shows should not be suggested to a user watching 'G' rated shows.

4. Heat Map: This analysis was done to find the correlation between various genres. It provided many inferences about the type of shows made and 
   highly correlated genres.

5. Distribution of shows' duration: This analysis provides the mean or the average duration of these shows in the dataset.  

# Implementing KNN Classifier:

 1. Concatenated the desired attributes into one attribute called "tags" to find related shows. Each record was vectorized in a
  multidimensional space as it was difficult to compare text values.
2. The CountVectorizer Library was used to create vectors of 5000 words that are randomly chosen.
3. The distance between the vector of the shows whose recommendations were being provided was found. For this,
  the angles between the vectors were considerd. The lesser the angle, the closer the vectors.
4. Cosine similarity was used to find the similarity score between each record.
5. The recommendation system takes a show as input and does the following:
	- Search the show index in the dataset.
	- A max-heap will store the show recommendations with cosine similarity scores and the show index.
	- Applying pop operation k times to the max-heap for k recommendations and using them to locate their indices in the dataset. 


# Installation and Execution Instructions:

- Install Microsoft SQLServer Management Studio (SSMS) : https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16
- Install Microsoft SQL Server Express : https://www.microsoft.com/en-us/download/details.aspx?id=55994
- Install Microsoft Access Database Engine : https://www.microsoft.com/en-us/download/details.aspx?id=54920
- Open SSMS and click on 'Connect' and select Database Engine.
- Set server name by clicking on the dropdown button > select local servers > database engine and selecting the SQL express sever that we installed.
- Set the Authentication to Windows authentication and click on Connect.
- Import the Netflix.bacpac file as the database by following the steps:
	a. Open SSMS > from Object Explorer, right click on Databases.
	b. Select Import Data-tier Application.
	c. Click Import Settings.
	d. Ensure Import from local disk is checked.
	e. Browse the path and open the Netflix.bacpac file.
	f. Click Next and Next to import the database. 
- Download and Install Pycharm(IDE): Download Link: https://www.jetbrains.com/pycharm/
- Load all the packages required for running the project. 
  Package Installation Guide: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
	- Packages: pandas, NumPy, matplotlib, seaborn, wordcloud, sklearn.preprocessing, pyodbc, nltk.stem.porter,
	  sklearn.feature_extraction, sklearn.metrics.pairwise, heapq.
  - While importing data from database into IDE, change the name of the Server in the code as per the server selected in SSMS. Rename the database in 
 code as per the name of the database in SSMS.
 
