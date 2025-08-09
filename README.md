# DW_BI_Interventions_Analysis

## Project Overview
This project focuses on building a complete **Business Intelligence (BI)** solution for analyzing fire brigade interventions in Poland.  
The workflow covered the full data processing pipeline, including:

- **ETL Process** – implemented using **SQL Server Integration Services (SSIS)**
- **Data Warehouse** – designed in a **star schema** for analytical efficiency
- **OLAP Cube** – created to enable multidimensional analysis
- **BI Reports** – developed using Business Intelligence tools to provide clear and interactive insights

The dataset used for analysis was sourced from the official Polish government portal and contains information on fire brigade interventions across the country.

---

## Data Source and Licensing
- **Source 1:** Official Polish government portal with public datasets on fire brigade interventions [https://dane.gov.pl/pl/institution/22,komenda-glowna-panstwowej-strazy-pozarnej](https://dane.gov.pl/pl/institution/22,komenda-glowna-panstwowej-strazy-pozarnej)
- **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode.pl)
- **Note:** This repository does **not** contain the original dataset. Only the database model, ETL process, OLAP cube design, and sample visualizations are provided.  

---

## Features Implemented
1. **ETL Process (SSIS)** – automated extraction, transformation, and loading of intervention data  
2. **Data Warehouse** – optimized star schema with fact and dimension tables  
3. **OLAP Cube** – enabling multidimensional queries for advanced analytics  
4. **Sample BI Reports** – visualizations created using BI tools for decision-making support

---

## Example Reports
Below are example BI reports generated from the designed model and OLAP cube. These are based on transformed and aggregated data from the original dataset.

![Example Report 1](/images/report1.png)
![Example Report 2](/images/report2.png)
![Example Report 3](/images/report3.png)
![Example Report 3](/images/report4.png)
![Example Report 3](/images/report5.png)
