# Name:  Megha Mansuria
# Assignment 3: Using the Google APIs to access YouTube Data
# I pledge my honor that I have abided by the Stevens Honor System.

# Source: I started by using the youtube_data.py file provided by the instructor (Dr. Cheryl Dugas) 
# as a foundation, but I have written additional code to supplement the assignment requirements.

# youtube_api.py searches YouTube for videos matching a search term and prints max number of results. 
# Each entry is sorted according to 3 analysis sections: 
# (1) newest first
# (2) highest views first
# (3) highest like percentage (like count/view count) first

# To run from terminal window:   python3 youtube_api.py 

from googleapiclient.discovery import build      # use build function to create a service object
import csv
import pprint

# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyAlSxNCx-exiOpniETAT7Y8-fjrSldiGJM"
API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

#  function youtube_search retrieves the YouTube records
def youtube_search(s_term, s_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_data = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()

    #yt_file = open('output.csv', 'w')
    with open('output.csv', mode='w', newline='') as csv_file: 
        # fieldnames is a list of the column headers, specifies the order in which its written
        fieldnames = ['id', 'publishedAt', 'title', 'duration', 'viewCount', 'likeCount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader() # writes the header

        # search for videos matching search term;
        for search_instance in search_data.get("items", []):
            if search_instance["id"]["kind"] == "youtube#video":

                # get videoId, title, date
                videoId = search_instance["id"]["videoId"]  
                title = search_instance["snippet"]["title"]
                publishedAt = search_instance["snippet"]["publishedAt"]   

                # get views and likes     
                video_data = youtube.videos().list(id=videoId,part="statistics").execute()
                for video_instance in video_data.get("items",[]):
                    viewCount = video_instance["statistics"]["viewCount"]
                    if 'likeCount' not in video_instance["statistics"]:
                        likeCount = 0
                    else:
                        likeCount = video_instance["statistics"]["likeCount"]

                # get duration 
                video_duration_times = youtube.videos().list(id=videoId,part="contentDetails").execute()
                for video_dur_instance in video_duration_times.get("items", []):
                    duration = video_dur_instance["contentDetails"]["duration"]
            
                # print the raw data in the .csv file called output.txt
                writer.writerow({'id': videoId,'publishedAt': publishedAt, 'title': title, 'duration': duration, 'viewCount': viewCount, 'likeCount': likeCount})

# print in console - newest video first 
def newest_first():
    with open('output.csv', mode='r', newline='') as csv_file:
        fieldnames = ['id', 'publishedAt', 'title', 'duration', 'viewCount', 'likeCount']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # sort by newest first
        sorted_newest = sorted(reader, key=lambda row: row['publishedAt'], reverse=True)

        # print analysis description
        print("\n************************ NEWEST VIDEO FIRST: *************************")
        print("                 title, id, date published, duration                  ")
        print("**********************************************************************\n")

        # pretty print output for newest videos
        pp = pprint.PrettyPrinter(indent=4)
        for i,row in enumerate(sorted_newest):
            if i == 0:
                continue
            print(str(i), " ", row['title'], row['id'], row['publishedAt'], row['duration'])

# print in console - top 5 highest views first 
def highest_views():
    with open('output.csv', mode='r', newline='') as csv_file:
        fieldnames = ['id', 'publishedAt', 'title', 'duration', 'viewCount', 'likeCount']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # copy reader into a new array copied_data
        copied_data = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            copied_data.append(row)

        # sort by highest views first
        copied_data.sort(key=lambda row: int(row['viewCount']), reverse=True)

        # print analysis description
        print("\n************************ HIGHEST VIEWS FIRST: ************************")
        print("              title, id, date published, duration, views              ")
        print("**********************************************************************\n")

        # pretty print output for highest views
        pp = pprint.PrettyPrinter(indent=4)
        for i,row in enumerate(copied_data, 1):
            print(str(i), " ", row['title'], row['id'], row['publishedAt'], row['duration'], row['viewCount'])
            if i == 5:
                break

# print in console - top 5 highest like percentage first 
def highest_percentage():
    with open('output.csv', mode='r', newline='') as csv_file:
        fieldnames = ['id', 'publishedAt', 'title', 'duration', 'viewCount', 'likeCount']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
 
        # copy reader into a new array copied_data
        copied_data = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            copied_data.append(row)

        # add new column of like_percentage for each video
        for row in copied_data:
            likes = float(row['likeCount'])
            views = float(str(row['viewCount']))
            row['like_percentage'] = str(likes / views * 100)
    
        # sort by highest like percentage first
        copied_data.sort(key=lambda row: row['like_percentage'], reverse=True)
        
        # print analysis description
        print("\n******************* HIGHEST LIKE PERCENTAGE FIRST: *******************")
        print("  title, id, like percentage, views, likes, date published, duration  ")
        print("**********************************************************************\n")
        
        # pretty print output for highest views
        pp = pprint.PrettyPrinter(indent=4)
        for i,row in enumerate(copied_data,1):
            print(str(i), " ", row['title'], row['id'], row['like_percentage'], row['viewCount'], row['likeCount'], row['publishedAt'], row['duration'])
            if i == 5:
                break

# main routine
def main():
    # get input from user
    print("Enter a term to search for: ")
    search_term = input()
    print("Enter a maximum number of results: ")
    search_max = input()
    
    # run function to save raw data to csv file
    youtube_search(search_term, search_max)

    # run function to print newest first in console
    newest_first()

    # run function to print highest views first in console
    highest_views()

    # run function to print highest percentage first in console
    highest_percentage()
    print("")

if __name__ == "__main__":
    main()
