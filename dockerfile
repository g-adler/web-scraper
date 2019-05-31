FROM node:8.16.0-jessie-slim

WORKDIR /home

RUN npx create-react-app web-scraper \
  && rm -f src/*  \
  && apt update -y \
  && apt install -y python3

COPY scraper.py web-scraper/.
COPY Product.py web-scraper/.

RUN cd web-scraper

ENTRYPOINT ["yarn" "start"]
