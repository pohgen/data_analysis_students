## Data Analysis Project with Web Scraping and BigQuery Integration

### Project Overview

You will find a full overview of the statistics in this file: [Data_Analysis.ipynb](./Analysis_of_a_Private_Uniwercity_Database.ipynb)

This project focuses on data collection, storage, transformation, and analysis using a custom-built web scraper, Google BigQuery, SQL, and Python-based data processing techniques. The dataset comprises student-related data extracted from multiple sources, integrated into a single table, and analyzed to derive insights.

### Data Collection
The dataset was obtained through a web scraper written in Python, leveraging the following technologies:
- **BeautifulSoup4 (bs4)** – for parsing HTML content
- **requests** – for making HTTP requests to retrieve web pages
- **dataclasses** – for structured storage of extracted information

The scraper extracted data from four different web pages and saved them into four CSV files:
1. `parsed_csv/Students_Home_Info_Dataset.csv` – Containing home details (Sleep hours, study hours).
2. `parsed_csv/Students_Personal_info_Dataset.csv` – Containing personal details.
3. `parsed_csv/Students_Univercity_Dataset.csv` – Containing performance-related statistics.
4. `parsed_csv/Students_Parents_Info_Dataset.csv` – Containing family and background information (Family Income, Family Education).

### Data Storage and Transformation
The extracted CSV files were manually uploaded to **Google BigQuery**, where each file was stored as a separate table. SQL queries were then used to merge these tables into a unified dataset using **Student_ID** as the primary key. This approach ensured data integrity by eliminating duplicates, thereby conforming to **First Normal Form (1NF)**.

The merging process was accomplished using the following SQL query:

```sql
CREATE TABLE `.students` AS
SELECT * 
FROM .students_personal_info 
JOIN .students_university USING (Student_ID)
JOIN .students_home_info USING (Student_ID)
JOIN .parents_info USING (Student_ID);
```

### Data Retrieval and Exploration
A custom Python script was written to connect to **Google BigQuery**, retrieve the unified table, and load it into a **pandas DataFrame** for further processing. 

For a detailed exploration of the dataset, refer to the **Jupyter Notebook** located in the root directory of this project: 

[Notebook: Data_Analysis.ipynb](./Analysis_of_a_Private_Uniwercity_Database.ipynb)

### Data Cleaning
Data cleaning was performed to ensure consistency and reliability. This included:
- Handling missing values
- Removing inconsistencies

### Data Analysis and Visualization
Once the dataset was cleaned, it was subjected to exploratory data analysis (EDA). Various statistical techniques and visualizations were applied using the following technologies:
- **pandas** – Data manipulation and processing
- **numpy** – Numerical analysis
- **matplotlib** & **seaborn** – Data visualization

All charts and visualizations, including correlation matrices, histograms, and trend analyses, can be found in the **Jupyter Notebook** mentioned above.

### Conclusion
This project demonstrated a full data pipeline, from web scraping to storage, transformation, and analysis. The integration of **BigQuery** allowed for efficient handling of large datasets, and the analytical process provided valuable insights into student behavior, academic performance, and family backgrounds.

For further details, please refer to the [Data_Analysis.ipynb](./Analysis_of_a_Private_Uniwercity_Database.ipynb) file in the root directory.

## Contact
For questions or contributions, feel free to reach out:

- **Email**: haliuta.oleksandr@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/oleksandr-haliuta/
