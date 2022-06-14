# eyeson-video-call-tryout README

Christophe Lipautz - "Building a Video Meeting Platform from Scratch"

http://github.com/eyeson-team/workshop-video-platform

## dependencies

- go
- sqlite3
- eyeson - need API key - see https://eyeson-team.github.io/api/getting-started/

- fiber = https://docs.gofiber.io/

`go get github.com/gofiber/fiber/v2`

- gorm
https://gorm.io/index.html

`go get -u gorm.io/gorm`

- MailCatcher - a simple SMTP server for testing

- eyeson.js - the EyesOn JS API

## references

https://eyeson-team.github.io/api/getting-started/


- web sockets
- web hooks (a URL you provide that is called, when a given event happens...)
-- can be validated by signing by the shared secret that is the API key
- redirections (30x HTTP status code)

##  usage

```sh
make server
# go run cmd/server.go
```
