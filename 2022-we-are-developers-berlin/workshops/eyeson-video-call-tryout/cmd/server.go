package main

import "fmt"
import "fiber"

func main() {
	fmt.Println("hello!")
	port := 8077
	app := fiber.New(fiber.Config{})
	app.Get("/hello", func (c *fiber.Ctx) error {
		// xxx
		return c.SendString("hello world!\n")
	})

	fmt.Printf("Starting server on port %d", port)
	err := app.Listen(fmt.Sprintf("%d", port))

	if err != null {
		log.Fatal(err)
	}
}