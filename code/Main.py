import pandas as pd
import numpy as np


def get_data(url):
    # Since pandas dataframe interpreted some
    # attributes as of object types we will convert
    # these types (especially datetime types)
    parse_date_att = ["pickup_datetime", "dropoff_datetime"]

    train_data = pd.read_csv(url, parse_dates=parse_date_att)

    # mapping True and False to store_and_fwd_flag attribute
    dummy = pd.get_dummies(train_data['store_and_fwd_flag'])
    # add additional dummy variable
    train_taxi_2 = pd.concat((train_data, dummy), axis=1)
    # delete stor_and_fwd_flag attribute
    train_taxi_2 = train_taxi_2.drop(['store_and_fwd_flag'], axis=1)

    train_taxi_2 = train_taxi_2.drop(['N'], axis=1)
    train_taxi_2 = train_taxi_2.rename(columns={"Y": "store_and_fwd_flag"})
    train_data = train_taxi_2
    train_data = train_data[train_data.trip_duration < train_data.trip_duration.quantile(0.99)]
    return train_data


def get_test_data(url):

    # Since pandas dataframe interpreted some
    # attributes as of object types we will convert
    # these types (especially datetime types)
    parse_date_att = ["pickup_datetime"]

    test_data = pd.read_csv(url, parse_dates=parse_date_att)
    # mapping True and False to store_and_fwd_flag attribute
    dummy = pd.get_dummies(test_data['store_and_fwd_flag'])
    # add additional dummy variable
    test_taxi_2 = pd.concat((test_data, dummy), axis=1)
    # delete stor_and_fwd_flag attribute
    test_taxi_2 = test_taxi_2.drop(['store_and_fwd_flag'], axis=1)

    test_taxi_2 = test_taxi_2.drop(['N'], axis=1)
    test_taxi_2 = test_taxi_2.rename(columns={"Y": "store_and_fwd_flag"})
    test_data = test_taxi_2
    return test_data
