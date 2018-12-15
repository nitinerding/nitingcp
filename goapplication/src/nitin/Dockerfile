FROM golang
ADD . /go/src/nitin
RUN go install nitin

FROM alpine:latest
COPY --from=0 /go/bin/nitin .
CMD ["./nitin"]
