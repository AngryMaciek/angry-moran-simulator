##### BASE IMAGE #####
FROM python:3.7.4-slim

##### METADATA #####
LABEL base.image="python:3.7.4-slim"
LABEL software="moranpycess"
LABEL software.description="Python framework for Moran Processes driven by game theory"
LABEL software.website="https://github.com/AngryMaciek/angry-moran-simulator"
LABEL software.documentation="https://github.com/AngryMaciek/angry-moran-simulator"
LABEL software.license="https://github.com/AngryMaciek/angry-moran-simulator/blob/master/LICENSE"
LABEL software.tags="Bioinformatcs"
LABEL maintainer="wsciekly.maciek@gmail.com"

COPY . .

##### INSTALL AND TEST-IMPORT #####
RUN pip install --upgrade pip \
  && python -m pip install . \
  && python -c 'import moranpycess'
