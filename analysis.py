from csv import reader
import datetime as dt

def avg_value(list, index):
    total_val = 0
    for data in list:
        value = data[index]
        value = int(value)
        total_val += value
    return total_val/len(list)


opened_file = open('hn_clean.csv',encoding='utf8')
read_file = reader(opened_file)
news_list = list(read_file)
ask_posts = []
show_posts = []
other_posts = []
for news in news_list:
    title = news[1]
    title = title.lower()
    if title.startswith('ask hn'):
        ask_posts.append(news)
    elif title.startswith('show hn'):
        show_posts.append(news)
    else:
        other_posts.append(news)
print("Total posts: ",len(news_list))
print("Ask posts: ",len(ask_posts))
print("Show posts: ",len(show_posts))
print("Other posts: ",len(other_posts))
print("\nComments on ask posts: ",avg_value(ask_posts,4))
print("Comments on show posts: ", avg_value(show_posts,4))
print("\nAsk posts get more comments")
print("\nComments by Hour:")
counts_by_hour = {}
comments_by_hour = {}
for posts in ask_posts:
    time_of_creation = posts[6]
    comments = int(posts[4])
    datetime_obj = dt.datetime.strptime(time_of_creation,"%m/%d/%Y %H:%M")
    hour = datetime_obj.strftime("%H")
    if hour in counts_by_hour:
        counts_by_hour[hour] +=1
        comments_by_hour[hour] += comments
    else:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = comments
avg_by_hour = []
for hours,comments in comments_by_hour.items():
    number_of_posts = counts_by_hour[hours]
    avg_comments = comments/number_of_posts
    avg_by_hour.append([avg_comments,hours])

avg_by_hour = sorted(avg_by_hour, reverse=True)
for data in avg_by_hour:
    print("{}:00 : {:.2f} average comments per post".format(data[1],data[0]))

print("\nRecommendation: Make a post at 3 PM to get the most comments")

