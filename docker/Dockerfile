FROM golang:1.16.2-alpine3.13 as builder
RUN apk add --no-cache git=2.30.2-r0
RUN go install github.com/sigstore/cosign/cmd/cosign@v0.5.0

FROM alpine:3.13.5
RUN apk add -u "python3=3.8.10-r0" && \
    mkdir /tmp/install && mkdir -p /atomworker && \
    wget -qO- "https://github.com/google/go-containerregistry/releases/download/v0.5.1/go-containerregistry_Linux_x86_64.tar.gz" | gunzip | tar xf - -C /tmp/install && \
    mv /tmp/install/crane /usr/local/bin && \
    wget -qO- "https://github.com/aquasecurity/trivy/releases/download/v0.18.3/trivy_0.18.3_Linux-64bit.tar.gz" | gunzip | tar xf - -C /tmp/install && \
    mv /tmp/install/trivy /usr/local/bin && \
    rm -Rf /tmp/install
ENV GITHUB_TOKEN=""
COPY --from=builder /go/bin/cosign /usr/local/bin
COPY *.py /atomworker
COPY franken /atomworker/franken

WORKDIR /atomworker
VOLUME ["/atomworker/conf", "/atomworker/auth", "/atomworker/output"]