FROM socialmediamacroscope/sentiment_analysis:latest

RUN mkdir -p /scripts
WORKDIR /scripts

COPY ./SmmExtractor.py ./
COPY ./extractor_info.json ./
COPY ./requirement.txt ./extractor-requirement.txt

# Install pyClowder and any other python dependencies
RUN pip3 install --no-cache-dir -r ./extractor-requirement.txt -U

# Command to be run when container is run
# Can add heartbeat to change the refresh rate
CMD python3 SmmExtractor.py --heartbeat 300

ENV MAIN_SCRIPT="SmmExtractor.py" \
    CLOWDER_VERSION=1
