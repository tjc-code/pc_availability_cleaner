import pandas as pd
import argparse


def clean_dataframe(df: pd.DataFrame, file_name):
    # filter out "?" availabilities
    filtered_df = df[
        ~(
            df.iloc[:, 1:]
            .astype(str)
            .apply(lambda x: x.str.contains(r"\?", regex=True))
            .all(axis=1)
        )
    ].rename(columns={"Unnamed: 0": "name"})

    return filtered_df


if __name__ == "__main__":

    # parse command line argument of the file name
    parser = argparse.ArgumentParser()
    file_name = "file_name"
    parser.add_argument(file_name, help="The file you want to clean without extension")
    args = parser.parse_args()
    config = vars(args)

    df = pd.read_excel(f"{config[file_name]}.xlsx")
    filtered_df = clean_dataframe(df, config[file_name])
    filtered_df.to_excel(f"cleaner_{file_name}", index=False)
