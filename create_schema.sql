-- only for reference 

CREATE TABLE IF NOT EXISTS `Users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_name` VARCHAR(100) UNIQUE,
  `password` VARCHAR(100),
  `is_active` BOOLEAN,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME
);

CREATE TABLE IF NOT EXISTS `Surveys` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `title` VARCHAR(200) UNIQUE,
  `description` TEXT,
  `user_id` INTEGER,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME,
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
);

CREATE TABLE IF NOT EXISTS `Questions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `survey_id` INTEGER,
  `description` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME,
  FOREIGN KEY (`survey_id`) REFERENCES `Surveys` (`id`)
);

CREATE TABLE IF NOT EXISTS `Answers` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `question_id` INTEGER,
  `answer` BOOLEAN,
  `user_id` INTEGER,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME,
  FOREIGN KEY (`question_id`) REFERENCES `Questions` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
);

