# Big Data Processing Pipeline

Program was implemented using Python, Twitter API, Kafka, MongoDB, and Tableau. Refer the report for further implementation details:<br/>
<a href="https://github.com/chandnii7/Big-Data-Processing-Pipeline/blob/main/doc/projectReport.pdf">View Report</a>
<br/>

### Architecture<br/>
Overview:
* Twitter API is leveraged to obtain information to be processed
* Kafka takes the data and connects the various other components of this pipeline
* MongoDB stores the obtained tweets for later analysis 
* Tableau creates meaningful visualizations
<br/>
<img src="https://github.com/chandnii7/Big-Data-Processing-Pipeline/blob/main/images/architecture.jpg" height="300" width="800"/>
<br/>

### Results:
Upon examining the visualizations we see a relative concentration of tweets containing the COVID hashtag in the Americas, Europe, and Southern Asia, this seems to line up with expectations of areas that both have a high adoption of twitter and many Covid-19 cases.  Further work needs to be done to validate this conclusion though.
<br/>
<img src="https://github.com/chandnii7/Big-Data-Processing-Pipeline/blob/main/images/heatMap.jpg" height="300" width="500"/>
<br />
