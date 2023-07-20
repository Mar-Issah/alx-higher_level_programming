-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS "rating" FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY SUM(tv_show_ratings.rate) DESC
;
