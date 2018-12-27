FROM golang
WORKDIR /go/src/dev1
ADD . /go/src/dev1
RUN go install dev1
ENV PORT 8081
CMD ["/go/bin/dev1"]
