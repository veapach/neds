package main

import (
	"server/database"

	"github.com/gin-gonic/gin"
)

func main() {
	database.ConnectDB()

	r := gin.Default()
	r.Run(":8080")
}
