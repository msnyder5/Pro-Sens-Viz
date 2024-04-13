### Pro Settings Analysis Tool

#### Description
This Python script is designed to extract and analyze the mouse sensitivity settings (DPI and sensitivity) of professional eSports players. It retrieves data from a specified URL that lists these settings, then visualizes the data to provide insights into common sensitivity configurations among the pros. The visualizations include a scatter plot of DPI versus sensitivity and a histogram of the effective DPI (eDPI), calculated as the product of DPI and sensitivity.

#### Requirements
- Python 3.x
- Libraries:
  - `pandas`: For data manipulation and analysis.
  - `matplotlib`: For creating visualizations.
  - `seaborn`: For enhanced visualization styles.
  - `requests`: For making HTTP requests to retrieve web data.
  - `beautifulsoup4`: For parsing HTML and XML documents.

To install the necessary libraries, you can use the following pip command:
```
pip install pandas matplotlib seaborn requests beautifulsoup4
```

#### Usage
To use this script, simply run it in a Python environment. Ensure you have internet connectivity as the script needs to fetch data from the web.

1. Clone the repository or download the script to your local machine.
2. Navigate to the script's directory in your terminal or command prompt.
3. Execute the script by running:
   ```
   python script_name.py
   ```

#### Script Functions
- `get_table()`: Fetches and parses the HTML table from the Apex Legends pro settings webpage. It returns a DataFrame with the retrieved data or `None` if the data retrieval fails.
- `visualize(df)`: Takes a DataFrame as input and generates two visualizations:
  - **Scatterplot of DPI vs Sens**: Plots each player's DPI against their sensitivity setting.
  - **Apex Pro eDPI Distribution**: Displays a histogram of eDPI values among the players, with an overlay of the kernel density estimate.
- `main()`: The main function that orchestrates the fetching and visualization process.

#### Expected Output
The script will display two plots:
1. A scatter plot showing the relationship between DPI and sensitivity settings of professional Apex Legends players.
2. A histogram showing the distribution of eDPI values, which helps to understand the common effective sensitivity settings used by the pros.

#### Note
The script depends on the structure of the webpage from which it retrieves data. Any changes to the HTML structure of the target URL may require updates to the parsing logic in the `get_table()` function.