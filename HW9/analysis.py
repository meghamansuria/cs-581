# Name:  Megha Mansuria
# Assignment 9: Analyze Social Network Data
# I pledge my honor that I have abided by the Stevens Honor System.

# analysis.py determines how often the Facebook (the company) owned social-media
# services - Facebook and Instagram - are utilized by each generation. 

# For this analysis' purpose:
# Daily includes "Several times a day" & "About once a day"
# Weekly includes "A few times a week" & "Every few weeks"
# Rarely includes "Less often"
# Unknown includes "Don't Know" & "Refused"

# The generations are:
# Generation Z (1996-TBD): ages 24 and younger
# Millennials (1977-1995): between ages 25 and 42
# Generation X (1965-1976): between ages 43 and 54
# Baby Boomers (1946-1964): between ages 55 and 73
# The Silent Generation (-1945): ages 74 and older

# To run from terminal window:  python3 analysis.py 
# A figure of pie charts will pop up and so, to quit the analysis.py program, quit the pie charts figure.

import csv
import pprint
import matplotlib.pyplot as plt

# returns whether Facebook or Instagram is most popular for Gen Z
def most_popular_genz():
    with open('Pew_Survey.csv', mode='r', newline='') as csv_file:
        fieldnames = ['respid', 'intfreq', 'snsint2', 'q20', 'web1a', 'web1b',
                    'web1c', 'web1d', 'web1e', 'web1f', 'web1g', 'web1h', 'web1i',
                    'sns2a', 'sns2b', 'sns2c', 'sns2d', 'sns2e', 'device1b', 
                    'device1c', 'device1d', 'cregion', 'sex', 'age', 'marital',
                    'educ2', 'emplnw', 'inc', 'party', 'partyln']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # get all Gen Z rows from csv file 
        genz = []
        genzcount = 0
        for i, row in enumerate(reader):
            # skips field names row
            if (i == 0):
                continue
            # Gen Z are ages 24 and younger, append row to list genz 
            # count how many total Gen Z responses, save to genzcount
            if(int(row['age']) < 25):
                genz.append(row)
                genzcount += 1

        # find all Gen Z who use Instagram
        genz_ig = []
        genz_ig_count = 0
        for z in genz:
            if (int(z['web1b']) == 1):
                genz_ig.append(z)
                genz_ig_count += 1
        
        # find Gen Z who use Instagram 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_ig = 0
        weekly_ig = 0
        rarely_ig = 0
        unknown_ig = 0
        for i in genz_ig:
            # increment for daily
            if (int(i['sns2b']) == 1 or int(i['sns2b']) == 2):
                daily_ig += 1
            # increment for weekly
            if (int(i['sns2b']) == 3 or int(i['sns2b']) == 4):
                weekly_ig += 1 
            # increment for rarely
            if (int(i['sns2b']) == 5):
                rarely_ig += 1
            # increment for don't know/refused
            if (int(i['sns2b']) == 8 or int(i['sns2b']) == 9):
                unknown_ig += 1

        # find all Gen Z who use Facebook
        genz_fb = []
        genz_fb_count = 0
        for z in genz:
            if (int(z['web1c']) == 1):
                genz_fb.append(z)
                genz_fb_count += 1
        
        # find Gen Z who use Facebook 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_fb = 0
        weekly_fb = 0
        rarely_fb = 0
        unknown_fb = 0
        for i in genz_fb:
            # increment for daily
            if (int(i['sns2c']) == 1 or int(i['sns2c']) == 2):
                daily_fb += 1
            # increment for weekly
            if (int(i['sns2c']) == 3 or int(i['sns2c']) == 4):
                weekly_fb += 1 
            # increment for rarely
            if (int(i['sns2c']) == 5):
                rarely_fb += 1 
            # increment for don't know/refused
            if (int(i['sns2c']) == 8 or int(i['sns2c']) == 9):
                unknown_fb += 1
 
        # total Generation Z participants
        print("Generation Z total participants: " + str(genzcount))
        print("        Instagram      Facebook ")
        print("Total:     "+ str(genz_ig_count).rjust(3) + "            " + str(genz_fb_count).rjust(3))
        print("Daily:     "+ str(daily_ig).rjust(3) + "            " + str(daily_fb).rjust(3))
        print("Weekly:    "+ str(weekly_ig).rjust(3) + "            " + str(weekly_fb).rjust(3))
        print("Rarely:    "+ str(rarely_ig).rjust(3) + "            " + str(rarely_fb).rjust(3))
        print("Unknown:   "+ str(unknown_ig).rjust(3) + "            " + str(unknown_fb).rjust(3))

        return genzcount, genz_ig_count, daily_ig, weekly_ig, rarely_ig, unknown_ig, genz_fb_count, daily_fb, weekly_fb, rarely_fb, unknown_fb

