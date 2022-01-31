CREATE TABLE chrome_history(
	history_id 			SERIAL 						PRIMARY KEY,
	demand				VARCHAR(64)					NOT NULL,
	is_downloaded 		BOOLEAN						NOT NULL,
	download_count 		INT							NULL,
	search_time			TIMESTAMP		UNIQUE		NOT NULL
);

CREATE TABLE price_comparison(
	product_id 				SERIAL				PRIMARY KEY,
	product_name			VARCHAR(250)		NOT NULL,
	high_product_price		MONEY				NOT NULL,
	high_shipping			MONEY				NOT NULL,
	low_product_price		MONEY				NOT NULL,
	low_shipping			MONEY				NOT NULL,
	high_eshop				VARCHAR(250)		NOT NULL,
	low_eshop				VARCHAR(250)		NOT NULL
);

DROP TABLE IF EXISTS chrome_history
DROP TABLE price_comparison


SELECT * FROM chrome_history