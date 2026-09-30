# 📊 Sales Data Analyzer & Visualization

A **Python-based Sales Data Analysis and Visualization project** designed to perform data exploration, cleaning, statistical analysis, data manipulation, and visualization using **Pandas, NumPy, Matplotlib, and Seaborn**.

This project provides a simple **menu-driven interface** that allows users to load a CSV sales dataset and perform different data analysis operations without manually writing individual commands.

---

## 🚀 Project Overview

The **Sales Data Analyzer** is a console-based Python application that helps analyze sales data efficiently.

The project covers important concepts used in **Data Analysis**, including:

* CSV data handling
* Pandas DataFrame operations
* NumPy array operations
* Data cleaning
* Mathematical calculations
* Searching, sorting, and filtering
* Aggregate functions
* Statistical analysis
* GroupBy and Transform
* Pivot Tables
* Concatenation
* Merge and Join
* Data splitting
* Data visualization
* Saving visualizations

The application starts with a simple menu where users can select the required operation.

---

## ✨ Features

### 1. 📂 Load Dataset

Load a sales dataset from a CSV file.

The program:

* Reads the CSV file using Pandas
* Converts the `Date` column into datetime format
* Displays the total number of rows
* Handles file-not-found and other errors

---

### 2. 🔍 Explore Data

Explore the loaded dataset using:

* First 5 rows
* Last 5 rows
* Column names
* Data types
* Basic DataFrame information

---

### 3. 🔢 NumPy Operations

The project demonstrates NumPy operations on the Sales column, including:

* Converting Pandas data into a NumPy array
* Indexing
* Slicing
* Addition
* Multiplication
* Maximum value
* Minimum value

---

### 4. 🧮 Mathematical Operations

The application performs mathematical calculations such as:

* Increasing sales by 10%
* Calculating profit percentage

Formula used:

```text
Profit Percentage = (Profit / Sales) × 100
```

---

### 5. 🔎 Search, Sort & Filter

Users can:

* Search products
* Search sales values
* Sort sales in descending order
* Sort profit in descending order
* Filter data by region
* Filter sales greater than 50,000

---

### 6. 📈 Aggregate Functions

The project calculates:

* Total Sales
* Average Sales
* Highest Sales
* Lowest Sales
* Total Profit
* Average Profit
* Sales by Product
* Sales by Region

It uses Pandas aggregation and `groupby()` operations.

---

### 7. 📊 Statistical Analysis

The application performs statistical analysis on Sales and Profit data.

It includes:

* Descriptive statistics
* Standard deviation
* Variance
* 50th percentile
* 75th percentile

---

### 8. 🔄 GroupBy & Transform

The project calculates:

* Total sales for each product
* Percentage contribution of each sale to its product's total sales

This demonstrates the use of Pandas `groupby()` with `transform()`.

---

### 9. 📋 Pivot Table

A Pivot Table is created using:

* **Index:** Region
* **Columns:** Product
* **Values:** Sales
* **Aggregation:** Sum

This helps compare product sales across different regions.

---

### 10. 🔗 Combine Data

The project demonstrates combining additional sales records with the existing DataFrame using `pd.concat()`.

---

### 11. 🔀 Merge DataFrames

The application demonstrates merging sales data with region-manager information using Pandas `merge()`.

---

### 12. 🤝 Join DataFrames

The project demonstrates joining regional target information with the sales dataset using Pandas `join()`.

---

### 13. ✂️ Split Data

Sales data can be separated into different regional datasets:

* North
* South
* East
* West

---

### 14. 🧹 Handle Missing Data

The application checks for missing values and provides options to:

* Fill missing Sales values with the mean
* Fill missing Profit values with the mean
* Remove rows containing missing values

---

## 📊 Data Visualization

The project supports **9 different visualization options**:

| No. | Visualization | Purpose                           |
| --: | ------------- | --------------------------------- |
|   1 | Bar Plot      | Compare sales by product          |
|   2 | Line Plot     | Show sales trends                 |
|   3 | Scatter Plot  | Analyze Sales vs Profit           |
|   4 | Pie Chart     | Show sales distribution by region |
|   5 | Histogram     | Analyze sales distribution        |
|   6 | Stack Plot    | Compare product sales over time   |
|   7 | Box Plot      | Analyze sales distribution        |
|   8 | Heatmap       | Show Sales and Profit correlation |
|   9 | Subplots      | Display multiple charts together  |

---

## 💾 Save Visualization

After creating a visualization, the application allows the user to save the last generated graph as an image file.

Example:

```text
sales_chart.png
```

