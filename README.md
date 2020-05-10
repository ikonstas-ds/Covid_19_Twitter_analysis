# Covid_19_Twitter_analysis
Exploratory analysis and visualisation of tweets and Covid-19 related data. An [interactive dashboard](https://app.powerbi.com/view?r=eyJrIjoiMWI2YWI0YzItYzljYS00ZjA2LWE0NzctNzlhYzZmY2Q2ZWEzIiwidCI6IjBkZmQwNWIzLTdlYjEtNDAyZi1iYzM4LWJkZDU2NmQ3OGExMSIsImMiOjh9) is provided with insights about the socio-political and socio-economical impacts of Covid-19 and indications of various correlations between social media data and other Covid-19 related data. Submitted at [#EUvsVirus](https://www.euvsvirus.org/) Pan-European Hackathon.


# Process
Coronavirus outbreak is a significant problem that society faces. Communities all around the world are studying ways to tackle the virus. In the era of big data, a vast amount of information can be found on the Web about coronavirus, such as data catalogues, web portals, public repositories and social media. The scope of this project is to provide an interface for understanding the global and national socio-political and socio-economic impacts of Covid-19 and how all these aspects correlate together. To achieve this, we used a curated dataset provided by [panaceaLab](https://github.com/thepanacealab/covid19_twitter) that consists of almost 35 million tweets from 01/01/2020 until 22 of April and updates every two days. Due to the short duration of the hackathon, we have decided to collect a subset of 100,000 tweets per day leading to a dataset of 2.14 million tweets. In addition, we collected data regarding Covid-19 national cases and deaths, stock market indices, governmental measures and mobility measures provided by Google.

After cleaning the data, to calculate the sentiment polarity we used AllenNLP which is an open-source NLP research library and provides pretrained models. We used the model RoBERTa which is trained on the Stanford Sentiment Treebank dataset. The script is written in Python programming language and was executed in Google Colaboratory. Having obtained the needed dataset we used Microsoft Power BI to visualise the data and provide an interactive dashboard for better flexibility and understanding for the end-user.

The main challenge of our work was to obtain the needed data during the 48-hour hackathon, as it required most of our time. Furthermore, the majority of the tweets do not contain geotagged data, which made it difficult to analyse the sentiment polarity based on each country.

This hackathon was a very fruitful experience for our team. It gave us the opportunity to join the community and contribute to combating the coronavirus outbreak and provide useful information.


# Data
<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Description</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Covid-19 Tweets</td>
      <td>Covid-19 Twitter chatter dataset for scientific use</td>
      <td>https://github.com/thepanacealab/covid19_twitter</td>
    </tr>
    <tr>
      <td>Google mobility</td>
      <td>Google mobility data</td>
      <td>https://www.google.com/covid19/mobility/</td>
    </tr>
    <tr>
      <td>Governmental measures</td>
      <td>Governmental measures per country during the coronavirus outbreak</td>
      <td>https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker</td>
    </tr>
    <tr>
      <td>Covid-19 cases-deaths</td>
      <td>Daily updated data on the geographic distribution of COVID-19 cases worldwide</td>
      <td>https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide</td>
    </tr>
  </tbody>
</table>
