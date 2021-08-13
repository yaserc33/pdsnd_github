from numpy import NaN
import pandas as pd


def ask_user():
    ''' ask user which city and filter they want

    input: int city : 1 for Washington 2 for New York City  3 for Chicago ,
           int  filter_ : 1 to 6 for month and 7 to 13 for day of week start with sunday
    output: (city , filter_type)

    '''
    # choose the city
    print(
        '-' *
        60,
        '\nWelcome in US bikeshare data ^-^ \n \nWhich city do you want to see data from ?\n')
    print(' 1- Washington\n 2- New York City \n 3- Chicago ')

    while True:
        try:
            city = int(input('\nPlease enter integer number: '))
            if city == 1:
                print("~" * 50, "\nwelcome in Washington (^_^) ")
                break
            elif city == 2:
                print("~" * 50, "\nwelcome in New York City (^_^) ")
                break
            elif city == 3:
                print("~" * 50, "\nwelcome in Chicago (^_^) ")
                break
            else:
                print(
                    "~" *
                    50,
                    '\nPlease enter a valid number\n(1 for Washington , 2 for New York City and 3 for Chicago)\n \n')
        except :
            print(
                "~" *
                50,
                '\nPlease enter integer number\n(1 for Washington , 2 for New York City and 3 for Chicago)\n \n ')

    # to find filter by month or day or no filter
    print(
        "~" * 50,
        '\nDo you want to filter the data by :',
        '\n 1- month\n 2- day of the week\n 3- with out filter "to see statistics for all data" ')

    while True:
        try:
            filter_ = int(input('\nPlease enter integer number: '))
            if filter_ == 1:

                # to find which month
                print(
                    "~" * 50,
                    '\nwhich month you want to filter the data by :',
                    '\n1-January\n2-February\n3-March\n4-April\n5-may\n6-June')

                while True:
                    try:
                        filter_m = int(
                            input('\nPlease enter integer number of month: '))
                        if (filter_m == 1 or filter_m == 2 or filter_m ==
                                3 or filter_m == 4 or filter_m == 5 or filter_m == 6):
                            filter_type = filter_m
                            break
                        else:
                            print(
                                "~" * 50,
                                '\nPlease enter a valid number\n (1-January , 2-February , 3-March , 4-April , 5-may and 6-June)\n \n')
                    except :
                        print(
                            "~" * 50,
                            '\nPlease enter integer number\n(1-January , 2-February , 3-March , 4-April , 5-may and 6-June)\n \n ')
                break

            elif filter_ == 2:

                # to find which day of the week
                print(
                    "~" * 50,
                    '\nwhich day you want to filter the data by :',
                    '\n1-Sunday \n2-Monday\n3-Tuesday\n4-Wednesday\n5-Thursday\n6-Friday\n7-Saturday')

                while True:
                    try:
                        filter_d = int(
                            input('\nPlease enter integer number of month: '))
                        if (filter_d == 1 or filter_d == 2 or filter_d == 3 or filter_d ==
                                4 or filter_d == 5 or filter_d == 6 or filter_d == 7):
                            filter_type = filter_d + 6
                            break
                        else:
                            print(
                                "~" *
                                50,
                                '\nPlease enter a valid number\n (1-Sunday , 2-Monday , 3-Tuesday , 4-Wednesday , 5-Thursday , 6-Friday , 7-Saturday)\n \n')
                    except :
                        print(
                            "~" *
                            50,
                            '\nPlease enter integer number\n(1-Sunday , 2-Monday , 3-Tuesday , 4-Wednesday , 5-Thursday , 6-Friday , 7-Saturday)\n \n ')
                break
            elif filter_ == 3:
                # no filter
                filter_type = 0
                print("You chosen to see all date ^_^ ")
                break
            else:
                print(
                    "~" * 50,
                    '\nPlease enter a valid number\n(1 by month , 2 by day 3 no filter)\n \n')
        except :
            print(
                "~" * 50,
                '\nPlease enter integer number\n(1 by month , 2 by day 3 no filter)\n \n ')

    return city, filter_type
##


