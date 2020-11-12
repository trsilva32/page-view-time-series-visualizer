import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=[0], index_col=[0])

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) &  (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig , ax = plt.subplots(figsize=(15,5))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date") ;plt.ylabel("Page Views")
    plt.plot(df.index, df.value, color = 'r')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year ; df_bar["month_nbr"] = df_bar.index.month ; df_bar["month"] = df_bar.index.month_name()
    df_bar = df_bar.groupby(["year","month_nbr","month"]).mean()
    df_bar = df_bar.sort_values(by='month_nbr')
    df_bar = df_bar.reset_index()

    # Draw bar plot
    fig = plt.subplots(figsize = (12,12))
    fig = sns.barplot(x= 'year', y='value', hue='month', data=df_bar)
    fig.set(xlabel = 'Years', ylabel = 'Average Page Views')
    fig = fig.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_nbr'] = [d.strftime('%m') for d in df_box.date]
    df_box = df_box.sort_values(by='month_nbr')

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(10) 

    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    ax1 = sns.boxplot(x=df_box.year, y=df_box.value, ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    ax2 = sns.boxplot(x=df_box.month, y=df_box.value, ax=ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