# returns whether Facebook or Instagram is most popular for Millennials
def most_popular_mil():
    with open('Pew_Survey.csv', mode='r', newline='') as csv_file:
        fieldnames = ['respid', 'intfreq', 'snsint2', 'q20', 'web1a', 'web1b',
                    'web1c', 'web1d', 'web1e', 'web1f', 'web1g', 'web1h', 'web1i',
                    'sns2a', 'sns2b', 'sns2c', 'sns2d', 'sns2e', 'device1b', 
                    'device1c', 'device1d', 'cregion', 'sex', 'age', 'marital',
                    'educ2', 'emplnw', 'inc', 'party', 'partyln']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # get all Millennials rows from csv file 
        mil = []
        milcount = 0
        for i, row in enumerate(reader):
            # skips field names row
            if (i == 0):
                continue
            # Millennials are between ages 25 and 42, append row to list mil 
            # count how many total Milennial responses, save to milcount
            if(int(row['age']) > 24 and (int(row['age']) < 43)):
                mil.append(row)
                milcount += 1

        # find all Millennials who use Instagram
        mil_ig = []
        mil_ig_count = 0
        for m in mil:
            if (int(m['web1b']) == 1):
                mil_ig.append(m)
                mil_ig_count += 1
        
        # find Millennials who use Instagram 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_ig = 0
        weekly_ig = 0
        rarely_ig = 0
        unknown_ig = 0
        for i in mil_ig:
            # increment for daily
            if (int(i['sns2b']) == 1 or int(i['sns2b']) == 2):
                daily_ig += 1
            # increment for weekly
            if (int(i['sns2b']) == 3 or int(i['sns2b']) == 4):
                weekly_ig += 1 
            # increment for rarely
            if (int(i['sns2b']) == 5):
                rarely_ig += 1 
            # increment for don't know/refused
            if (int(i['sns2b']) == 8 or int(i['sns2b']) == 9):
                unknown_ig += 1

        # find all Millennials who use Facebook
        mil_fb = []
        mil_fb_count = 0
        for m in mil:
            if (int(m['web1c']) == 1):
                mil_fb.append(m)
                mil_fb_count += 1
        
        # find Millennials who use Facebook 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_fb = 0
        weekly_fb = 0
        rarely_fb = 0
        unknown_fb = 0
        for i in mil_fb:
            # increment for daily
            if (int(i['sns2c']) == 1 or int(i['sns2c']) == 2):
                daily_fb += 1
            # increment for weekly
            if (int(i['sns2c']) == 3 or int(i['sns2c']) == 4):
                weekly_fb += 1 
            # increment for rarely
            if (int(i['sns2c']) == 5):
                rarely_fb += 1 
            # increment for don't know/refused
            if (int(i['sns2c']) == 8 or int(i['sns2c']) == 9):
                unknown_fb += 1

        # total Millennials participants
        print("Millennial total participants: " + str(milcount))
        print("        Instagram      Facebook ")
        print("Total:     "+ str(mil_ig_count).rjust(3) + "            " + str(mil_fb_count).rjust(3))
        print("Daily:     "+ str(daily_ig).rjust(3) + "            " + str(daily_fb).rjust(3))
        print("Weekly:    "+ str(weekly_ig).rjust(3) + "            " + str(weekly_fb).rjust(3))
        print("Rarely:    "+ str(rarely_ig).rjust(3) + "            " + str(rarely_fb).rjust(3))
        print("Unknown:   "+ str(unknown_ig).rjust(3) + "            " + str(unknown_fb).rjust(3))

        return milcount, mil_ig_count, daily_ig, weekly_ig, rarely_ig, unknown_ig, mil_fb_count, daily_fb, weekly_fb, rarely_fb, unknown_fb

