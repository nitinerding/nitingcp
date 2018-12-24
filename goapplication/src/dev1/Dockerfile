FROM golang
WORKDIR /go/src/nitin
ADD . /go/src/nitin
RUN go install nitin
ENV PORT 8080
CMD ["/go/bin/nitin"]
