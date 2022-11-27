CREATE TABLE IF NOT EXISTS `Surveys` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `title` VARCHAR(200) UNIQUE,
  `description` TEXT,
  `user_id` INTEGER,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME,
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
);