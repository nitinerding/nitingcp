FROM golang:latest
ADD . /go/src/version2
RUN go install version2
WORKDIR /go/bin
ENV PORT 80
CMD ["./version2"]
