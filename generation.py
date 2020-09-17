import pandas as pd
import numpy as np
from numpy import random
from toolz import pipe, partial
import random


def generate():
    df = pd.date_range(
        start="2020-01-01",
        end="2020-11-01",
        tz="America/Argentina/Buenos_Aires",
        freq="T",
    )
    df = pd.DataFrame(0, index=df, columns=["value"])
    df = df.loc[(df.index.hour >= 9) & (df.index.hour <= 19), :]
    df = df.loc[~(df.index.day_name().isin(["Saturday", "Sunday"])), :]
    df = df.groupby([df.index.month, df.index.day]).apply(
        lambda df: df.sample(300).sort_index()
    )
    df.index = df.index.droplevel([0, 1])
    # todo : use pipe
    df = df.groupby([df.index.month, df.index.day]).transform(
        lambda df: pd.Series(
            pipe(
                generate_fake_day(150),
                np.array,
                # todo: agregar errores
                # lambda a: np.concatenate((a, np.zeros(20))),
                # np.random.permutation,
            )
        )
    )
    df.index = df.index.tz_convert("utc")
    return df


def generate_fake_day(people_number=10):
    result = np.zeros(2 * people_number)
    ya_entraron = 0
    for i in range(2 * people_number):
        parcial = np.sum(result)
        assert parcial >= 0
        new_value = 0

        if parcial <= 0:  # Si ya salieron todos los que entraron
            result[i] = 1
            ya_entraron += 1
            continue

        if ya_entraron >= people_number:  # Si ya entraron todos los que queria
            result[i] = -1
            continue

        new_value = random.choice([-1, 1])
        if new_value == 1:
            ya_entraron += 1
        result[i] = new_value

    assert np.sum(result) == 0
    assert result[0] == 1
    assert result[(2 * people_number) - 1] == -1
    # print(result)
    return result
