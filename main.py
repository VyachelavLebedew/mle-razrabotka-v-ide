import pandas as pd
from src.reporter import DataFrameReporter


def main():
    data = pd.read_csv('data/payments.csv')
    df = pd.DataFrame(data)
    obj = DataFrameReporter()
    return obj.show_report(df)

if __name__ == '__main__':
    main()
