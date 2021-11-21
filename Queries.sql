 -- Query1
select ratings.movieId,movies.title,count(*) As countNumber
from [dbo].[ratings] join dbo.movies on ratings.movieId=movies.movieId
group by ratings.movieId,movies.title
having count(*)>50 
Order By countNumber DESC

-- Query2
select Years,MAX(Rate) As MaxRating,MAX(title) As title
from (
Select Years.YearMovie As Years,movies.title As title,Count(*) As Rate
from Years join movies on movies.movieId = Years.movieId
		join ratings on movies.movieId = ratings.movieId
group by Years.YearMovie,ratings.movieId,movies.title
)AS Table_Count
group by Table_Count.Years
Order by Table_Count.Years
-- Query3
select title,genres,AVG(rating) As AvgRating
from movies join ratings on movies.movieId = ratings.movieId
where genres like '%Adventure%'
group by movies.movieId,title,genres
having AVG(rating)>3
-- Query4
Go 
declare @AvgAfter decimal(5,2);
set @AvgAfter=(
select AVG(AvgRating) from ViewAfter2005Average)

declare @AvgBefore decimal(5,2);
set @AvgBefore=(
select Avg(AvgRating) from ViewBefore2005Average)

select Abs(@AvgAfter-@AvgBefore)
Go
-- Query 5
select Distinct userId
from ratings rate
where Not  EXISTS ( 
select * from ratings as r where Not rate.rating=r.rating and rate.userId=r.userId);
-- Query6
select mo.title , tg4.tag , tg4.number
from(
  select tg3.tag , COUNT(*) as number , tg3.movieId
  from(
    select tags.tag as tag , tg.movieId as movieId
    from(
      select sc.tagId as tagId , sc.movieId as movieId
      from scores as sc
      where not EXISTS (select * 
          from scores as sc2
          where sc.movieId=sc2.movieId and sc.relevance<sc2.relevance)) as tg ,
      tags inner join [tags-relevance] on tags.tag=[tags-relevance].tag
      where tags.movieId=tg.movieId and [tags-relevance].tagId=tg.tagId) as tg3
  group by tg3.movieId,tg3.tag)as tg4 inner join movies as mo on mo.movieId=tg4.movieId;