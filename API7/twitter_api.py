#  Author: Megha Mansuria
#  Assignment 7: Using the Twitter API to access Twitter Data
#  I pledge my honor that I have abided by the Stevens Honor System.

#  Source: I started by using the twitter_data.py file provided by the instructor (Dr. Cheryl Dugas) 
#  as a foundation, but I have written additional code to supplement the assignment requirements.

#  Description:
#  twitter_api.py allows the user to input twitter user screen names and returns the following results:
#  (1) User Screen Name     (2) User Name                (3) User ID
#  (4) User Description     (5) Location                 (6) Number of Friends
#  (7) Number of Followers  (8) 5 Most Recent Followers  (9) 5 Most Recent Tweets

#  To run in a terminal window:   python3 twitter_api.py
#  Detailed instructions: keep entering twitter user screen names to get data, enter STOP to end program

import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "zVbbPyesSgAWCdlwxJQ8IGBHj"
CONSUMER_KEY_SECRET = "gOxTrj0MQbX7Gb45Vk4DiEdUFDjBx483Wnyj0St60QbVzXuQfY"
ACCESS_TOKEN = "1325663697247891457-3bzkb8JPkuq2xxzw9OhrJ19gVeyU4f"
ACCESS_TOKEN_SECRET = "NyviZMWCWaOrRyTHBsaZ6CwOhzp9A2j1ytgHoqsV4eYgM"

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
                 
# Get Information About a Twitter User Account
def get_information(screenName):
    # api.get_user to look for the provided user screen name
    # Prints error and returns if user does not exist
    try:
        twitter_user = api.get_user(screen_name=screenName)
    except tweepy.TweepError as e:
        print("Error:", e.args[0][0]['message'])
        return

    # Get Basic Account Information
    print("********** Basic Information **********")
    # Print given screen name
    print("(1) User Screen Name: " + screenName)
    # Print the associated name
    print("(2) User Name: " + twitter_user.name)
    # Print twitter user ID
    print("(3) User ID: " + str(twitter_user.id))
    # Print user's description (bio)
    print("(4) User Description: " + twitter_user.description)
    # Print user's location (location found in description/bio)
    print("(5) Location: " + twitter_user.location)
    # Print user's number of friends (who they follow)
    print("(6) Number of Friends: " + str(twitter_user.friends_count))
    # Print user's number of followers
    print("(7) Number of Followers: " + str(twitter_user.followers_count))

    # Determine an Account’s 5 Most Recent Followers
    print("\n****** 5 Most Recent Followers: *******")
    
    # Creating a Cursor. Get and print 5 followers
    cursor = tweepy.Cursor(api.followers, screen_name=screenName)
    for account in cursor.items(5):
        print(account.screen_name)

    # Determine an account’s 5 Most Recent Tweets
    print("\n******** 5 Most Recent Tweets: ********")

    # Creating a Cursor
    cursor = tweepy.Cursor(api.user_timeline, screen_name=screenName)
    # Get and print 5 tweets
    # Use enumerate to label: TWEET 1, TWEET 2, ...
    for i, tweet in enumerate(cursor.items(5), 1):
        print("TWEET " + str(i))
        print(tweet.text)
        print()

def main():
    # While loop for getting input from the user
    userinput = input('Enter a Twitter User Screen Name: ') # Get User Screen Name
    while (userinput != 'STOP'):
        # Call get_information using the userinput parameter
        get_information(userinput)
        # Prompt user for another input 
        userinput = input('Enter another Twitter User Screen Name: ')

    # Print exit message and return
    print("Thank you for using twitter_api.py! Goodbye!\n")
    return

if __name__ == "__main__":
    main()