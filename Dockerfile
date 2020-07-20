FROM nvidia/cuda:11.0-base-rc
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update \
    && apt-get install -y software-properties-common \
    && apt-get -y update \
    && add-apt-repository universe
RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip && apt-get -y install python3-tk

# Install python dependencies
RUN python3 -m pip install\
        Pillow \
        numpy

# Copy in files
COPY ./src .

# run
CMD ["python3", "juliasetGen.py"]