The project uses Matplotlib's `savefig()` method to save the visualization.

---

## 🛠️ Technologies Used

| Technology    | Purpose                        |
| ------------- | ------------------------------ |
| 🐍 Python     | Core programming language      |
| 🐼 Pandas     | Data manipulation and analysis |
| 🔢 NumPy      | Numerical operations           |
| 📈 Matplotlib | Data visualization             |
| 📊 Seaborn    | Statistical visualization      |
| 📄 CSV        | Dataset format                 |

The project imports Pandas, NumPy, Matplotlib, and Seaborn at the beginning of the program.

---

## 📁 Suggested Project Structure

```text
Sales-Data-Analyzer/
│
├── sales_analyzer.py
├── sales_data.csv
├── README.md
│
└── screenshots/
    ├── main_menu.png
    ├── data_exploration.png
    ├── statistical_analysis.png
    ├── bar_plot.png
    ├── line_plot.png
    ├── scatter_plot.png
    ├── pie_chart.png
    ├── histogram.png
    └── heatmap.png
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Sales-Data-Analyzer.git
```

### Step 2: Open the Project

```bash
cd Sales-Data-Analyzer
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 4: Run the Program

```bash
python sales_analyzer.py
```

---

## ▶️ How to Use

After running the program, the following menu is displayed:

```text
==================================================
        SALES DATA ANALYZER
==================================================

1. Load Dataset
2. Explore Data
3. NumPy Operations
4. Mathematical Operations
5. Search, Sort and Filter
6. Aggregate Functions
7. Statistical Analysis
8. GroupBy and Transform
9. Pivot Table
10. Combine Data using Concat
11. Merge Data
12. Join Data
13. Split Data
14. Handle Missing Data
15. Data Visualization
16. Save Visualization
17. Exit
```

### Example Workflow

```text
1. Load Dataset
       ↓
2. Explore Data
       ↓
3. Clean Missing Data
       ↓
4. Perform Analysis
       ↓
5. Statistical Analysis
       ↓
6. Create Visualizations
       ↓
7. Save Visualization
```

---

## 🖼️ Project Screenshots

Add your actual screenshots inside the `screenshots` folder and display them here.

### Main Menu

![Main Menu](screenshots/main_menu.png)

### Data Analysis

![Data Analysis](screenshots/data_exploration.png)

### Statistical Analysis

![Statistical Analysis](screenshots/statistical_analysis.png)

### Sales Visualization

![Sales Visualization](screenshots/bar_plot.png)

### Sales vs Profit

![Sales vs Profit](screenshots/scatter_plot.png)

### Correlation Heatmap

![Correlation Heatmap](screenshots/heatmap.png)

---

## 🎯 Learning Objectives

This project was developed to practice practical Data Analysis concepts using Python.

### Python

* Classes and Objects
* Methods
* Loops
* Conditional Statements
* Exception Handling
* User Input

### Pandas

* DataFrame
* CSV handling
* Filtering
* Sorting
* GroupBy
* Transform
* Pivot Table
* Merge
* Join
* Concat
* Missing Data Handling

### NumPy

* Arrays
* Indexing
* Slicing
* Mathematical operations
* Statistical operations

### Data Visualization

* Bar Chart
* Line Chart
* Scatter Plot
* Pie Chart
* Histogram
* Stack Plot
* Box Plot
* Heatmap
* Subplots

---

## 🧠 Key Concepts Demonstrated

This project demonstrates how Python libraries can be combined to create a complete data-analysis workflow:

```text
CSV Dataset
     ↓
Pandas
     ↓
Data Cleaning
     ↓
Data Manipulation
     ↓
NumPy Calculations
     ↓
Statistical Analysis
     ↓
Visualization
     ↓
Business Insights
```

---

## 🔮 Future Improvements

Possible future improvements include:

* Add a graphical user interface using Tkinter
* Add more advanced statistical analysis
* Add interactive dashboards
* Add automatic report generation
* Add Excel file support
* Add database connectivity
* Add more advanced filtering options
* Add export functionality for analysis results
* Add machine learning-based sales prediction

---

## 👨‍💻 Author

**Dharmendra Rajput**

BCA Graduate | Aspiring Data Analyst

### Skills

`Python` `Pandas` `NumPy` `Matplotlib` `Seaborn` `SQL` `Excel` `Data Analysis`

---

## ⭐ If You Like This Project

If you find this project useful for learning Python and Data Analysis:

⭐ **Star the repository**

🍴 **Fork the repository**

📌 **Explore the code**

---

## 📄 License

This project is created for **educational and learning purposes**.
