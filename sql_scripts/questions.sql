CREATE TABLE IF NOT EXISTS `Questions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `survey_id` INTEGER,
  `description` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME,
  FOREIGN KEY (`survey_id`) REFERENCES `Surveys` (`id`)
);