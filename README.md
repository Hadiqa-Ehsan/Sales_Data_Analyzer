
# 📊 Sales Data Analyzer

A Python tool to analyze sales data, track revenue trends, and generate actionable business insights.

## ✨ Features

- **Sales Data Input** – Add product names, quantities, prices, and dates
- **Revenue Calculation** – Calculate total and daily revenue automatically
- **Best Selling Products** – Identify top-performing products
- **Sales Trends** – Track daily, weekly, and monthly sales patterns
- **Peak Days Analysis** – Find highest and lowest sales days
- **Average Order Value** – Calculate average transaction amount
- **CSV Export** – Save reports for further analysis

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization and charts
- **CSV Module** – Data storage
- **Datetime Module** – Date-based analysis

## 📁 Project Structure

```
Sales_Data_Analyzer/
├── sales_analyzer.py    # Main program
├── sales_data.csv       # Stored sales records
├── sales_report.csv     # Generated reports
├── sales_chart.png      # Visualization output
└── README.md            # Documentation
```

## 🔧 How to Run

1. Download or clone the project
2. Open terminal in the project folder
3. Install dependencies:

```bash
pip install pandas matplotlib
```

4. Run the program:

```bash
python sales_analyzer.py
```

## 📖 Usage Example

```
--- Sales Data Analyzer ---

1. Add Sale Record
2. View Total Revenue
3. Best Selling Products
4. Daily Sales Report
5. Generate Sales Chart
6. Exit

Enter your choice: 1
Enter product name: Laptop
Enter quantity sold: 5
Enter price per unit: $800
Enter date (YYYY-MM-DD): 2026-05-10

Sale recorded! Revenue: $4000

Enter choice: 2
--- Total Revenue Report ---
Total Revenue: $15,750
Total Units Sold: 42
Average Order Value: $375

Enter choice: 3
--- Best Selling Products ---
1. Laptop - $12,000 (15 units)
2. Mouse - $2,250 (45 units)
3. Keyboard - $1,500 (30 units)
```

## 📈 Sample Visualizations

- **Bar Chart** – Sales by product
- **Line Graph** – Daily revenue trends
- **Pie Chart** – Revenue contribution by product

## 📌 Future Improvements

- Predict future sales using basic forecasting
- Add profit margin calculations
- Customer purchase history tracking
- Inventory alert system
- Web dashboard with Flask

## 👩‍💻 Author

**Hadiqa Ehsan**  
[GitHub Profile](https://github.com/Hadiqa-Ehsan)

## 📄 License

MIT License

---

⭐ Star this repo if you found it useful for business analytics!
