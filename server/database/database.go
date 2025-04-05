package database

import (
	"server/models"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func ConnectDB() {
	db, err := gorm.Open(sqlite.Open("neds.db"), &gorm.Config{})
	if err != nil {
		panic("Не удалось подключиться к БД")
	}
	db.AutoMigrate(&models.User{})
	DB = db
}
