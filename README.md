# ADA Project Proposal - On the move for a good time!

**Team**

* Eric Bezzam
* Shiyue Nie
* Weiyu Zhang

**Abstract**

In this project, we would like to detect movement patterns within Switzerland, in particular event detection and identify popular destinations. To accomplish this task we will make use of geolocated tweets in the Swiss area. In a previous work, it has been shown that social media data can be exploited to extract urban movement patterns [1]. We would like to apply similar techniques to Switzerland as a whole. Some patterns that we are considering to analyze include:

1. _Highly concentrated activity due to an event (concert, show, festival, sporting event)_
2. _Concentrated activity at locations over time (or during the weekend / a particular season) due to a popular/touristic site_
3. _General social movement trends (e.g. where to friends meet up in the evening or during the weekend)_

The final goal of the project is to map out social movement patterns within Switzerland while showing the (hopefully) meaningful insight social media data can provide in such an analysis.

**Data Description**


**Feasibility and Risks**

During this project, we would have liked to identify general movement trends (such as the flow of frontaliers) but as the Swisscom data is not available we will tend towards identifying social activity from the provided Twitter data. This seems feasible as most users are probably not using Twitter to share/log their hourly or even daily motions but perhaps are more likely to post something when they are doing something "fun" or "unique" such as going out with friends, attending an event, or visiting an exciting place (we will try to find some concrete analysis/previous work to justify this for the final report!). Moreover, such tweets can be associated with a location (using the Twitter Search API [2]) and has been collected into a dataset that will be provided by the ADA course.

Although social media data is sparse (with regards to useable information), we are assuming that during the social activities/movements mentioned in the abstract, people are more likely to make a post. Below we have done a brief feasibility/risk analysis for each of the ideas. After working with data, we will be able to identify which tasks are more feasible for the final project.

1. _Highly concentrated activity due to an event_: we feel that this is the most feasible of the three as our main criteria for detecting an event is a high concentration of Twitter activity in a short amount of time and at a particular location. Moreover, if ":)" or ":(" were used as query operators for the data collected [2], it might also be possible to gauge the general sentiment of an event. Associating concentrated activity to an event has its risk since it relies on assumptions from us.
2. _Concentrated activity at locations over time due to a popular/touristic site_: This poses some risks as most of Switzerland's popular destinations are in the wilderness, where people (and certainly tourists) may not have internet connection. And as previously mentioned, it might to difficult to identify long term trends from solely social media data. 
3. _General social movement trends_: it is quite difficult to identify trends from solely Twitter data as it is quite sparse and it would not be correct to draw general conclusions if this is the case. Nonetheless, if we were to try to identify some sort of trend it might be easier for the evenings/weekends when people are free from work/school and more likely to be involved in social activity (and perhaps posting on Twitter). Moreover, such an analysis will probably be more applicable to urban environments, e.g. Zurich, Geneva, Basel, and Lausanne.

The feasibility and risks of this project will be better understood when the data has been provided. Perhaps there are not enough people represented in the data that use Twitter enough and that are using it in a meaningful manner for our analysis. It may be the case that we would need to collect more data from Twitter, SBB, Instagram, Facebook, and/or Flickr.


**Deliverables**

Leading up to our analysis, we will have also performed some data cleaning and wranling with Pandas in order to organize the provided dataset so that it can be conveniently used for our analysis.

Our final deliverable be in the form of an IPython notebook with appealing visualization(s). Possible ideas include:

1. Timeline of popular events + possible sentiment analysis;
2. Interactive map with some sort of indication (e.g. circle size) for amount of activity;
3. (If enough data), maps showing general movements in urban areas and a breakdown of which places people like to go to. 

Some tools we will consider for visualization include: Folium, Bokeh, geoplotlib, Plotly, and Seaborn.

If there is sufficient data for general trends during evenings/weekends, we would like to do some statistical modeling as was done in [1] for NYC. In this case, we would use scikit-learn and/or Tensorflow. 

An in-depth description of the data cleaning and statistical modeling will be provided in a report.

**Timeplan**



**References**
<br>
[1] "Extracting Urban Patterns from Location-based Social Networks" - http://www.agentgroup.unimore.it/Zambonelli/PDF/LBSN11.pdf
<br>
[2] Twitter Search API - https://dev.twitter.com/rest/public/search
