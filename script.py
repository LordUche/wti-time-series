import pandas as pd
from datetime import datetime as dt, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

url = 'wti-prices.csv'
date_parser = lambda x: dt.strptime(x, '%m/%d/%Y')

# Load data
df = pd.read_csv(url, parse_dates=['Day'], date_parser=date_parser, index_col='Day')

# Add missing dates
idx = pd.date_range(df.index.min(), df.index.max(), freq='D')
df = df.reindex(idx)

# Use previous prices for missing values
df = df.interpolate(method='pad', limit=df.size)

# plt.style.use('seaborn')
# plt.xkcd()

plt.plot_date(df.index, df.Price, linestyle='solid', marker='')

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.xlabel('Dates')
plt.ylabel('Prices')
plt.title('WTI Crude Oil Prices')

plt.tight_layout()
plt.savefig('price_plot.svg')
plt.show()

df_diff = df.diff(periods=1)[1:]

plt.plot_date(df_diff.index, df_diff.Price, linestyle='solid', linewidth=1, marker='')

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.xlabel('Dates')
plt.ylabel('Prices')
plt.title('WTI Crude Oil Prices with Differencing')

plt.tight_layout()
plt.savefig('price_diff_plot.svg')
plt.show()