# returns whether Facebook or Instagram is most popular for Generation X
def most_popular_genx():
    with open('Pew_Survey.csv', mode='r', newline='') as csv_file:
        fieldnames = ['respid', 'intfreq', 'snsint2', 'q20', 'web1a', 'web1b',
                    'web1c', 'web1d', 'web1e', 'web1f', 'web1g', 'web1h', 'web1i',
                    'sns2a', 'sns2b', 'sns2c', 'sns2d', 'sns2e', 'device1b', 
                    'device1c', 'device1d', 'cregion', 'sex', 'age', 'marital',
                    'educ2', 'emplnw', 'inc', 'party', 'partyln']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # get all Gen X rows from csv file 
        genx = []
        genxcount = 0
        for i, row in enumerate(reader):
            # skips field names row
            if (i == 0):
                continue
            # Gen X are between ages 43 and 54, append row to list genx 
            # count how many total Gen X responses, save to genxcount
            if(int(row['age']) > 42 and (int(row['age']) < 55)):
                genx.append(row)
                genxcount += 1

        # find all Gen X who use Instagram
        genx_ig = []
        genx_ig_count = 0
        for x in genx:
            if (int(x['web1b']) == 1):
                genx_ig.append(x)
                genx_ig_count += 1
        
        # find Gen X who use Instagram 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_ig = 0
        weekly_ig = 0
        rarely_ig = 0
        unknown_ig = 0
        for i in genx_ig:
            # increment for daily
            if (int(i['sns2b']) == 1 or int(i['sns2b']) == 2):
                daily_ig += 1
            # increment for weekly
            if (int(i['sns2b']) == 3 or int(i['sns2b']) == 4):
                weekly_ig += 1 
            # increment for rarely
            if (int(i['sns2b']) == 5):
                rarely_ig += 1 
            # increment for don't know/refused
            if (int(i['sns2b']) == 8 or int(i['sns2b']) == 9):
                unknown_ig += 1
        
        # find all Gen X who use Facebook
        genx_fb = []
        genx_fb_count = 0
        for x in genx:
            if (int(x['web1c']) == 1):
                genx_fb.append(x)
                genx_fb_count += 1
        
        # find Gen X who use Facebook 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_fb = 0
        weekly_fb = 0
        rarely_fb = 0
        unknown_fb = 0
        for i in genx_fb:
            # increment for daily
            if (int(i['sns2c']) == 1 or int(i['sns2c']) == 2):
                daily_fb += 1
            # increment for weekly
            if (int(i['sns2c']) == 3 or int(i['sns2c']) == 4):
                weekly_fb += 1 
            # increment for rarely
            if (int(i['sns2c']) == 5):
                rarely_fb += 1
            # increment for don't know/refused
            if (int(i['sns2c']) == 8 or int(i['sns2c']) == 9):
                unknown_fb += 1 

        # total Generation X participants
        print("Generation X total participants: " + str(genxcount))
        print("        Instagram      Facebook ")
        print("Total:     "+ str(genx_ig_count).rjust(3) + "            " + str(genx_fb_count).rjust(3))
        print("Daily:     "+ str(daily_ig).rjust(3) + "            " + str(daily_fb).rjust(3))
        print("Weekly:    "+ str(weekly_ig).rjust(3) + "            " + str(weekly_fb).rjust(3))
        print("Rarely:    "+ str(rarely_ig).rjust(3) + "            " + str(rarely_fb).rjust(3))
        print("Unknown:   "+ str(unknown_ig).rjust(3) + "            " + str(unknown_fb).rjust(3))

        return genxcount, genx_ig_count, daily_ig, weekly_ig, rarely_ig, unknown_ig, genx_fb_count, daily_fb, weekly_fb, rarely_fb, unknown_fb

