#
# Good references:
# https://denibertovic.com/posts/handling-permissions-with-docker-volumes/
# https://askubuntu.com/questions/1457726/how-and-where-to-install-conda-to-be-accessible-to-all-users
# https://www.fromlatest.io
#
# ~AngryMaciek

##### BASE IMAGE #####
FROM bitnami/minideb:bullseye
# INFO: https://github.com/bitnami/minideb

##### METADATA #####
LABEL base.image="bitnami/minideb:bullseye"
LABEL version="2.0.0"
LABEL software="moranpycess"
LABEL software.description="Python framework for Moran Processes driven by game theory"
LABEL software.documentation="https://github.com/AngryMaciek/angry-moran-simulator"
LABEL software.website="https://github.com/AngryMaciek/angry-moran-simulator"
LABEL software.license="MIT"
LABEL software.tags="Bioinformatcs"
LABEL maintainer="Maciek Bak"
LABEL maintainer.email="wsciekly.maciek@gmail.com"

##### INSTALL SYSTEM-LEVEL DEPENDENCIES #####
RUN install_packages curl ca-certificates gnupg2 git gosu

##### DEFINE BUILD VARIABLES #####
ARG MAMBADIR="/mambaforge"
ARG CONDABINDIR="/mambaforge/bin"
ARG MAMBAURL="https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh"

##### SET ENVIROMENTAL VARIABLES #####
ENV LANG C.UTF-8

##### INSTALL MAMBAFORGE #####
RUN /bin/bash -c "curl -L ${MAMBAURL} > mambaforge.sh \
    && bash mambaforge.sh -b -p ${MAMBADIR} \
    && ${CONDABINDIR}/conda config --system --set channel_priority strict \
    && source ${CONDABINDIR}/activate \
    && conda init bash \
    && rm -f mambaforge.sh"

##### BUILD DEV ENV #####
COPY environment.yml .
RUN /bin/bash -c "${CONDABINDIR}/mamba install conda-build boa conda-verify -c conda-forge --yes \
  && ${CONDABINDIR}/mamba env create --file environment.yml \
  && ${CONDABINDIR}/conda clean --all --yes \
  && rm -f environment.yml"

##### EXPOSE PORTS #####
EXPOSE 8888

##### PREPARE WORKING DIRECTORY #####
VOLUME /moranpycess
WORKDIR /moranpycess

##### SETUP ENTRYPOINT #####
COPY entrypoint.sh /bin/entrypoint.sh
RUN /bin/bash -c "chmod +x /bin/entrypoint.sh \
  && groupadd conda \
  && chgrp -R conda ${MAMBADIR} \
  && chmod 770 -R ${MAMBADIR}"
ENTRYPOINT ["/bin/entrypoint.sh"]
CMD ["/bin/bash"]
