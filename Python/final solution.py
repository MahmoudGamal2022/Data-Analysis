# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 22:39:39 2021

@author: Mahmoud Batran
"""
import pandas as pd
import time
import datetime

""" create dictionary contain three keys for three cities 
    each key have value that is data set of city"""

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

# create al list that contain a three name of cities

cities_list = ["chicago", "new york", "washington"]


def get_city():
    """
    Asks user to specify a city to analyze.check if user input correct or not if not ask user to Try again and enter correct 
    input must be in  cities_list[]
    input accepts the string of "Chicago" and its case variants, such as "chicago", "CHICAGO", or "cHicAgo".
   Args:
       None.
   Returns:
       str (city): correct name of the city to filter.
   """

    #  Asks user to specify a city to analyze
    user_input_city = input("would you like to see data for Chicago, New York, Washington? \n").lower()
    # while to check if user input correct or not
    while user_input_city.lower() not in cities_list:
        user_input_city = input(
            "please, try again input correct choose city Chicago, New York, Washington? \n").lower()
    # str (city): correct name of the city to filter.
    return user_input_city


# create a dictionary of name months and key refer the number of months
# it contain all months but if month not have date the program print that is no data in this filter

month_dict = {"1": 'january', "2": 'february', "3": 'march',
              "4": 'april', "5": 'may', "6": 'june',
              "7": 'july', "8": 'august', "9": 'september',
              "10": 'october', "11": 'november', "12": 'december'
              }


def get_month():
    """
    Asks user to specify a month to filter.
    input should be in key or value of {month_dict}
    check if user input correct or not, 
    input accepts the string of "month" and its case variants, such as "January", "JANUARY", or "jAnUary". or all for all month
    input accepts the integer of month such as 1, 2, 3 for janaury, feb, march
   Args:
       None.
   Returns:
       str (month): correct name of the month to filter.
   """
    # Asks user to specify a month to filter.
    user_input_month = input(
        "which month? (all, january, february, ... , june? or type number of month 1, 2, 3 ...., 12)\n").lower()
    # check if user input correct or not,
    if user_input_month.lower() != "all":
        while user_input_month.lower() not in month_dict.keys() and user_input_month.lower() not in month_dict.values():
            user_input_month = input("please, try agian input not correct (all or january, february, ... , june? or "
                                     "type number of month 1, 2, 3 ...., 12)\n").lower()
    return user_input_month


# create a list of name days and all to all days the first day is monday
days_list = ["m", "tu", "w", "th", "f", "sa", "su", "all"]


def get_day():
    """
    Asks user to specify a day to filter.
    check if user input correct or not, 
    input should be in days_lis ["m", "tu", "w", "th", "f", "sa", "su", "all"]
    input accepts the string of "days" and its case variants, such as "sa", "Sa", or "SA". or all for all days
   Args:
       None.
   Returns:
       str (day): correct name of the day to filter.
   """
    # Asks user to specify a day to filter.
    user_input_day = input("which day? (all, M, Tu, W, Th, F, Sa, Su. please type a day)  \n").lower()
    # check if user input correct or not
    while user_input_day.lower() not in days_list:
        user_input_day = input("please, try again input correct choose of day? \n").lower()
    return user_input_day


def get_filters():
    """
    Args:
        None.
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-' * 44)
    return get_city(), get_month(), get_day()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # read csv file of city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # check if user want to all months of not
    if month != 'all':
        # use the key of the months dictionary to get the corresponding int
        for key, value in month_dict.items():
            # check input user if a number of month or name of month
            if month == value or month == key:
                df = df[df['month'] == int(key)]

    # check if user want to all months of not
    if day != 'all':
        day = days_list.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Args:
        DataFrame: that return by function load data.
    """
    print('-' * 40)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month 
    # diplay the number of month and name of month such as this most common month is: 2  'february'
    popular_month = df['month'].mode()[0]
    print(f"most common month is: {popular_month}  '{month_dict[str(popular_month)]}'")

    # display the most common day of week
    # display the number of dat and name of day such as most common day in week is: 2  'wednesday
    # hint week start from monday number of monday is 0
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    popular_day = df['day_of_week'].mode()[0]
    print(f"most common day in week is: {popular_day}  '{day_list[popular_day]}'")

    # display the most common start hour
    # use dt.hour to extract hours from start time
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"most common hour in day is: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Args:
        DataFrame: that return by function load data.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"most common Start Station in is: {popular_start_station}")

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"most common trip from start to end is: {popular_end_station}")

    # display most frequent combination of start station and end station trip
    df['Start_End_Station'] = df['Start Station'] + " To " + df['End Station']
    popular_trip = df['Start_End_Station'].mode()[0]
    print(f"most common trip from start to end: {popular_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    Args:
        DataFrame: that return by function load data.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time by seconds and convert seconds to day and hours and minuats
    total_travel_time = df['Trip Duration'].sum()
    resconds = datetime.timedelta(seconds=int(total_travel_time))
    print(f"average travel time is {total_travel_time} seconds '{resconds}'")

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print(f"average travel time is {average_travel_time} second")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.
    Args:
        DataFrame: that return by function load data.and city name
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types and count of NaN value
    user_types_count = df['User Type'].value_counts()
    user_NaN = df['User Type'].isna().sum()
    for index, type_count in enumerate(user_types_count):
        print("{}: {}".format(user_types_count.index[index], type_count))
    print(f"The NaN count is: {user_NaN}")

    print("-" * 25)

    # check if the city not washington 
    if city.lower() != "washington":
        # Display counts of gender
        count_gender = df['Gender'].value_counts()
        count_gender_NaN = df['Gender'].isna().sum()
        for index, gender_count in enumerate(count_gender):
            print("{}: {}".format(count_gender.index[index], gender_count))
        print(f"The NaN count is: {count_gender_NaN}")

        print("-" * 25)

        # Display earliest, most recent, and most common year of birth
        most_earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print(f"The most earliest year is: {most_earliest}")
        print(f"The most recent year is: {most_recent}")
        print(f"The most most common year of birth is: {most_common_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df, city):
    """ 
    display the raw date
    Args:
        DataFrame: that return by function load data And city name
    """

    bool_list = ['yes', 'no']
    user_input_raw = ''
    count = 0
    # check if the user input in bool list
    while user_input_raw.lower() not in bool_list:
        user_input_raw = input("Would you like view individual trip data? Type 'yes' or 'no'\n").lower()
        if user_input_raw.lower() == "yes":
            print(df.head())
        elif user_input_raw.lower() not in bool_list:
            print("\nPlease check your input.and Try again")
    # while loop to ask user if he wants to view more raw data
    while user_input_raw.lower() == 'yes':
        count += 5
        user_input_raw = input("Would you like to view more raw data? Type 'yes'\n").lower()
        if user_input_raw.lower() == "yes":
            print(df[count:count + 5])
        elif user_input_raw.lower() != "yes":
            break


def main():
    # main function
    while True:
        global city, month, day
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:  # this check if there is data to filter of not
            print('\nNo Date in this filter!, choose another filter')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
            display_raw_data(df, city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
