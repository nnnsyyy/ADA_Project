# ADA Project Proposal - On the move for a good time!

## Team

* Eric Bezzam ([@ebezzam](https://github.com/ebezzam/))
* Shiyue Nie ([@nnnsyyy](https://github.com/nnnsyyy))
* Weiyu Zhang ([@BeforeRain](https://github.com/BeforeRain/))

## Abstract

In this project, we would like to detect movement patterns within Switzerland, in particular event detection and identify popular destinations. To accomplish this task we will make use of geolocated tweets in the Swiss area. In a previous work, it has been shown that social media data can be exploited to extract urban movement patterns [1]. We would like to apply similar techniques to Switzerland as a whole. Some patterns that we are considering to analyze include:

1. _Highly concentrated activity due to an event (concert, show, festival, sporting event)_
2. _Concentrated activity at locations over time (or during the weekend / a particular season) due to a popular/touristic site_
3. _General social movement trends (e.g. where do friends meet up in the evening or during the weekend)_

The final goal of the project is to map out social movement patterns within Switzerland while showing the (hopefully) meaningful insight social media data can provide in such an analysis.

## Data Description
In this project, we will use geolocated tweets as our main dataset, identifying mobility patterns and detecting events from them. To further explore these patterns and events, we may use Swiss public transport data to conduct spatial and temporal analysis. 

- **Geolocated Tweets**   

The ADA staff will provide us with a dataset of geolocated tweets in the Swiss area starting from 2012. The dataset is collected using the Twitter API. For every [tweet object](https://dev.twitter.com/overview/api/tweets), we can obtain its user, text, geo-location, time, etc. The following table describes these fields: 


| Field | Type | Description |
| ----- | ----- | ----------- |
| user | Users | The user who posted this Tweet |
| text | String | The actual UTF-8 text of the status update |
| coordinates | Collection of Float | The longitude and latitude of the Tweet’s location, as an collection in the form of [longitude, latitude] |
| created_at | String | UTC time when this Tweet was created |

We will have a better understanding of the dataset after we get access to it. In case the provided dataset is insufficient, we will scrape more data using [Twitter REST API](https://dev.twitter.com/rest/public).


- [Swiss Public Transport API](https://transport.opendata.ch/docs.html)  

The Transport API allows scraping public transport data within Switzerland. With that API, we can obtain available connections for given departure and arrival stations. Thus, we can analyze the relationship between mobility patterns and the number of connections over time.

- [SBB OpenData](http://www.sbb.ch/en/group/the-company/facts-and-figures/open-data.html)  

SBB(Swiss federal railways) provides open data and APIs for stations and traffic, which could be useful for further analysis of mobility patterns and detected events.


## Feasibility and Risks

During this project, we would have liked to identify general movement trends (such as the flow of frontaliers) but as the Swisscom data is not available we will tend towards identifying social activity from the provided Twitter data. This seems feasible as most users are probably not using Twitter to share/log their hourly or even daily motions but perhaps are more likely to post something when they are doing something "fun" or "unique" such as going out with friends, attending an event, or visiting an exciting place (we will try to find some concrete analysis/previous work to justify this for the final report!).

Although social media data is sparse (with regards to useable information), we are assuming that during the social activities/movements mentioned in the abstract, people are more likely to make a post. Below we have done a brief feasibility/risk analysis for each of the ideas. After working with the data, we will be able to identify which tasks are more feasible for the final project.

1. _Highly concentrated activity due to an event_: We feel that this is the most feasible of the three as our main criteria for detecting an event is a high concentration of Twitter activity in a short amount of time and at a particular location. Moreover, if ":)" or ":(" were used as query operators for the data collected [2], it might also be possible to gauge the general sentiment of an event. Associating concentrated activity to an event has its risk since it relies on assumptions from us about what the event could be.
2. _Concentrated activity at locations over time due to a popular/touristic site_: This poses some risks as most of Switzerland's popular destinations are in the wilderness, where people (and certainly tourists) may not have internet connection. Moreover, it might be difficult to identify long term trends from solely social media data. 
3. _General social movement trends_: As previously mentioned, it is quite difficult to identify trends from solely Twitter data as it is quite sparse and it would not be correct to draw general conclusions if this is the case. Nonetheless, if we were to try to identify some sort of trend it might be easier for the evenings/weekends when people are free from work/school and more likely to be involved in social activity (and perhaps posting on Twitter). Moreover, such an analysis will probably be more applicable to urban environments, e.g. Zurich, Geneva, Basel, and Lausanne.

The feasibility and risks of this project will be better understood when the data has been provided. Perhaps there are not enough people represented in the data that use Twitter enough and that are using it in a meaningful manner for our analysis. It may be the case that we would need to collect more data from Twitter, SBB, Instagram, Facebook, and/or Flickr.


## Deliverables

Leading up to our analysis, we will have also performed some data cleaning and wranling with Pandas in order to organize the provided dataset so that it can be conveniently used for our analysis.

Our final deliverable will be in the form of an IPython notebook with appealing visualization(s). Possible ideas include:

1. Timeline of popular events + possible sentiment analysis;
2. Interactive map with some sort of indication (e.g. circle size) for amount of activity;
3. (If enough data), maps showing general movements in urban areas and a breakdown of which places people like to go to. 

Some tools we will consider for visualization include: Folium, Bokeh, Plotly, and Seaborn.

If we are able to obtain sufficient data for general trends, we would like to do some statistical modeling as was done in [1] for NYC. In this case, we would use scikit-learn and/or Tensorflow. 

An in-depth description of the data cleaning and statistical modeling will be provided in a report.

## Timeplan

1. Preparation(2 weeks): 

  - Data cleaning: Check all attributes of the available Twitter data to see which features we have/need (e.g. location, time, topic/key words etc.). Ensure the formats of useful features and then generate precise testing data. Sorting data by time(especially weekends and holidays). 
  - Research: Study existing papers or programs relevant to located data analysis or social media data analysis. Choose the appropriate methodology with some useful models and algorithms which may be suitable to our project.
  
2. Testing(2 weeks):

  - Model selection: Design tentative models and make some analysis. Figure out theirs pros and cons.
  - Further research: Comparing to different references and our tentative models, optimize the algorithms.
  - Data refresh: If needed, we will do some data scraping for supplement.
  
3. Preliminary analysis(1-2 weeks):

  - Specific results: Accomplish part of setting goals, like finding some movement trends or activities/events.
  - Visualization study: Apply some viz methods to the results.
  
4. Integrating(2-3 weeks):

  - Model modifying: Modularize the codes(e.g. packing functions) which achieve general result.
  - Visualization realisation: Display the event analysis on map.
  - Verification and validation: Make sure methods can be used in all cases after modifying.
  
5. Conclusion(1-2 weeks):

  - Log sorting: Review all records from the beginning. Draw the whole process and list some important progress (e.g. problem found and solved, function implementation).
  - Improvement: If time permitted, improve the readability of results (e.g. suggestions and visualization).
  - Report writing and symposium.


## References
<br>
[1] "Extracting Urban Patterns from Location-based Social Networks" - http://www.agentgroup.unimore.it/Zambonelli/PDF/LBSN11.pdf
<br>
[2] Twitter Search API - https://dev.twitter.com/rest/public/search

