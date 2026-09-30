import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    # -----------------------------------------
    # Constructor
    # -----------------------------------------
    def __init__(self):

        self.data = pd.DataFrame()

        # This stores the last graph
        self.last_plot = None

    # -----------------------------------------
    # Load CSV file
    # -----------------------------------------
    def load_data(self, file_path):

        try:

            self.data = pd.read_csv(file_path)

            # Convert Date into datetime
            self.data["Date"] = pd.to_datetime(
                self.data["Date"]
            )

            print("\nDataset loaded successfully!")
            print("Total rows:", len(self.data))

        except FileNotFoundError:

            print("\nFile not found.")
            print("Please check the file path.")

        except Exception as e:

            print("\nError:", e)

    # -----------------------------------------
    # Explore Data
    # -----------------------------------------
    def explore_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        while True:

            print("\n========== EXPLORE DATA ==========")

            print("1. First 5 rows")
            print("2. Last 5 rows")
            print("3. Column names")
            print("4. Data types")
            print("5. Basic information")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                print(self.data.head())

            elif choice == "2":

                print(self.data.tail())

            elif choice == "3":

                print(list(self.data.columns))

            elif choice == "4":

                print(self.data.dtypes)

            elif choice == "5":

                self.data.info()

            elif choice == "6":

                break

            else:

                print("Invalid choice.")

    # -----------------------------------------
    # Handle Missing Data
    # -----------------------------------------
    def clean_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== MISSING DATA ==========")

        missing = self.data.isnull().sum()

        print(missing)

        if missing.sum() == 0:

            print("\nNo missing values found.")

        else:

            print("\n1. Fill Sales with mean")
            print("2. Fill Profit with mean")
            print("3. Drop rows with missing values")

            choice = input("Enter your choice: ")

            if choice == "1":

                mean_sales = self.data["Sales"].mean()

                self.data["Sales"] = self.data[
                    "Sales"
                ].fillna(mean_sales)

                print("Sales missing values filled.")

            elif choice == "2":

                # One line
                self.data["Profit"] = self.data["Profit"].fillna(self.data["Profit"].mean())

                print("Profit missing values filled.")

            elif choice == "3":

                self.data.dropna(inplace=True)

                print("Missing rows removed.")

            else:

                print("Invalid choice.")

    # -----------------------------------------
    # NumPy Operations
    # -----------------------------------------
    def numpy_operations(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== NUMPY OPERATIONS ==========")

        # Convert Sales column into NumPy array
        sales_array = self.data["Sales"].to_numpy()

        print("\nSales Array:")
        print(sales_array)

        # Indexing
        print("\nFirst sales value:")

        print(sales_array[0])

        # Slicing
        print("\nFirst 5 sales values:")

        print(sales_array[:5])

        # Mathematical operation
        print("\nSales + 1000:")

        print(sales_array + 1000)

        # Multiplication
        print("\nSales * 2:")

        print(sales_array * 2)

        # Maximum
        print("\nHighest Sales:")

        print(np.max(sales_array))

        # Minimum
        print("\nLowest Sales:")

        print(np.min(sales_array))

    # -----------------------------------------
    # Mathematical Operations
    # -----------------------------------------
    def mathematical_operations(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== MATHEMATICAL OPERATIONS ==========")

        # Increase sales by 10%
        self.data["Sales_After_10_Percent"] = (
            self.data["Sales"] * 1.10
        )

        # Calculate profit percentage
        self.data["Profit_Percent"] = (
            self.data["Profit"] /
            self.data["Sales"]
        ) * 100

        print(
            self.data[
                [
                    "Sales",
                    "Profit",
                    "Sales_After_10_Percent",
                    "Profit_Percent"
                ]
            ].head()
        )

    # -----------------------------------------
    # Search, Sort and Filter
    # -----------------------------------------
    def search_sort_filter(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        while True:

            print("\n========== SEARCH / SORT / FILTER ==========")

            print("1. Search Product")
            print("2. Search Sales")
            print("3. Sort by Sales")
            print("4. Sort by Profit")
            print("5. Filter by Region")
            print("6. Filter Sales greater than 50000")
            print("7. Back")

            choice = input("Enter your choice: ")

            # Search product
            if choice == "1":

                product = input(
                    "Enter product name: "
                )

                result = self.data[
                    self.data["Product"].str.lower()
                    == product.lower()
                ]

                print(result)

            # Search sales
            elif choice == "2":

                sales = float(
                    input("Enter sales amount: ")
                )

                result = self.data[
                    self.data["Sales"] == sales
                ]

                print(result)

            # Sort sales
            elif choice == "3":

                result = self.data.sort_values(
                    by="Sales",
                    ascending=False
                )

                print(result)

            # Sort profit
            elif choice == "4":

                result = self.data.sort_values(
                    by="Profit",
                    ascending=False
                )

                print(result)

            # Filter region
            elif choice == "5":

                region = input(
                    "Enter region: "
                )

                result = self.data[
                    self.data["Region"].str.lower()
                    == region.lower()
                ]

                print(result)

            # Filter sales
            elif choice == "6":

                result = self.data[
                    self.data["Sales"] > 50000
                ]

                print(result)

            elif choice == "7":

                break

            else:

                print("Invalid choice.")

    # -----------------------------------------
    # Aggregate Functions
    # -----------------------------------------
    def aggregate_functions(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== AGGREGATE FUNCTIONS ==========")

        print(
            "Total Sales:",
            self.data["Sales"].sum()
        )

        print(
            "Average Sales:",
            self.data["Sales"].mean()
        )

        print(
            "Highest Sales:",
            self.data["Sales"].max()
        )

        print(
            "Lowest Sales:",
            self.data["Sales"].min()
        )

        print(
            "Total Profit:",
            self.data["Profit"].sum()
        )

        print(
            "Average Profit:",
            self.data["Profit"].mean()
        )

        print("\nSales by Product:")

        product_sales = self.data.groupby(
            "Product"
        )["Sales"].sum()

        print(product_sales)

        print("\nSales by Region:")

        region_sales = self.data.groupby(
            "Region"
        )["Sales"].sum()

        print(region_sales)

    # -----------------------------------------
    # Statistical Analysis
    # -----------------------------------------
    def statistical_analysis(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== STATISTICAL ANALYSIS ==========")

        print("\nDescriptive Statistics:")

        print(
            self.data[
                ["Sales", "Profit"]
            ].describe()
        )

        print("\nSales Standard Deviation:")

        print(
            self.data["Sales"].std()
        )

        print("\nSales Variance:")

        print(
            self.data["Sales"].var()
        )

        print("\nSales 50th Percentile:")

        print(
            self.data["Sales"].quantile(0.50)
        )

        print("\nSales 75th Percentile:")

        print(
            self.data["Sales"].quantile(0.75)
        )

    # -----------------------------------------
    # GroupBy + Transform
    # -----------------------------------------
    def groupby_transform(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== GROUPBY + TRANSFORM ==========")

        # Total sales for each product
        self.data["Product_Total_Sales"] = (
            self.data.groupby("Product")["Sales"]
            .transform("sum")
        )

        # Percentage of product sales
        self.data["Sales_Percentage"] = (
            self.data["Sales"] /
            self.data["Product_Total_Sales"]
        ) * 100

        print(
            self.data[
                [
                    "Product",
                    "Sales",
                    "Product_Total_Sales",
                    "Sales_Percentage"
                ]
            ]
        )

    # -----------------------------------------
    # Pivot Table
    # -----------------------------------------
    def create_pivot_table(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== PIVOT TABLE ==========")

        pivot = pd.pivot_table(
            self.data,
            index="Region",
            columns="Product",
            values="Sales",
            aggfunc="sum",
            fill_value=0
        )

        print(pivot)

    # -----------------------------------------
    # Combine using CONCAT
    # -----------------------------------------
    def combine_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== CONCAT DATA ==========")

        extra_data = pd.DataFrame({

            "Date": ["2026-03-01"],

            "Product": ["Laptop"],

            "Sales": [80000],

            "Region": ["North"],

            "Profit": [13000]

        })

        extra_data["Date"] = pd.to_datetime(
            extra_data["Date"]
        )

        self.data = pd.concat(
            [self.data, extra_data],
            ignore_index=True
        )

        print("\nData combined successfully.")

        print(self.data.tail())

    # -----------------------------------------
    # Merge DataFrames
    # -----------------------------------------
    def merge_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== MERGE DATA ==========")

        region_data = pd.DataFrame({

            "Region": [
                "North",
                "South",
                "East",
                "West"
            ],

            "Manager": [
                "Rahul",
                "Amit",
                "Priya",
                "Neha"
            ]

        })

        merged_data = pd.merge(
            self.data,
            region_data,
            on="Region",
            how="left"
        )

        print(merged_data.head())

    # -----------------------------------------
    # Join DataFrames
    # -----------------------------------------
    def join_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== JOIN DATA ==========")

        region_info = pd.DataFrame({

            "Region": [
                "North",
                "South",
                "East",
                "West"
            ],

            "Target": [
                300000,
                250000,
                280000,
                300000
            ]

        })

        region_info.set_index(
            "Region",
            inplace=True
        )

        sample_data = self.data.set_index(
            "Region"
        )

        joined_data = sample_data.join(
            region_info,
            how="left"
        )

        print(joined_data.head())

    # -----------------------------------------
    # Split Data
    # -----------------------------------------
    def split_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        print("\n========== SPLIT DATA ==========")

        north_data = self.data[
            self.data["Region"] == "North"
        ]

        south_data = self.data[
            self.data["Region"] == "South"
        ]

        east_data = self.data[
            self.data["Region"] == "East"
        ]

        west_data = self.data[
            self.data["Region"] == "West"
        ]

        print("\nNorth Data:")
        print(north_data)

        print("\nSouth Data:")
        print(south_data)

        print("\nEast Data:")
        print(east_data)

        print("\nWest Data:")
        print(west_data)

    # -----------------------------------------
    # Visualization
    # -----------------------------------------
    def visualize_data(self):

        if self.data.empty:

            print("\nPlease load the dataset first.")
            return

        while True:

            print("\n========== DATA VISUALIZATION ==========")

            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Box Plot")
            print("8. Heatmap")
            print("9. Subplots")
            print("10. Back")

            choice = input("Enter your choice: ")

            # --------------------------------
            # BAR PLOT
            # --------------------------------
            if choice == "1":

                product_sales = self.data.groupby(
                    "Product"
                )["Sales"].sum()

                plt.figure(figsize=(8, 5))

                plt.bar(
                    product_sales.index,
                    product_sales.values
                )

                plt.title("Sales by Product")

                plt.xlabel("Product")

                plt.ylabel("Sales")

                plt.xticks(rotation=45)

                plt.tight_layout()

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # LINE PLOT
            # --------------------------------
            elif choice == "2":

                daily_sales = self.data.groupby(
                    "Date"
                )["Sales"].sum()

                plt.figure(figsize=(10, 5))

                plt.plot(
                    daily_sales.index,
                    daily_sales.values,
                    marker="o"
                )

                plt.title("Sales Trend")

                plt.xlabel("Date")

                plt.ylabel("Sales")

                plt.xticks(rotation=45)

                plt.tight_layout()

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # SCATTER PLOT
            # --------------------------------
            elif choice == "3":

                plt.figure(figsize=(8, 5))

                plt.scatter(
                    self.data["Sales"],
                    self.data["Profit"]
                )

                plt.title(
                    "Sales vs Profit"
                )

                plt.xlabel("Sales")

                plt.ylabel("Profit")

                plt.tight_layout()

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # PIE CHART
            # --------------------------------
            elif choice == "4":

                region_sales = self.data.groupby(
                    "Region"
                )["Sales"].sum()

                plt.figure(figsize=(7, 7))

                plt.pie(
                    region_sales.values,
                    labels=region_sales.index,
                    autopct="%1.1f%%"
                )

                plt.title(
                    "Sales by Region"
                )

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # HISTOGRAM
            # --------------------------------
            elif choice == "5":

                plt.figure(figsize=(8, 5))

                plt.hist(
                    self.data["Sales"],
                    bins=5
                )

                plt.title(
                    "Sales Distribution"
                )

                plt.xlabel("Sales")

                plt.ylabel("Frequency")

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # STACK PLOT
            # --------------------------------
            elif choice == "6":

                product_data = self.data.groupby(
                    ["Date", "Product"]
                )["Sales"].sum().unstack(
                    fill_value=0
                )

                plt.figure(figsize=(10, 5))

                plt.stackplot(
                    product_data.index,
                    product_data.T,
                    labels=product_data.columns
                )

                plt.title(
                    "Product Sales Stack Plot"
                )

                plt.xlabel("Date")

                plt.ylabel("Sales")

                plt.legend()

                plt.xticks(rotation=45)

                plt.tight_layout()

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # BOX PLOT
            # --------------------------------
            elif choice == "7":

                plt.figure(figsize=(8, 5))

                sns.boxplot(
                    x=self.data["Sales"]
                )

                plt.title(
                    "Sales Box Plot"
                )

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # HEATMAP
            # --------------------------------
            elif choice == "8":

                numeric_data = self.data[
                    ["Sales", "Profit"]
                ]

                correlation = numeric_data.corr()

                plt.figure(figsize=(6, 5))

                sns.heatmap(
                    correlation,
                    annot=True
                )

                plt.title(
                    "Sales and Profit Correlation"
                )

                self.last_plot = plt.gcf()

                plt.show()

            # --------------------------------
            # SUBPLOTS
            # --------------------------------
            elif choice == "9":

                fig, axes = plt.subplots(
                    1,
                    2,
                    figsize=(12, 5)
                )

                product_sales = self.data.groupby(
                    "Product"
                )["Sales"].sum()

                axes[0].bar(
                    product_sales.index,
                    product_sales.values
                )

                axes[0].set_title(
                    "Sales by Product"
                )

                axes[0].tick_params(
                    axis="x",
                    rotation=45
                )

                axes[1].scatter(
                    self.data["Sales"],
                    self.data["Profit"]
                )

                axes[1].set_title(
                    "Sales vs Profit"
                )

                axes[1].set_xlabel(
                    "Sales"
                )

                axes[1].set_ylabel(
                    "Profit"
                )

                plt.tight_layout()

                self.last_plot = fig

                plt.show()

            elif choice == "10":

                break

            else:

                print("Invalid choice.")

    # -----------------------------------------
    # Save Visualization
    # -----------------------------------------
    def save_visualization(self):

        if self.last_plot is None:

            print(
                "\nPlease create a graph first."
            )

            return

        file_name = input(
            "Enter file name (example: sales_chart.png): "
        )

        self.last_plot.savefig(
            file_name,
            bbox_inches="tight"
        )

        print(
            "\nVisualization saved successfully!"
        )

    # -----------------------------------------
    # Destructor
    # -----------------------------------------
    def __del__(self):

        print(
            "\nSalesDataAnalyzer object closed."
        )


# =================================================
# MAIN PROGRAM
# =================================================

analyzer = SalesDataAnalyzer()


while True:

    print("\n")
    print("=" * 50)
    print("        SALES DATA ANALYZER")
    print("=" * 50)

    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. NumPy Operations")
    print("4. Mathematical Operations")
    print("5. Search, Sort and Filter")
    print("6. Aggregate Functions")
    print("7. Statistical Analysis")
    print("8. GroupBy and Transform")
    print("9. Pivot Table")
    print("10. Combine Data using Concat")
    print("11. Merge Data")
    print("12. Join Data")
    print("13. Split Data")
    print("14. Handle Missing Data")
    print("15. Data Visualization")
    print("16. Save Visualization")
    print("17. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        file_path = input(
            "Enter CSV file path: "
        )

        analyzer.load_data(file_path)

    elif choice == "2":

        analyzer.explore_data()

    elif choice == "3":

        analyzer.numpy_operations()

    elif choice == "4":

        analyzer.mathematical_operations()

    elif choice == "5":

        analyzer.search_sort_filter()

    elif choice == "6":

        analyzer.aggregate_functions()

    elif choice == "7":

        analyzer.statistical_analysis()

    elif choice == "8":

        analyzer.groupby_transform()

    elif choice == "9":

        analyzer.create_pivot_table()

    elif choice == "10":

        analyzer.combine_data()

    elif choice == "11":

        analyzer.merge_data()

    elif choice == "12":

        analyzer.join_data()

    elif choice == "13":

        analyzer.split_data()

    elif choice == "14":

        analyzer.clean_data()

    elif choice == "15":

        analyzer.visualize_data()

    elif choice == "16":

        analyzer.save_visualization()

    elif choice == "17":

        print(
            "\nExiting the program. Goodbye!"
        )

        break

    else:

        print(
            "\nInvalid choice. Please try again."
        )