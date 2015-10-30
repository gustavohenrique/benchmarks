package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"log"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
	"runtime"
)

type Site struct {
	LongUrl  string `json:"longUrl" db:"long_url"`
	ShortUrl string `json:"shortUrl" db:"short_url"`
}

var db *sqlx.DB

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	var err error
	db, err = sqlx.Connect("postgres", "user=postgres dbname=benchmark password=root host=docker.postgres.local sslmode=disable")

	if err != nil {
		log.Fatal(err)
	}

	db.SetMaxOpenConns(10)

	http.HandleFunc("/hello", hello)
	http.HandleFunc("/", findAll)

	srv := &http.Server{
		Addr:    ":8080",
		Handler: nil,
	}
	srv.ListenAndServe()
}

func hello(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-type", "text/plain")
	fmt.Fprintf(w, "Hello World")
}

func findAll(w http.ResponseWriter, r *http.Request) {
	sites := []Site{}
	db.Query("SELECT long_url, short_url FROM urls", &sites)
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	// w.WriteHeader(200)
	json.NewEncoder(w).Encode(sites)
}
