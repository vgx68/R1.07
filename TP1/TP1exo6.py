print("entre des minutes")
mi=int(input())
jour= (mi//24)//60
mi=mi%(24*60)
heure= mi// 60
mi=mi%60
minutes= mi
print("voici la date", jour,"octobre", heure,":",minutes)
