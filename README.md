# smm-extractor
This repo includes a few popular [Social Media Macroscope Extractors](https://smm.ncsa.illinois.edu/) such as 
Sentiment Analysis, Network Visualization, Text Preprocessing, Topic Modeling, Name Entity Recognition, and etc.

## Build
To build Clowder SMM extractors, make sure to use the correct dockerfile in each of the extractor folder (**extractor.
dockerfile**). 
* Note you can also build SMM extractor (**dockerfile**) that is being used independently of Clowder but on the 
  SMM system.

Some of the useful command:

Build
```angular2html
docker build -f extractor.dockerfile -t socialmediamacroscope/network_analysis_extractor:latest .
```

Push
```angular2html
docker push socialmediamacroscope/network_analysis_extractor:latest
```

## Deploy
For how to deploy Clowder extractors please refer to the official [Documentation](https://clowder-framework. readthedocs.io/en/latest/develop/extractors.html#.)

You can access the latest pre-built SMM extractors on docker.io:

[socialmediamacroscope/sentiment_analysis_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/sentiment_analysis_extractor/general)
[socialmediamacroscope/topic_modeling_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/topic_modeling_extractor/general)
[socialmediamacroscope/network_analysis_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/network_analysis_extractor/general)
[socialmediamacroscope/preprocessing_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/preprocessing_extractor/general)
[socialmediamacroscope/name_entity_recognition_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/name_entity_recognition_extractor/general)
[socialmediamacroscope/autophrase_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/autophrase_extractor/general)

To include those extractors with docker-compose:
```
  smm-sentiment:
    image: socialmediamacroscope/sentiment_analysis_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  smm-preprocessing:
    image: socialmediamacroscope/preprocessing_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  name-entity-recognition:
    image: socialmediamacroscope/name_entity_recognition_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  network-analysis:
    image: socialmediamacroscope/network_analysis_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  topic-modeling:
    image: socialmediamacroscope/topic_modeling_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}
```


## Submit file to extractors
# smm-extractor
This repo includes a few popular [Social Media Macroscope Extractors](https://smm.ncsa.illinois.edu/) such as 
Sentiment Analysis, Network Visualization, Text Preprocessing, Topic Modeling, Name Entity Recognition, and etc.

## Build
To build Clowder SMM extractors, make sure to use the correct dockerfile in each of the extractor folder (**extractor.
dockerfile**). 
* Note you can also build SMM extractor (**dockerfile**) that is being used independently of Clowder but on the 
  SMM system.

Some of the useful command:

Build
```angular2html
docker build -f extractor.dockerfile -t socialmediamacroscope/network_analysis_extractor:latest .
```

Push
```angular2html
docker push socialmediamacroscope/network_analysis_extractor:latest
```

## Deploy
For how to deploy Clowder extractors please refer to the official [Documentation](https://clowder-framework. readthedocs.io/en/latest/develop/extractors.html#.)

You can access the latest pre-built SMM extractors on docker.io:

[socialmediamacroscope/sentiment_analysis_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/sentiment_analysis_extractor/general)
[socialmediamacroscope/topic_modeling_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/topic_modeling_extractor/general)
[socialmediamacroscope/network_analysis_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/network_analysis_extractor/general)
[socialmediamacroscope/preprocessing_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/preprocessing_extractor/general)
[socialmediamacroscope/name_entity_recognition_extractor](https://hub.docker.com/repository/docker/socialmediamacroscope/name_entity_recognition_extractor/general)

To include those extractors with docker-compose:
```
  smm-sentiment:
    image: socialmediamacroscope/sentiment_analysis_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  smm-preprocessing:
    image: socialmediamacroscope/preprocessing_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  name-entity-recognition:
    image: socialmediamacroscope/name_entity_recognition_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  network-analysis:
    image: socialmediamacroscope/network_analysis_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}

  topic-modeling:
    image: socialmediamacroscope/topic_modeling_extractor:latest
    restart: unless-stopped
    networks:
      - clowder
    depends_on:
      - rabbitmq
      - clowder
    environment:
      - RABBITMQ_URI=${RABBITMQ_URI:-amqp://guest:guest@rabbitmq/%2F}
```
