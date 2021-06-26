# **Election-Analysis**

#### **Overview of Election Audit**
 - The purpose of this audit was to fist determine who the winner of the election was. I had to count the total votes, count the total votes per canidate, and divide them together to see who had the most votes and highest percentage. I then had to print the results to a .txt file, so it would be easy to read. It was great to see who won the election, but it would also be nice to see where the majority of votes came from. After determining the winner, I had to figure out which county had the most votes, and add that to the .txt file. 

#### **Election Audit Results**
- ```
    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)

    -------------------------
    Winner: Denver
    Winning County Vote Count: 306,055
    Winning County Percentage: 82.8%
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------
  ```
- **Overview of the Results**
- - The total votes for the election equalled 369,711, with Denver having the most votes at 306,055. This accounted for 82.8% of the total votes! It is easy to say whoever won Denver was going to most likely win the election. 
- - The winner was Diana Degette, with a total of 272,892 votes. This accounted for 73.8% of the total votes, and blew her competition out of the water. 

#### **Election Audit Summary**
- This script will be able to be used with any election, and only needs some simple modifications. 
- - **Examples of Modifications**
- - - ```
        Election Results
        -------------------------
        Total Votes: 778,287
        -------------------------

        State Votes:
        Alabama: 5.0% (38,855)

        Texas: 39.3% (306,055)

        Kansas: 3.2% (24,801)

        Tennessee: 52.5% (408,576)

        -------------------------
        Winner: Tennessee
        Winning State Vote Count: 408,576
        Winning State Percentage: 52.5%
        -------------------------
        Charles Casper Stockham: 10.9% (85,213)
        Diana DeGette: 35.1% (272,892)
        Raymon Anthony Doane: 1.5% (11,606)
        Joe Biden: 52.5% (408,576)
        -------------------------
        Winner: Joe Biden
        Winning Vote Count: 408,576
        Winning Percentage: 52.5%
        -------------------------
- - - In this example I converted County to "State" and added a candidate "Joe Biden." We see that he won the election in Tennessee with 408,576 votes, and also won the election. He is our new President!
- - - ```
        Nickname Results for Tennessee
        -------------------------
        Total Votes: 778,287
        -------------------------

        Nickname Votes:
        "Where there are only two seasons.": 5.0% (38,855)

        "Just like Florida, but with no ocean.": 39.3% (306,055)

        "Death is here.": 3.2% (24,801)

        "Turn around for your own safety.": 52.5% (408,576)

        -------------------------
        Winner: "Turn around for your own safety."
        Winning Nickname Count: 408,576
        Winning Nickname Percentage: 52.5%
        -------------------------
- - - In this example, we see that there is a vote to choose a nickname for Tennessee. It looks like the winner is "Turn around for your own safety." This shows this code doesn't have to just be used for elections, but for anything that requires voting!
