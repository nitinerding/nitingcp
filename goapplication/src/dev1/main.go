package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	host, _ := os.Hostname()
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello Nitin Rana, you've requested: %s\n", host)
	})

	http.ListenAndServe(":80", nil)
}
