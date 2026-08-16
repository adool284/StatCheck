from project import calculate_central_tendency, calculate_dispersion, calculate_advanced_stats

def test_calculate_central_tendency():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    res = calculate_central_tendency(data)
    assert res["Mean"] == 5.0
    assert res["Median"] == 4.5
    assert res["Mode"] == 4

def test_calculate_dispersion():
    data = [10, 20, 30, 40, 50]
    res = calculate_dispersion(data)
    assert res["Range"] == 40
    assert res["Variance"] == 250
    assert res["IQR (Interquartile Range)"] == 30.0

def test_calculate_advanced_stats():
    data = [10, 20, 30, 40, 50]
    res = calculate_advanced_stats(data)
    assert res["Sample Size (n)"] == 5
    assert res["Standard Error (SEM)"] > 0
