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
