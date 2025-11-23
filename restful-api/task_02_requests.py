import requests
import csv

def fetch_and_print_posts():
    """
    JSONPlaceholder-dən postları çəkir və başlıqlarını çap edir.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Status kodunu çap edirik
    print(f"Status Code: {response.status_code}")
    
    # Əgər sorğu uğurludursa (200 OK)
    if response.status_code == 200:
        # JSON formatına çeviririk
        posts = response.json()
        
        # Hər bir postun başlığını (title) çap edirik
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    JSONPlaceholder-dən postları çəkir və CSV faylına yazır.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Məlumatı tələb olunan struktura salırıq (list of dictionaries)
        # Yalnız id, title və body sahələrini götürürük
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
            
        # CSV faylına yazmaq
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Başlıqları (header) yazırıq
            writer.writeheader()
            
            # Məlumatları (rows) yazırıq
            writer.writerows(structured_data)
