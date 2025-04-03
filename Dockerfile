FROM jenkins/jenkins:lts

USER root

# 필수 도구 설치
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    git \
    curl wget unzip gnupg2 && \
    apt-get clean

# Chrome 설치
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Git, GitLab 플러그인 직접 설치
RUN jenkins-plugin-cli --plugins \
    git \
    gitlab-plugin \
    workflow-aggregator \
    credentials-binding

USER jenkins