# returns whether Facebook or Instagram is most popular for Baby Boomers
def most_popular_baby():
    with open('Pew_Survey.csv', mode='r', newline='') as csv_file:
        fieldnames = ['respid', 'intfreq', 'snsint2', 'q20', 'web1a', 'web1b',
                    'web1c', 'web1d', 'web1e', 'web1f', 'web1g', 'web1h', 'web1i',
                    'sns2a', 'sns2b', 'sns2c', 'sns2d', 'sns2e', 'device1b', 
                    'device1c', 'device1d', 'cregion', 'sex', 'age', 'marital',
                    'educ2', 'emplnw', 'inc', 'party', 'partyln']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # get all Baby Boomers rows from csv file 
        baby = []
        babycount = 0
        for i, row in enumerate(reader):
            # skips field names row
            if (i == 0):
                continue
            # Baby Boomers are between ages 55 and 73, append row to list baby 
            # count how many total Baby Boomers responses, save to babycount
            if(int(row['age']) > 54 and (int(row['age']) < 74)):
                baby.append(row)
                babycount += 1

        # find all Baby Boomers who use Instagram
        baby_ig = []
        baby_ig_count = 0
        for b in baby:
            if (int(b['web1b']) == 1):
                baby_ig.append(b)
                baby_ig_count += 1

        # find Baby Boomers who use Instagram 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_ig = 0
        weekly_ig = 0
        rarely_ig = 0
        unknown_ig = 0
        for i in baby_ig:
            # increment for daily
            if (int(i['sns2b']) == 1 or int(i['sns2b']) == 2):
                daily_ig += 1
            # increment for weekly
            if (int(i['sns2b']) == 3 or int(i['sns2b']) == 4):
                weekly_ig += 1 
            # increment for rarely
            if (int(i['sns2b']) == 5):
                rarely_ig += 1 
            # increment for don't know/refused
            if (int(i['sns2b']) == 8 or int(i['sns2b']) == 9):
                unknown_ig += 1
        
        # find all Baby Boomers who use Facebook
        baby_fb = []
        baby_fb_count = 0
        for b in baby:
            if (int(b['web1c']) == 1):
                baby_fb.append(b)
                baby_fb_count += 1
        
        # find Baby Boomers who use Facebook 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_fb = 0
        weekly_fb = 0
        rarely_fb = 0
        unknown_fb = 0
        for i in baby_fb:
            # increment for daily
            if (int(i['sns2c']) == 1 or int(i['sns2c']) == 2):
                daily_fb += 1
            # increment for weekly
            if (int(i['sns2c']) == 3 or int(i['sns2c']) == 4):
                weekly_fb += 1 
            # increment for rarely
            if (int(i['sns2c']) == 5):
                rarely_fb += 1
            # increment for don't know/refused
            if (int(i['sns2c']) == 8 or int(i['sns2c']) == 9):
                unknown_fb += 1 

        # total Baby Boomer participants
        print("Baby Boomer total participants: " + str(babycount))
        print("        Instagram      Facebook ")
        print("Total:     "+ str(baby_ig_count).rjust(3) + "            " + str(baby_fb_count).rjust(3))
        print("Daily:     "+ str(daily_ig).rjust(3) + "            " + str(daily_fb).rjust(3))
        print("Weekly:    "+ str(weekly_ig).rjust(3) + "            " + str(weekly_fb).rjust(3))
        print("Rarely:    "+ str(rarely_ig).rjust(3) + "            " + str(rarely_fb).rjust(3))
        print("Unknown:   "+ str(unknown_ig).rjust(3) + "            " + str(unknown_fb).rjust(3))

        return babycount, baby_ig_count, daily_ig, weekly_ig, rarely_ig, unknown_ig, baby_fb_count, daily_fb, weekly_fb, rarely_fb, unknown_fb

