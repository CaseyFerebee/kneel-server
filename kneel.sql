CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders` 
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)
);

CREATE TABLE `Sizes` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` REAL NOT NULL,
    `price` NUMERIC(5, 2) NOT NULL
);

CREATE TABLE `Styles` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` NUMERIC(5, 2) NOT NULL
);


INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12);
INSERT INTO `Metals` VALUES (null, "14k Gold", 400);
INSERT INTO `Metals` VALUES (null, "Palladium", 5000);
INSERT INTO `Metals` VALUES (null, "Platinum", 300);

INSERT INTO `Orders` VALUES (null, 1, 2, 2);
INSERT INTO `Orders` VALUES (null, 2, 1, 4);
INSERT INTO `Orders` VALUES (null, 3, 3, 5);

INSERT INTO `Sizes` VALUES (null, 0.5, 100.00);
INSERT INTO `Sizes` VALUES (null, 1.0, 150.00);
INSERT INTO `Sizes` VALUES (null, 2.0, 250.00);


INSERT INTO `Styles` VALUES (null, 'Classic', 50.00);
INSERT INTO `Styles` VALUES (null, 'Modern', 75.00);
INSERT INTO `Styles` VALUES (null, 'Vintage', 60.00);


Drop TABLE Styles