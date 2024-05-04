from requests import get


def bold_text(t1, t2):
    return f"\033[1m{t1}. {t2} \033[0m"


search = input('Search:\t')

url = 'https://newsapi.org/v2/everything?'
params = {
    'apiKey': '757e0ca3a9144c2192bce813d064efeb',
    'q': search,  # Specify your query here
    'pageSize': 22  # Specify the number of articles you want
}
try:
    data = get(url, params=params).json()
    if 'articles' in data:
        articles = data.get('articles', [])  # this function takes value of python_data['articles'] and stores it in a list
        for index, article in enumerate(articles):
            title = article.get('title', '')  # this function takes value of python_data['articles'] and stores it is a string
            description = article.get('description', '')  # this function takes value of python_data['articles'] and stores it as a string
            if title != '[Removed]':
                print(bold_text(index + 1, title))
                print(description, '\n')
    else:
        print('No articles were found')
except Exception as e:
    print('Error', e)
