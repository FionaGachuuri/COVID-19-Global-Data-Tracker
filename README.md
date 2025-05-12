# COVID-19 Global Data Tracker

## Project Description
This repository contains a comprehensive data analysis project that tracks and visualizes global COVID-19 trends. The project analyzes cases, deaths, recoveries, and vaccinations across countries and over time, using Python data analysis tools to generate insights and visualizations.

## Project Objectives
- Import and clean COVID-19 global data from reliable sources
- Analyze time trends for cases, deaths, and vaccinations
- Compare metrics across countries and regions
- Visualize global trends with charts and maps
- Communicate findings in a comprehensive notebook report

## Data Source
The primary data source for this project is the [Our World in Data COVID-19 Dataset](https://github.com/owid/covid-19-data/tree/master/public/data), which provides a comprehensive and regularly updated dataset on COVID-19 cases, deaths, and vaccinations.

## Tools and Libraries Used
- Python 3.8+
- pandas: Data manipulation and analysis
- matplotlib & seaborn: Static data visualization
- plotly: Interactive visualization and mapping
- numpy: Numerical operations


## How to Run the Project

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/covid-19-tracker.git
   cd covid-19-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the COVID-19 dataset:
   ```
   mkdir -p data
   cd data
   wget https://covid.ourworldindata.org/data/owid-covid-data.csv
   cd ..
   ```

4. Open and run the Jupyter Notebook:
   ```
   jupyter notebook covid_data_tracker.ipynb
   ```

5. Follow the cells in the notebook to run the analysis step by step.

## Key Features
- Comprehensive data cleaning and preparation
- Time series analysis of COVID-19 cases and deaths
- Vaccination progress tracking and comparison
- Interactive choropleth maps
- Statistical insights and correlation analysis
- Detailed visualization with proper annotations

## Key Insights
1. **Case Distribution**: Analysis of total cases across different countries and regions
2. **Mortality Analysis**: Death rates and total deaths comparison between countries
3. **Vaccination Progress**: Tracking vaccination rates and comparing rollout effectiveness
4. **Regional Patterns**: Identifying geographic patterns in COVID-19 spread
5. **Temporal Trends**: Observing waves and patterns in case numbers over time

## Future Improvements
- Add forecasting models to predict future trends
- Include more granular regional data (states/provinces)
- Add economic impact analysis
- Expand vaccination effectiveness analysis

## Author
Fiona Gachuuri

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Our World in Data for providing the comprehensive COVID-19 dataset
- The global scientific community for their tireless work during the pandemic
