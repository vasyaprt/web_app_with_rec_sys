# Recommendation Algorithm
import pandas as pd
from .models import Tour, Rating, Order, Views
from django.db.models import Case, When

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_similar(tittle,rating,corrMatrix, Middle):
    similar_ratings = corrMatrix[tittle]*(rating-2.5) #находим коэффиценты отношений оцененных экскурсии и остальных
    similar_ratings = similar_ratings.sort_values(ascending=False)# сортировка полученного списка
    return similar_ratings

def get_recommend(request, tour_id):

    tour_rating = pd.DataFrame(list(Rating.objects.all().values())) #перенос данных из бд


    userRatings = tour_rating.pivot_table(index=['user_id'], columns=['tour_id'], values='rating')# матрица рейтингов
    userRatings = userRatings.fillna(0, axis=1) # заполнение пустых ячеек нулями
    corrMatrix = userRatings.corr(method='pearson') #корреляция item-item??

    user = pd.DataFrame(list(Rating.objects.filter(user=request.user).values())).drop(['user_id', 'id'], axis=1) # поиск всех оценок пользователя
    user_filtered = [tuple(x) for x in user.values] #преобразование оценок [(tour_id, оценка)]
    tour_id_ordered = [each[0] for each in user_filtered] #отделение id экскурсий


    midl_rating_list_object=list(Rating.objects.filter(user=request.user).values('rating'))
    midl_rating_list = [k['rating'] for k in midl_rating_list_object]
    midl_rating=sum(midl_rating_list)/len(midl_rating_list)

    similar_tours = pd.DataFrame()
    for tour, rating in user_filtered:
        similar_tours = similar_tours.append(get_similar(tour, rating, corrMatrix, midl_rating), ignore_index=True)#матрица коэффицентов для туров оценненых пользователем

    tours_id = list(similar_tours.sum().sort_values(ascending=False).index)
    tours_id_recommend = [each for each in tours_id if each not in tour_id_ordered]
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(tours_id_recommend)])
    tour_list = list(Tour.objects.filter(id__in=tours_id_recommend).order_by(preserved)[:4])
    tour_name = Tour.objects.get(id=tour_id)
    k = 0
    while k < len(tour_list):
        c = tour_list[k]
        if ( c == tour_name):
            del tour_list[k]
        else:
            k += 1
    tour_list=tour_list[:3]
    return tour_list


def get_sim(tour_id, count):
    df = pd.DataFrame(list(Tour.objects.all().values()))

    imp_features=[]
    for i in range(0, df.shape[0]):
        imp_features.append(df['title'][i]+' '+df['description'][i]+' '+df['type'][i]+' '+str(df['price'][i]))


    df['for_rec']=imp_features
    new_id = [i for i in range(len(df))]
    df['new_id']=new_id


    cm= CountVectorizer().fit_transform(df['for_rec'])
    cs= cosine_similarity(cm)

    tour=df[df.id==tour_id]['new_id'].values[0]
    scores= list(enumerate(cs[tour]))
    sorted_scores=sorted(scores, key=lambda x:x[1], reverse=True)
    sorted_scores=sorted_scores[1:]
    tour_sim_list = [i[0]+5 for i in sorted_scores]
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(tour_sim_list)])
    tour_list=list(Tour.objects.filter(id__in=tour_sim_list).order_by(preserved)[:count])

    return tour_list

def get_sviews(tour_id, request):
    tours=list(Views.objects.filter(user=request.user).values('tour_id').order_by('-id'))
    tour_ids = [k['tour_id'] for k in tours]

    tour_name = Tour.objects.get(id=tour_id)

    tour_list= get_sim(tour_id,4)
    for i in tour_ids[:3]:
        tour_list=tour_list+(get_sim(i, 1))


    k=0
    while k < len(tour_list):
        c = tour_list[k]
        if((tour_list.count(c)>1) | (c==tour_name) ):
            del tour_list[k]
        else:
            k += 1

    z = 0
    while z < len(tour_list):
        c2 = int(tour_list[z].id)
        for it in range(len(tour_ids)):

            if (c2 == tour_ids[it]):
                del tour_list[z]
        z += 1

    tour_list=tour_list[:3]


    return tour_list