# returns whether Facebook or Instagram is most popular for The Silent Generation
def most_popular_silent():
    with open('Pew_Survey.csv', mode='r', newline='') as csv_file:
        fieldnames = ['respid', 'intfreq', 'snsint2', 'q20', 'web1a', 'web1b',
                    'web1c', 'web1d', 'web1e', 'web1f', 'web1g', 'web1h', 'web1i',
                    'sns2a', 'sns2b', 'sns2c', 'sns2d', 'sns2e', 'device1b', 
                    'device1c', 'device1d', 'cregion', 'sex', 'age', 'marital',
                    'educ2', 'emplnw', 'inc', 'party', 'partyln']
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)

        # get all Silent Generation rows from csv file 
        silent = []
        silentcount = 0
        for i, row in enumerate(reader):
            # skips field names row
            if (i == 0):
                continue
            # The Silent Generation are ages 74 and older, append row to list silent 
            # count how many total Silent Generation responses, save to silentcount
            if(int(row['age']) > 73):
                silent.append(row)
                silentcount += 1

        # find all Silent Generation who use Instagram
        silent_ig = []
        silent_ig_count = 0
        for s in silent:
            if (int(s['web1b']) == 1):
                silent_ig.append(s)
                silent_ig_count += 1
        
        # find Silent Generation who use Instagram 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_ig = 0
        weekly_ig = 0
        rarely_ig = 0
        unknown_ig = 0
        for i in silent_ig:
            # increment for daily
            if (int(i['sns2b']) == 1 or int(i['sns2b']) == 2):
                daily_ig += 1
            # increment for weekly
            if (int(i['sns2b']) == 3 or int(i['sns2b']) == 4):
                weekly_ig += 1 
            # increment for rarely
            if (int(i['sns2b']) == 5):
                rarely_ig += 1 
            # increment for don't know/refused
            if (int(i['sns2b']) == 8 or int(i['sns2b']) == 9):
                unknown_ig += 1

        # find all Silent Generation who use Facebook
        silent_fb = []
        silent_fb_count = 0
        for s in silent:
            if (int(s['web1c']) == 1):
                silent_fb.append(s)
                silent_fb_count += 1
        
        # find Baby Boomers who use Facebook 
        # - daily (several or once a day)
        # - weekly (few times a week or every few weeks)
        # - rarely (less often)
        # - unknown (don't know or refused)
        daily_fb = 0
        weekly_fb = 0
        rarely_fb = 0
        unknown_fb = 0
        for i in silent_fb:
            # increment for daily
            if (int(i['sns2c']) == 1 or int(i['sns2c']) == 2):
                daily_fb += 1
            # increment for weekly
            if (int(i['sns2c']) == 3 or int(i['sns2c']) == 4):
                weekly_fb += 1 
            # increment for rarely
            if (int(i['sns2c']) == 5):
                rarely_fb += 1
            # increment for don't know/refused
            if (int(i['sns2c']) == 8 or int(i['sns2c']) == 9):
                unknown_fb += 1 

        # total Silent Generation participants
        print("Silent Generation total participants: " + str(silentcount))
        print("        Instagram      Facebook ")
        print("Total:     "+ str(silent_ig_count).rjust(3) + "            " + str(silent_fb_count).rjust(3))
        print("Daily:     "+ str(daily_ig).rjust(3) + "            " + str(daily_fb).rjust(3))
        print("Weekly:    "+ str(weekly_ig).rjust(3) + "            " + str(weekly_fb).rjust(3))
        print("Rarely:    "+ str(rarely_ig).rjust(3) + "            " + str(rarely_fb).rjust(3))
        print("Unknown:   "+ str(unknown_ig).rjust(3) + "            " + str(unknown_fb).rjust(3))

        return silentcount, silent_ig_count, daily_ig, weekly_ig, rarely_ig, unknown_ig, silent_fb_count, daily_fb, weekly_fb, rarely_fb, unknown_fb

