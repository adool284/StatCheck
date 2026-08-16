import math
import statistics
from tabulate import tabulate

def main():
    print("=== StatCheck Pro: Advanced Statistical Verifier ===")
    user_input = input("Enter your dataset (numbers separated by spaces): ")

    try:
        # Convert input string into a list of floats
        data = [float(x) for x in user_input.split()]
        if len(data) < 3:
            print("Error: For advanced metrics (Skewness/Confidence), please enter at least 3 numbers.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    # Call the 4 core functions
    central = calculate_central_tendency(data)
    dispersion = calculate_dispersion(data)
    advanced = calculate_advanced_stats(data)

    # Merge all results and format the output
    final_report = {**central, **dispersion, **advanced}
    print("\n" + format_summary(final_report))


def calculate_central_tendency(data):
    """1. Computes measures of central tendency and distribution shape."""
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)

    try:
        mode_val = statistics.mode(data)
    except statistics.StatisticsError:
        mode_val = "No unique mode"

    # Calculate Skewness manually to determine distribution asymmetry
    n = len(data)
    std_dev = statistics.stdev(data) if n > 1 else 1
    if std_dev != 0:
        skewness = (sum((x - mean_val) ** 3 for x in data) / n) / (std_dev ** 3)
    else:
        skewness = 0.0

    return {
        "Mean": round(mean_val, 4),
        "Median": round(median_val, 4),
        "Mode": mode_val,
        "Skewness": round(skewness, 4)
    }


def calculate_dispersion(data):
    """2. Computes measures of dispersion and advanced quartiles."""
    n = len(data)
    num_range = max(data) - min(data)
    variance_val = statistics.variance(data) if n > 1 else 0.0
    stdev_val = statistics.stdev(data) if n > 1 else 0.0

    # Calculate Quartiles and Interquartile Range (IQR)
    sorted_data = sorted(data)
    q1 = statistics.median(sorted_data[:n//2])
    if n % 2 != 0:
        q3 = statistics.median(sorted_data[(n+1)//2:])
    else:
        q3 = statistics.median(sorted_data[n//2:])
    iqr = q3 - q1

    return {
        "Range": round(num_range, 4),
        "Variance": round(variance_val, 4),
        "Std Deviation": round(stdev_val, 4),
        "Q1 (First Quartile)": round(q1, 4),
        "Q3 (Third Quartile)": round(q3, 4),
        "IQR (Interquartile Range)": round(iqr, 4)
    }


def calculate_advanced_stats(data):
    """3. Computes inferential statistics, confidence intervals, and standard error."""
    n = len(data)
    mean_val = statistics.mean(data)
    stdev_val = statistics.stdev(data)

    # Standard Error of the Mean (SEM)
    sem = stdev_val / math.sqrt(n) if n > 0 else 0

    # 95% Confidence Interval (CI) using Z-score approximation (Z = 1.96)
    margin_of_error = 1.96 * sem
    ci_lower = mean_val - margin_of_error
    ci_upper = mean_val + margin_of_error

    return {
        "Standard Error (SEM)": round(sem, 4),
        "95% CI Lower Bound": round(ci_lower, 4),
        "95% CI Upper Bound": round(ci_upper, 4),
        "Sample Size (n)": n
    }


def format_summary(results):
    """4. Formats and displays the final statistical report in a professional grid table."""
    table_data = [[metric, value] for metric, value in results.items()]
    return tabulate(table_data, headers=["Statistical Metric", "Value"], tablefmt="fancy_grid")


if __name__ == "__main__":
    main()
