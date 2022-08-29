import pandas as pd


class VisitorsAnalyticsUtils:
    # Load data from csv file
    def loadDataFile(self, fileName):
        # load data from csv file
        df = pd.read_csv(fileName, na_values=" na ")
        # fill missing values with 0
        df = df.fillna(0)
        # print first 5 rows of dataframe
        print("\n*** First 5 rows of data loaded ***")
        print(df.head())
        return df

    # Parse data
    def parseData(self, df, period, region):
        # parse data based on region from user input
        if region == 0:
            df = df[
                [
                    "   ",  # date
                    " Brunei Darussalam ",
                    " Indonesia ",
                    " Malaysia ",
                    " Philippines ",
                    " Thailand ",
                    " Viet Nam ",
                    " Myanmar ",
                    " Japan ",
                    " Hong Kong ",
                    " China ",
                    " Taiwan ",
                    " Korea, Republic Of ",
                    " India ",
                    " Pakistan ",
                    " Sri Lanka ",
                    " Saudi Arabia ",
                    " Kuwait ",
                    " UAE ",
                ]
            ]
        elif region == 1:
            df = df[
                [
                    "   ",  # date
                    " United Kingdom ",
                    " Germany ",
                    " France ",
                    " Italy ",
                    " Netherlands ",
                    " Greece ",
                    " Belgium & Luxembourg ",
                    " Switzerland ",
                    " Austria ",
                    " Scandinavia ",
                    " CIS & Eastern Europe ",
                ]
            ]
        elif region == 2:
            df = df[
                [
                    "   ",  # date
                    " USA ",
                    " Canada ",
                    " Australia ",
                    " New Zealand ",
                    " Africa ",
                ]
            ]
        # parse date from dataframe
        times = df.iloc[:, 0].to_list()
        formatted_times = [time.split(" ")[1] for time in times]
        selected = []
        # loop through year column and filter out the data based on period
        for index, time in enumerate(formatted_times):
            if period == 0:
                if int(time) >= 1978 and int(time) <= 1987:
                    selected.append(index)
            if period == 1:
                if int(time) >= 1988 and int(time) <= 1997:
                    selected.append(index)
            if period == 2:
                if int(time) >= 1998 and int(time) <= 2007:
                    selected.append(index)
            if period == 3:
                if int(time) >= 2008 and int(time) <= 2017:
                    selected.append(index)
        # select data based on selected index
        df = df.filter(items=selected, axis=0)
        # get year from selected indexes
        selected_times = [int(formatted_times[selector]) for selector in selected]
        # replace first column with selected times
        df.iloc[:, 0] = selected_times
        # replace "   " with "year" for readability
        df.rename(columns={"   ": "year"}, inplace=True)
        print("\n*** Parsed Data (Regions)***")
        print(df.info())
        print("\n*** Parsed Data (Years)***")
        print(df.year.describe())
        return df

    def getTop3Countries(self, df):
        print("\n*** Top 3 Countries ***")
        # remove first column
        df = df.iloc[:, 1:]
        # remove comma from all values in the dataframe and convert to int
        df = df.replace(",", "", regex=True)
        # make sure values are numeric
        df = df.apply(pd.to_numeric)
        # get sum of each column and sort in descending order
        df = df.sum(axis=0).sort_values(ascending=False)
        # print top 3 countries
        print(df.head(3))


if __name__ == "__main__":
    time_period = ["1978-1987", "1988-1997", "1998-2007", "2008-2017"]
    region = ["asia", "europe", "others"]

    # prompt user to enter time period and region
    print("Enter time period (0: 1978-1987, 1: 1988-1997, 2: 1998-2007, 3: 2008-2017):")
    time_period_index = int(input())
    print("Enter region (0: asia, 1: europe, 2: others):")
    region_index = int(input())

    worker = VisitorsAnalyticsUtils()
    df = worker.loadDataFile("./Int_Monthly_Visitor.csv")
    df = worker.parseData(df, time_period_index, region_index)
    worker.getTop3Countries(df)
    # print(df.columns)
