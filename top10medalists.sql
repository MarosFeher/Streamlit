CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `top10_medailists` AS
    SELECT 
        `p`.`Player_name` AS `Athlete`,
        `s`.`sport_name` AS `Sport`,
        `pm`.`medals_sum` AS `Medals in Total`
    FROM
        (((`players_medals` `pm`
        JOIN `players` `p` ON ((`p`.`Player_ID` = `pm`.`player_id`)))
        JOIN `players_sports` `ps` ON ((`ps`.`player_id` = `pm`.`player_id`)))
        JOIN `sports` `s` ON ((`s`.`sport_ID` = `ps`.`sport_ID`)))
    ORDER BY `pm`.`medals_sum` DESC
    LIMIT 10