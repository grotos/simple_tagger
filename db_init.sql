CREATE TABLE active_learning (phrase TEXT NOT NULL, type TEXT, intent TEXT NOT NULL, is_ok TEXT, final_tag TEXT);

INSERT INTO active_learning (phrase, type, intent) VALUES ('kim jesteś','check','faq_1');
INSERT INTO active_learning (phrase, type, intent) VALUES ('co słychać','tag','{"halo":0.9, "co_slychac":0.7}');
INSERT INTO active_learning (phrase, type, intent) VALUES ('zrób przelew','tag','{"przelew_zwykly":0.9, "przelew_ogolny":0.9}');
INSERT INTO active_learning (phrase, type, intent) VALUES ('co słychać bola','check','faq_21');
INSERT INTO active_learning (phrase, type, intent) VALUES ('co słychać kola','check','faq_2');
INSERT INTO active_learning (phrase, type, intent) VALUES ('co słychać fdss ','check','faq_2');
INSERT INTO active_learning (phrase, type, intent) VALUES ('co słychać jhfadsf','check','faq_23');
INSERT INTO active_learning (phrase, type, intent) VALUES ('co słychać u ciebie','check','faq_6_alo');