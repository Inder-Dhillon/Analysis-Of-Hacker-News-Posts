from csv import reader,writer
opened_file = open('hacker_news.csv',encoding='utf8')
opened_clean = open('hn_clean.csv','w',encoding='utf8',newline='')
read_file = reader(opened_file)
news_list = list(read_file)
news_list = news_list[1:]
write_file = writer(opened_clean)
i = 0
#Cleaning the data-set
#Removing posts with no comments
for news in news_list:
    num_comments = news[4]
    i +=1
    print(i)
    if num_comments != '0':
        write_file.writerow(news)
