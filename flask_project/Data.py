import pyodbc


conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MATINB;"
                      "Database=First Project;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()
def Query1():

    cursor.execute(
        'select ratings.movieId,movies.title,count(*) As countNumber '
        'from [dbo].[ratings] join dbo.movies on ratings.movieId=movies.movieId '
        'group by ratings.movieId,movies.title '
        'having count(*)>50 '
        'Order By countNumber DESC');

    return cursor;

def Query2():
    cursor.execute('select Years,MAX(Rate) As MaxRating,MAX(title) As title '
                   'from (Select Years.YearMovie As Years,movies.title As title,Count(*) As Rate '
                   'from Years '
                   'join movies on movies.movieId = Years.movieId '
                   'join ratings on movies.movieId = ratings.movieId '
                   'group by Years.YearMovie,ratings.movieId,movies.title)AS Table_Count '
                   'group by Table_Count.Years Order by Table_Count.Years');

    return cursor;
def Query3(genres):
    statement = "select title,genres,AVG(rating) As AvgRating from movies join ratings on movies.movieId = ratings.movieId where genres like '%47%' group by movies.movieId,title,genres having AVG(rating)>3";
    statement = statement.replace("47", genres)
    cursor.execute(statement);
    return cursor;
def Query4():
    cursor.execute('select dbo.Func1_Query4() as Number;');
    return cursor;
def Query5():
    cursor.execute("select Distinct userId from ratings rate where Not  EXISTS (select * from ratings as r where Not rate.rating=r.rating and rate.userId=r.userId);");
    return cursor;
def Query6():
    cursor.execute('select mo.title , tg4.tag , tg4.number from(select tg3.tag , COUNT(*) as number , tg3.movieId from(select tags.tag as tag , tg.movieId as movieId from(select sc.tagId as tagId , sc.movieId as movieId from scores as sc where not EXISTS (select * from scores as sc2 where sc.movieId=sc2.movieId and sc.relevance<sc2.relevance)) as tg ,tags inner join [tags-relevance] on tags.tag=[tags-relevance].tag where tags.movieId=tg.movieId and [tags-relevance].tagId=tg.tagId) as tg3 group by tg3.movieId,tg3.tag)as tg4 inner join movies as mo on mo.movieId=tg4.movieId;');
    return cursor;