# main routine
def main():
    # call each generational function and print the results
    print("\nInstagram and Facebook usage by each generation:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    genzcount, genz_ig_count, dailyiz, weeklyiz, rarelyiz, unknowniz, genz_fb_count, dailyfz, weeklyfz, rarelyfz, unknownfz = most_popular_genz()
    print("\n------------------------------------------------\n")
    milcount, mil_ig_count, dailyim, weeklyim, rarelyim, unknownim, mil_fb_count, dailyfm, weeklyfm, rarelyfm, unknownfm = most_popular_mil()
    print("\n------------------------------------------------\n")
    genxcount, genx_ig_count, dailyix, weeklyix, rarelyix, unknownix, genx_fb_count, dailyfx, weeklyfx, rarelyfx, unknownfx = most_popular_genx()
    print("\n------------------------------------------------\n")
    babycount, baby_ig_count, dailyib, weeklyib, rarelyib, unknownib, baby_fb_count, dailyfb, weeklyfb, rarelyfb, unknownfb = most_popular_baby()
    print("\n------------------------------------------------\n")
    silentcount, silent_ig_count, dailyis, weeklyis, rarelyis, unknownis, silent_fb_count, dailyfs, weeklyfs, rarelyfs, unknownfs = most_popular_silent()
    print()

    # create pie charts for each generation with their usage breakdowns
    labels = 'Daily', 'Weekly', 'Rarely', 'Unknown'
    colors = '#AED5FF', '#FFCB89', '#FFF289', '#FF9E89'  #D7C8FF
    fig = plt.figure(figsize=(12,6.5))

    # pie charts of Gen Z
    # Instagram chart
    genz_ig = [dailyiz, weeklyiz, rarelyiz, unknowniz]
    ax1 = fig.add_subplot(341)
    ax1.axis('equal')
    ax1.pie(genz_ig, labels=labels, autopct='%1.1f%%', colors=colors)
    ax1.set_title('Gen Z IG Usage')
    # Facebook chart
    genz_fb = [dailyfz, weeklyfz, rarelyfz, unknownfz]
    ax2 = fig.add_subplot(342)
    ax2.pie(genz_fb, labels=labels, autopct='%1.1f%%', colors=colors)
    ax2.set_title('Gen Z FB Usage')
    ax2.axis('equal')

    # pie charts of Millennials
    # Instagram chart
    mil_ig = [dailyim, weeklyim, rarelyim, unknownim]
    ax3 = fig.add_subplot(343)
    ax3.axis('equal')
    ax3.pie(mil_ig, labels=labels, autopct='%1.1f%%', colors=colors)
    ax3.set_title('Millennial IG Usage')
    # Facebook chart
    mil_fb = [dailyfm, weeklyfm, rarelyfm, unknownfm]
    ax4 = fig.add_subplot(344)
    ax4.pie(mil_fb, labels=labels, autopct='%1.1f%%', colors=colors)
    ax4.set_title('Millennial FB Usage')
    ax4.axis('equal')

    # pie charts of Gen X
    # Instagram chart
    genx_ig = [dailyix, weeklyix, rarelyix, unknownix]
    ax5 = fig.add_subplot(345)
    ax5.axis('equal')
    ax5.pie(genx_ig, labels=labels, autopct='%1.1f%%', colors=colors)
    ax5.set_title('Gen X IG Usage')
    # Facebook chart
    genx_fb = [dailyfx, weeklyfx, rarelyfx, unknownfx]
    ax6 = fig.add_subplot(346)
    ax6.pie(genx_fb, labels=labels, autopct='%1.1f%%', colors=colors)
    ax6.set_title('Gen X FB Usage')
    ax6.axis('equal')

    # pie charts of Baby Boomer
    # Instagram chart
    baby_ig = [dailyib, weeklyib, rarelyib, unknownib]
    ax7 = fig.add_subplot(347)
    ax7.axis('equal')
    ax7.pie(baby_ig, labels=labels, autopct='%1.1f%%', colors=colors)
    ax7.set_title('Baby Boomer IG Usage')
    # Facebook chart
    baby_fb = [dailyfb, weeklyfb, rarelyfb, unknownfb]
    ax8 = fig.add_subplot(348)
    ax8.pie(baby_fb, labels=labels, autopct='%1.1f%%', colors=colors)
    ax8.set_title('Baby Boomer FB Usage')
    ax8.axis('equal')

    # pie charts of Silent Gen
    # Instagram chart
    silent_ig = [dailyis, weeklyis, rarelyis, unknownis]
    ax9 = fig.add_subplot(3,4,10)
    ax9.axis('equal')
    ax9.pie(silent_ig, labels=labels, autopct='%1.1f%%', colors=colors)
    ax9.set_title('Silent Gen IG Usage')
    # Facebook chart
    silent_fb = [dailyfs, weeklyfs, rarelyfs, unknownfs]
    ax10 = fig.add_subplot(3,4,11)
    ax10.pie(silent_fb, labels=labels, autopct='%1.1f%%', colors=colors)
    ax10.set_title('Silent Gen FB Usage')
    ax10.axis('equal')

    plt.tight_layout()
    plt.show()
    
    return

if __name__ == "__main__":
    main()