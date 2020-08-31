import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city_list = {'chicago', 'new york city', 'washington'}
    city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()

    while city not in city_list:
        city = input('You provided invalid input. Please type "Chicago", "New York", or "Washington" to select a city. ').lower()

    print(f'Okay, let\'s look at data for {city.title()}.')
    month_filter = input('Would you like to filter data by a specific month? Type "yes" or "no". ').lower()
    while month_filter != 'yes' and month_filter != 'no':
        month_filter = input('You provided invalid input. Please type "yes" if you would like to filter by a specific month. Otherwise, type "no". ').lower()

    month_list = {'january', 'february', 'march', 'april', 'may', 'june', 'all'}
    if month_filter == 'yes':
        month = input('We have data from January through June. Type the month (January, February, March, April, May, or June) you want to filter on. ').lower()
        while month not in month_list:
            month = input('You provided invalid input. Please type the full name of the month you want to filter on. If you no longer want to filter by month, type "all". ').lower()
    else:
        month = 'all'

    day_filter = input('Would you like to filter data by a specific day? Type "yes" or "no". ').lower()
    while day_filter != 'yes' and day_filter != 'no':
        day_filter = input('You provided invalid input. Please type "yes" if you would like to filter by a specific day. Otherwise, type "no". ').lower()

    day_list = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'}
    if day_filter == 'yes':
        day = input('Please type the day of the week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday) you want to filter on. ').lower()
        while day not in day_list:
            day = input('You provided invalid input. Please type the full name of the day of the week you want to filter on. If you no longer want to filter by day, type "all". ').lower()
    else:
        day = 'all'


    print('-'*40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_idx = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month_idx]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print(f'Most common month: {months[common_month - 1].title()}')

    # display the most common day of week
    common_day = df['Start Time'].dt.weekday_name.mode()[0]
    print(f'Most common day: {common_day}')

    # display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'Most common start hour: {common_start_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'Most common start station: {common_start_station}')

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'Most common end station: {common_end_station}')

    # display most frequent combination of start station and end station trip
    print('Most common combination of start station and end station:')
    print('Start station - ' + (df['Start Station'] + '\nEnd station - ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(f'Total travel time: {total_time}')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    Args:
        (str) city - name of the city to analyze
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:')
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)

    if city == 'chicago' or city == 'new york city':
        # Display counts of gender
        print('Counts of gender:')
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print(f'Earliest birth year: {earliest_birth_year}')

        most_recent_birth_year = df['Birth Year'].max()
        print(f'Most recent birth year: {most_recent_birth_year}')

        most_common_birth_year = df['Birth Year'].mode()[0]
        print(f'Most common birth year: {most_common_birth_year}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data from dataframe 5 rows at a time"""

    print_question = input('Type "yes" if you would like to see the first 5 rows of raw data: ')
    if print_question.lower() == 'yes':
        start_idx = 0
        end_idx = 5
        df_size = df.shape[0]

        while end_idx <= df_size:
            print(df.iloc[start_idx:end_idx])
            print_continue = input('Type "yes" if you would like to see the next 5 rows of raw data: ')
            if print_continue.lower() != 'yes':
                break
            start_idx += 5
            end_idx += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
