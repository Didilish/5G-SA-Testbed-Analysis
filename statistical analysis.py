import numpy as np
import scipy.stats as stats

# Extracting the data from the provided snippet
# Creating sample data based on the output snippet, assuming the file has columns named 'Throughput', 'UL Packet Loss', and 'DL Packet Loss'.
data = {
    "Throughput": [0.40947656, 0.02176563, 2.41957813, 3.01292969, 4.90798438, 5.68970313, 6.28964063, 6.74172656,
                   12.13892188, 15.053625, 39.57166406, 74.17078906, 101.2719375, 104.108375, 105.39455469, 107.0824375,
                   108.31421094, 109.50545313, 109.89139063, 111.40628906],
    "UL Packet Loss": [0.0, 0.0, 0.0, 0.00080192, 0.00059952, 0.00048309, 0.00038139, 0.00095481, 0.00082873, 0.00074221,
                       0.00066667, 0.00060618, 0.00055597, 0.00051238, 0.00047962, 0.00044951, 0.00042129, 0.00038745,
                       0.00035834, 0.00033003],
    "DL Packet Loss": [0.0, 0.0, 0.0, 0.00408163, 0.00286533, 0.00249377, 0.0021978, 0.00194553, 0.00135135, 0.00112994,
                       0.0007722, 0.00058343, 0.00046168, 0.00042845, 0.00041391, 0.00039841, 0.0003858, 0.00037272,
                       0.00036563, 0.00035211]
}

# Creating a DataFrame from the sample data
df = pd.DataFrame(data)

# Function to calculate 95% confidence interval
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    margin_of_error = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
    return mean, mean - margin_of_error, mean + margin_of_error

# Calculating mean, variance, and confidence interval for each metric
metrics = {}
for column in df.columns:
    mean = df[column].mean()
    variance = df[column].var()
    mean, ci_lower, ci_upper = confidence_interval(df[column])
    metrics[column] = {
        "Mean": mean,
        "Variance": variance,
        "95% Confidence Interval": (ci_lower, ci_upper)
    }

# Creating Table 1: Statistical Analysis of Testbed Performance Metrics
table_data = {
    "Metric": [],
    "Mean Value": [],
    "Variance": [],
    "95% Confidence Interval": []
}

for metric, values in metrics.items():
    table_data["Metric"].append(metric)
    table_data["Mean Value"].append(values["Mean"])
    table_data["Variance"].append(values["Variance"])
    table_data["95% Confidence Interval"].append(f"[{values['95% Confidence Interval'][0]}, {values['95% Confidence Interval'][1]}]")

# Creating a DataFrame for the table
table_df = pd.DataFrame(table_data)
import ace_tools as tools; tools.display_dataframe_to_user(name="Table 1: Statistical Analysis of Testbed Performance Metrics", dataframe=table_df)
