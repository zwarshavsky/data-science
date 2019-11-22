Saltiest Hacker News Trolls Product Vision Document
Proposal

What problem does your app solve?
Finding and ranking the saltiest comments from trolls on HackerNews
Be as specific as possible; how does your app solve the problem?B
By aggregating the comments of trolls and ranking them through ‘saltiness’ analysis the app will be able to display the comments of the trolliest users and allow the user to search through their recent comments
What is the mission statement?
Hacker News Saltiest Trolls strives to rank the most active users by level of saltiness for the entertainment purposes of HackerNews users.
Features

What features are required for your minimum viable product?
UI- Marketing page with a detailed description of the app with a call to action prompt for the app, about page with bios of the team. 
Front-End- User-onboarding, feed of negative comments from the saltiest trolls on HackerNews, save their favorite comments and delete them, utilizing time-stamps, usernames, & index of salty troll-rank *stretch* search by troll username to find user comments
Back-end- Utilize query language to pull ‘salty troll data’ to the app from the aggregator
DS- Provide an accessible JSON userlist from the HackerNews API 
What features may you wish to put in a future release?


Sarcasm meter, humor level, meanness
What do the top 3 similar apps do for their users?
reddit-user-analyzer

Frameworks - Libraries

What 3rd party frameworks/libraries are you considering using?
axios , Formik, Yup, Styled-Components, React, React-Router, Material UI


Do APIs require you to contact its maintainer to gain access?
no


Are you required to pay to use the API?
no


Have you considered using Apple Frameworks? (MapKit, Healthkit, ARKit?)
no


For Data Scientists

Describe the Established data source with at least rough data able to be provided on day 1.
HackerNews API data source JSON


You can gather information about the data set you’ll be working with from the project description. Be sure to collaborate with your PM, and your Backend Architect to chat about the resources you have.


Write a description for what the DS problem is (what uncertainty/prediction are we trying to do here? Sentiment analysis? Why is this a useful solution to a problem?
Predicting the negativity of user comments, this is useful because the app will reliably tell you the negativity ranking of another user without actually skimming through every comment  and interpreting from there


A target (e.g. JSON format or such) for output that DS students can deliver to web/other students for them to ingest and use in the app
JSON


Target Audience

Who is your target audience? Be specific.
HackerNews users, from about age 20-40 who are in the fields of programming and development, typically male




