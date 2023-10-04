FROM ubuntu:20.04

# Timezone Configuration
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y    apt-utils \
                                    lsb-release \
                                    mesa-utils \
                                    gnupg2 \
                                    net-tools \
                                    iputils-ping \
                                    build-essential \
                                    wget \
                                    unzip \
                                    curl \
                                    git \
                                    mc \
                                    nano \
                                    ffmpeg \
                                    x11-apps

## GUI tunnel from docker
RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get install -y --no-install-recommends \
        libxau6 libxau6:i386 \
        libxdmcp6 libxdmcp6:i386 \
        libxcb1 libxcb1:i386 \
        libxext6 libxext6:i386 \
        libx11-6 libx11-6:i386 && \
    rm -rf /var/lib/apt/lists/*

RUN apt update &&  apt install -y make \
                                libssl-dev \
                                zlib1g-dev \
                                libbz2-dev \
                                libreadline-dev \
                                libsqlite3-dev \
                                llvm \
                                libncurses5-dev \
                                libncursesw5-dev \
                                xz-utils \
                                tk-dev \
                                libffi-dev \
                                liblzma-dev \
                                libgdbm-dev \
                                libnss3-dev \
                                libedit-dev \
                                libc6-dev \
                                cmake \
                                unzip \
                                autoconf \
                                autogen \
                                automake \
                                libtool \
                                mlocate

RUN apt update && apt install -y python3-pip python3-dev && pip3 install --upgrade setuptools pip
ENV DEBIAN_FRONTEND=noninteractive

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN apt update && apt install -y ros-noetic-desktop
RUN apt update && apt install -y python3-rosdep \
                                python3-rosinstall \
                                python3-rosinstall-generator \
                                python3-wstool \
                                build-essential 
                                
RUN pip3 install --ignore-installed requests \
                                    fastapi \
                                    uvicorn \
                                    flask \
                                    pymongo \
                                    pydantic \
                                    regex
RUN pip3 install pyqt5
RUN pip3 install pandas 
ENV PYTHONPATH "${PYTHONPATH}:/workspace/alpaca_logging_tools/"

RUN /bin/bash -c 'echo "source /opt/ros/noetic/setup.bash; source /workspace/ros_ws/devel/setup.bash --extend"  >> ~/.bashrc'
WORKDIR /workspace
# ENTRYPOINT /bin/bash -c 'source /opt/ros/noetic/setup.bash && cd /workspace/ros_ws && /bin/bash'