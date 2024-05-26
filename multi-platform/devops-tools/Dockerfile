FROM --platform=${TARGETPLATFORM} python:slim

# Tools Versions
ARG  HELM_VER=v3.15.0
ARG  TRFM_VER=1.8.3
ARG  K8CL_VER=v1.30.1

# Builder Arguments
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH 

# check Buidler Shell   
SHELL ["/bin/bash", "-c"]

RUN apt-get update; \
    apt-get install -y curl wget unzip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install ansible

# Terraform Install
RUN curl -L "https://releases.hashicorp.com/terraform/${TRFM_VER}/terraform_${TRFM_VER}_${TARGETOS}_${TARGETARCH}.zip" -o terraform.zip
RUN curl -LO "https://releases.hashicorp.com/terraform/${TRFM_VER}/terraform_${TRFM_VER}_SHA256SUMS"
RUN unzip terraform.zip
RUN install -o root -g root -m 0755 terraform /usr/local/bin/terraform

# Get latest kubectl
RUN curl -LO "https://dl.k8s.io/release/${K8CL_VER}/bin/${TARGETPLATFORM}/kubectl"
RUN curl -LO "https://dl.k8s.io/release/${K8CL_VER}/bin/${TARGETPLATFORM}/kubectl.sha256"
# Install helm
RUN curl -LO https://get.helm.sh/helm-${HELM_VER}-${TARGETOS}-${TARGETARCH}.tar.gz  && \
tar -zxvf helm-${HELM_VER}-${TARGETOS}-${TARGETARCH}.tar.gz && \
mv ${TARGETOS}-${TARGETARCH}/helm /usr/local/bin/helm

# Install AWS Client
RUN export AWSARCH=$(echo "${TARGETARCH}" | sed 's#arm#aarch#;s#amd#x86_#'); \
    curl https://awscli.amazonaws.com/awscli-exe-${TARGETOS}-${AWSARCH}.zip -o awscliv2.zip && \
    unzip awscliv2.zip && \
    ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update && \
    rm -rf ./aws

CMD [/bin/bash]
