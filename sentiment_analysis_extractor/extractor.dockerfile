FROM socialmediamacroscope/sentiment_analysis:latest

RUN mkdir -p /scripts
WORKDIR /scripts

COPY ./SmmExtractor.py ./
COPY ./extractor_info.json ./

# Install pyClowder and any other python dependencies
RUN pip install --no-cache-dir -r ../requirement.txt

# Command to be run when container is run
# Can add heartbeat to change the refresh rate
CMD python3 SmmExtractor.py --heartbeat 40

ENV MAIN_SCRIPT="SmmExtractor.py" \
    CLOWDER_VERSION=1
