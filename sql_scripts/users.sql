CREATE TABLE IF NOT EXISTS `Users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_name` VARCHAR(100) UNIQUE,
  `password` VARCHAR(100),
  `is_active` BOOLEAN,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME
);