package goose

import(

	
)

type Workspace struct {
	ID uint
	Topic string
}

workspace := Workspace{Topic: "Support Team"}
db.Crate(&workspace)

// ...
