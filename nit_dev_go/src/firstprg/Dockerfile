FROM golang:latest
ADD . /go/src/firstprg
RUN go install firstprg
WORKDIR /go/bin
ENV PORT 80
CMD ["./firstprg"]
