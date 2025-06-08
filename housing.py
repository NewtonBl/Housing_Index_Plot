import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def state():
    link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_state.xls"
    raw_df = pd.read_excel(link)
    df = raw_df.query('state == "MI"')
    df = df.iloc[:, [1, 2, 3, 4]]

    sns.relplot(raw_df, x="yr", y="index_sa", hue="qtr", palette="muted")
    plt.title("Michigan House Price Index - Seasonally Adjusted")
    plt.show()


def Both():
    US_link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_us_and_census.xls"
    US_raw_df = pd.read_excel(US_link)
    US_df = US_raw_df.query('division == "USA"')
    US_df = US_df.iloc[:, [1, 2, 3, 4]]
    US_df["period"] = pd.PeriodIndex(year=US_df["year"], quarter=US_df["qtr"], freq="Q").astype(str)


    State_link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_state.xls"
    State_raw_df = pd.read_excel(State_link)
    State_df = State_raw_df.query('state == "MI"')
    State_df = State_df.iloc[:, [1, 2, 3, 4]]
    State_df["period"] = pd.PeriodIndex(year=State_df["yr"], quarter=State_df["qtr"], freq="Q").astype(str)


    fig, ax = plt.subplots(1, 2, figsize=(16, 6), layout='constrained')
    ax[0].set_title("US House Price Index - Seasonally Adjusted")
    ax[0].plot(US_df["period"], US_df["index_po_seasonally_adjusted"], marker="x", markersize=3, markeredgecolor="black")
    ax[0].set_xticks(US_df["period"][::4])  # Show every 4th tick
    ax[0].set_xticklabels(US_df["period"][::4], rotation=90)
    ax[0].set_xlabel("Period")
    ax[0].set_ylabel("House Price Index")


    ax[1].set_title("Michigan House Price Index - Seasonally Adjusted")
    ax[1].plot(State_df["period"], State_df["index_sa"], marker="x", markersize=3, markeredgecolor="black")
    ax[1].set_xticks(State_df["period"][::4])  # Show every 4th tick
    ax[1].set_xticklabels(State_df["period"][::4], rotation=90)
    ax[1].set_xlabel("Period")
    ax[1].set_ylabel("House Price Index")
    plt.show()


def Together_SA():
    US_link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_us_and_census.xls"
    US_raw_df = pd.read_excel(US_link)
    US_df = US_raw_df.query('division == "USA"')
    US_df = US_df.iloc[:, [1, 2, 3, 4]]
    US_df["period"] = pd.PeriodIndex(year=US_df["year"], quarter=US_df["qtr"], freq="Q").astype(str)


    State_link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_state.xls"
    State_raw_df = pd.read_excel(State_link)
    State_df = State_raw_df.query('state == "MI"')
    State_df = State_df.iloc[:, [1, 2, 3, 4]]
    State_df["period"] = pd.PeriodIndex(year=State_df["yr"], quarter=State_df["qtr"], freq="Q").astype(str)


    fig, ax = plt.subplots( figsize=(16, 6), layout='constrained')
    ax.set_title("US vs. MI Price Index - Seasonally Adjusted")
    ax.plot(US_df["period"], US_df["index_po_seasonally_adjusted"], marker="x", markersize=3, markeredgecolor="black")
    ax.plot(State_df["period"], State_df["index_sa"], marker="x", markersize=3, markeredgecolor="black", color="green")
    ax.set_xticks(US_df["period"][::4])  # Show every 4th tick
    ax.set_xticklabels(US_df["period"][::4], rotation=90)
    ax.set_xlabel("Period (Year and Quarter)")
    ax.set_ylabel("House Price Index")
    ax.legend(["US", "Michigan"])
    ax.grid(axis='x', linestyle='--')
    plt.figtext(0.5, 0.5, "Quarterly seasonally adjusted home sale price index from FHFA.gov", wrap=True, horizontalalignment='center', fontsize=12)
    plt.show()


def Together_NSA():
    US_link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_us_and_census.xls"
    US_raw_df = pd.read_excel(US_link)
    US_df = US_raw_df.query('division == "USA"')
    US_df = US_df.iloc[:, [1, 2, 3, 4]]
    US_df["period"] = pd.PeriodIndex(year=US_df["year"], quarter=US_df["qtr"], freq="Q").astype(str)


    State_link = "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_state.xls"
    State_raw_df = pd.read_excel(State_link)
    State_df = State_raw_df.query('state == "MI"')
    State_df = State_df.iloc[:, [1, 2, 3, 4]]
    State_df["period"] = pd.PeriodIndex(year=State_df["yr"], quarter=State_df["qtr"], freq="Q").astype(str)


    fig, ax = plt.subplots( figsize=(16, 6), layout='constrained')
    ax.set_title("US vs. MI Price Index - Not Seasonally Adjusted")
    ax.plot(US_df["period"], US_df["index_po_not_seasonally_adjusted"], marker="x", markersize=3, markeredgecolor="black")
    ax.plot(State_df["period"], State_df["index_nsa"], marker="x", markersize=3, markeredgecolor="black", color="green")
    ax.set_xticks(US_df["period"][::4])  # Show every 4th tick
    ax.set_xticklabels(US_df["period"][::4], rotation=90)
    ax.set_xlabel("Period")
    ax.set_ylabel("House Price Index")
    ax.legend(["US", "Michigan"])
    ax.grid(axis='x', linestyle='--')
    plt.show()


if __name__ == "__main__":
    Together_SA()