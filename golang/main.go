package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"

    "github.com/gorilla/mux"

    "github.com/jmoiron/sqlx"
    _ "github.com/lib/pq"
)

type Site struct {
    LongUrl  string `json:"longUrl" db:"long_url"`
    ShortUrl string `json:"shortUrl" db:"short_url"`
}

func main() {
    db, _ = sqlx.Connect("postgres", "user=postgres dbname=benchmark password=root host=docker.postgres.local sslmode=disable")
    db.SetMaxOpenConns(5)

    router := mux.NewRouter().StrictSlash(true)
    router.
        Methods("GET").
        Path("/hello").
        Name("Hello").
        HandlerFunc(hello)

    router.
        Methods("GET").
        Path("/").
        Name("FindAll").
        HandlerFunc(findAll)

    http.ListenAndServe(":8080", router)
}

func hello(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-type", "text/plain")
    fmt.Fprintf(w, "Hello World")
}

func findAll(w http.ResponseWriter, r *http.Request) {
    sites := []Site{}
    db.Select(&sites, "SELECT long_url, short_url FROM urls")
    w.Header().Set("Content-Type", "application/json; charset=UTF-8")
    // w.WriteHeader(200)
    json.NewEncoder(w).Encode(sites)
}