def data_frame_editor(city, filter_type):
    '''to load cvs file the user has chosen then to filter it

    input : int city : to load to load the cvs file ,
            int filter_type : to filter the cvs file
    output: df : dateframe after filtering

    '''
    # the following if to create dateframe from CSVs
    if city == 1:
        city_date = pd.read_csv('Washington.csv')

    elif city == 2:
        city_date = pd.read_csv('new_york_city.csv')

    else:
        city_date = pd.read_csv('chicago.csv')

    # the following if to filter date where =  0 no filter , 1-6 by month ,
    # 7-13 by day of the week
    if filter_type == 0:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date.copy()
        return df

    elif filter_type == 1:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.month_name() ==
                       'January'].copy()
        return df

    elif filter_type == 2:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.month_name() ==
                       'February'].copy()
        return df

    elif filter_type == 3:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.month_name() ==
                       'March'].copy()
        return df

    elif filter_type == 4:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.month_name() ==
                       'April'].copy()
        return df

    elif filter_type == 5:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.month_name() == 'May'].copy()
        return df

    elif filter_type == 6:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.month_name() ==
                       'June'].copy()
        return df

    elif filter_type == 7:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Sunday'].copy()
        return df
        print("77")
    elif filter_type == 8:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Monday'].copy()
        return df
    elif filter_type == 9:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Tuesday'].copy()
        return df
    elif filter_type == 10:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Wednesday'].copy()
        return df
    elif filter_type == 11:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Thursday'].copy()
        return df
    elif filter_type == 12:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Sunday'].copy()
        return df
    elif filter_type == 13:
        city_date['Start Time'] = pd.to_datetime(city_date['Start Time'])
        df = city_date[city_date['Start Time'].dt.day_name() ==
                       'Friday'].copy()
        return df
##


def stats(df, city):
    '''do stats on  dataframe "df" '''

    # answer of questions set 1
    print(
        '~' * 61,
        '\nPopular times of travel\n',
        '~' * 60,
        '\n-most common month is : ',
        (df['Start Time'].dt.month_name().mode())[0],
        '\n-most common day of the week is : ',
        (df['Start Time'].dt.day_name().mode())[0],
        '\n-most common hour is : ',
        (df['Start Time'].dt.hour.mode())[0],
        '\n')

    # answer of questions set 2
    print(
        '~' * 61,
        '\nPopular stations and trip\n',
        '~' * 60,
        '\n-most common start station is : ',
        (df['Start Station'].mode())[0],
        '\n-most common end station is : ',
        (df['End Station'].mode())[0],
        '\n-most common trip from start to end :  ',
        (df['Start Station'] + '  and  ' + df['End Station']).mode()[0],
        '\n')
    # answer of questions set 3
    print('~' * 61,
          '\nTrip duration\n',
          '~' * 60,
          '\n-total travel time is : ',
          int(df['Trip Duration'].sum() // 60),
          'minutes',
          '\n-average travel time : ',
          int(df['Trip Duration'].mean() // 60),
          'minutes\n')

    # answer of questions set 4
    print(
        '~' * 61,
        '\nUser info\n',
        '~' * 60,
        '\n-counts of each user type : \n',
        (df['User Type'] == 'Subscriber').sum(),
        ' Subscriber\n',
        (df['User Type'] == 'Customer').sum(),
        ' Customer\n')
    if (city == 2 or city == 3):
        # no need for  df.dropna(axis=0) because NAN will not affect the result
        print(
            '\n-counts of each gender : \n',
            (df['Gender'] == 'Male').sum(),
            ' Male\n',
            (df['Gender'] == 'Female').sum(),
            ' Female\n')

        print('\n- The earliest year of birth : ',
              int(df['Birth Year'].min()),
              '\n- The most recent year of birth : ',
              int(df['Birth Year'].max()),
              '\n- The agv  year of birth : ',
              int(df['Birth Year'].mean()),
              '\n')


def row_data(df):
    ''' print row data first 5 then ask user if he want more '''

    print('#' * 60, '\nDo you want to print the first 5 rows of filtered data?')
    n = 5
    while True:
        try:
            end_q = input('\nif yes type \'Y\' ,if NO type \'N\': ')
            if end_q.lower() == 'y':
                print(df.head(n), "\n")
                print(
                    '#' * 60,
                    '\nDo you want to print the extra 5 rows of filtered data?')
                while True:
                    try:
                        end_q = input(
                            '\nif yes type \'Y\' ,if NO type \'N\': ')
                        if end_q.lower() == 'y':
                            n += 5
                            print(df.head(n))
                        elif end_q.lower() == 'n':
                            return
                    except :
                        print('\nif yes type \'Y\' ,if NO type \'N\':')

            elif end_q.lower() == 'n':
                return

        except :
            print('\nif yes type \'Y\' ,if NO type \'N\':')


def main():
    city, filter_type = ask_user()
    df = data_frame_editor(city, filter_type)
    stats(df, city)
    row_data(df)

    # restart program
    print('#' * 60, '\nDo you want to restart program?')

    while True:
        try:
            end_q2 = input('\nif yes type \'Y\' ,if NO type \'N\': ')
            if end_q2.lower() == 'y':
                main()
            elif end_q2.lower() == 'n':
                break

        except :
            print('\nif yes type \'Y\' ,if NO type \'N\':')


main()
