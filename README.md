# ADA_Project

**Abstract**

From geolocalized Twitter data, we would like to perform event detection and identify popular touristic destinations. From these findings, we would like to determine whether or not there are sufficient conditions to reach these events / touristic destinations.

Data Description

Geolocated Twitter data
Swiss public transport API
SBB Data

**Feasibility and Risks**

There is risk that we are not able to gather enough information from the Twitter information. One challenge will be figuring out how to determine there is an event. The simplest manner would be detect a high frequency of tweets at a certain time and at a certain place. We might need to cross-reference a detected date and location to an event by scraping data additional data from the internet. Another way to detect an event would be to see if the same pattern occurs roughly a year later and in the same place. 

Working between three different APIs and datasets poses the problem of how data is entered as different tools might have different names and standards for things such as the names of places.

**Deliverables**

As a deliverable we will have a table listing detected events and popular touristic locations along with the estimated attendance from tweets and some indications of the number of connections to that event or location. Sometimes there are increased connections due to the occurrence of an event.

We will also try to create some interactive visualisation with Bokeh and perhaps with a map.

**Timeplan**

When we get hold of the Twitter data, we will first need to see what we have available. We might want to sort the tweets by location and within location by date (perhaps aggregate into weeks). This basic processing will give us a general overview of much data we have per region and how it is spread across time.
