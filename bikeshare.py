import time
import datetime
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

    print("\nHello! Let's explore some US bikeshare data!\n")

    # get user input for city (chicago, new york city, washington)

    city = input("Would you like to see data for Chicago, New York city or Washington? ")
    while city.lower() not in (CITY_DATA.keys()):
        print("\nSorry! you entered a wrong city name\n")
        city = input("Would you like to see data for Chicago, New York city or Washington? ").lower()
        


    # get user input for month (all, january, february, ... , june)

    months_list = ["january", "february", "march", "april", "may", "june", "all"]
    month = input("\nWhich month? please, choose from : january, february, march, april, may, june or all if you don't want a month filter:  ").lower()

    while month not in months_list:
        print("\nInvalid month name. Please, try again!\n")
        month = input("Which month? please, choose from : january, february, march, april, may, june or all if you don't want a month filter:  ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" , "all"]
    day = input("\nWhich day? please choose from: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all if you don't want a day filter:  ").lower()

    while day not in days_list:
        print("\nInvalid day name. Please, try again!\n")
        day = input("Which day? please choose from: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all if you don't want a day filter:  ").lower

    print('-'*40)  
     
    return city, month, day


def load_data(city, month ,day) :
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])

    # Convert 'Start Time' column in the DataFrame to datetime type

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # add 'month', 'day_of_week', 'hour' columns to the DataFrame

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable

    months_list = ["january", "february", "march", "april", "may", "june"]
    if month != "all" :
        month = months_list.index(month) +1

        # filter by month to create the new dataframe

        df = df[df['month'] == month]
    
    # filter by day if applicable

    if day != "all":

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    print("\nThe most common Month: {}\n".format(most_common_month))

    # display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print("\nThe most common Day: {}\n".format(most_common_day))

    # display the most common start hour

    most_common_hour = df['hour'].mode()[0]
    print("\nThe most common Hour: {}\n".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print("\nThe most common Start Station is: {}".format(common_start_station))

    # display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print("\nThe most common End Station is: {}".format(common_end_station))

    # Create a column in the DataFrame contains the trip

    df['Trip'] = " from " + df['Start Station'] + " to " + df['End Station']

    # display most frequent combination of start station and end station trip

    most_popular_trip = df['Trip'].mode()[0]
    print("\nThe most Popular Trip is: {}".format(most_popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print("\nThe Total Travel Time is: {} Days".format(total_travel_time / 86400))

    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe Mean Travel Time is: {} Minutes".format(mean_travel_time / 60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print("\nThe Counts of each User Type:\n{}".format(user_types))


    # Display counts of gender

    if "Gender" in (df.columns):
        gender_types = df['Gender'].value_counts()
        print("\nGender Types:\n {}".format(gender_types))

    else:
        print("\nThere is no Gender data for Washington")
    
    
    

    # Display earliest, most recent, and most common year of birth

    if "Birth Year" in (df.columns):

        earliest_year = df['Birth Year'].min().astype(int)
        print("\nThe Oldest User Birth Year is: {}".format(earliest_year))

        recent_year = df['Birth Year'].max().astype(int)
        print("\nThe Youngest User Birth Year is: {}".format(recent_year))

        most_common_year = df['Birth Year'].mode()[0].astype(int)
        print("\nThe most common Birth Year is: {}".format(most_common_year))

    else:
        print("\nThere is no Birth Year data for Washington")

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    """
    Asks if the user wants to see raw data
    
    Returns:
    Additional five rows of the raw data each time the user inputs 'yes'

    """

    # get user input for showing raw data

    user_input = input("\nDo you want to see five rows of the raw data? Enter 'yes' or 'no'\n")
    while user_input.lower() not in ['yes' , 'no']:
        print("\nInvalid input! please, choose 'yes or 'no")
        user_input = input("\nDo you want to see five rows of the raw data? Enter 'yes' or 'no'\n")


    # Display five rows each time from the raw data if user inputs yes

    count = 0
    while user_input.lower() == 'yes':
        count += 5
        print(df.head(count))
        user_input = input("\nDo you want to see another five rows of the raw data? Enter 'yes' or 'no'\n")

    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()