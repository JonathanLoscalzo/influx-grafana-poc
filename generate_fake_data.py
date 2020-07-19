
times = pd.date_range(start='2020-01-01', end='2020-08-01', tz='utc', freq='min')
values = np.random.choice([-1,0-0],times.shape[0])