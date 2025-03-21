movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def get_ratings(name):
    for movie in movies:
        if movie["name"] == name:
            if movie["imdb"] > 5.5:
                return True
            else:
                return False
            
#2
def sublist_5_5():
    score_above_5_5 = []
    for m in movies:
        if m['imdb'] > 5.5:
            score_above_5_5.append(m['name'])
    return score_above_5_5
print(sublist_5_5())

#3
def category_list(category):
    category_movie = []
    for m in movies:
        if m['category'] == category:
            category_movie.append(m['name'])
    return category_movie
print(category_list('Romance'))

#4
def computes_average():
    sum = 0
    count = len(movies)
    for m in movies:
        sum += m['imdb']
    return sum/count
print(round(computes_average(), 2))

#5
def category_computes_average(category):
    sum_category_movie = 0
    for m in movies:
        if m['category'] == category:
            sum_category_movie += m['imdb']
    return sum_category_movie/len(category_list(category))
print(category_computes_average('Romance'))