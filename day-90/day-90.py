import requests
import json

API_KEY = '4dedd2caa76740bd8bbc401fb945c34e'  # Replace with your actual API key

def fetch_articles(query, max_pages=3):
    all_articles = []
    try:
        for page in range(1, max_pages + 1):
            url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}&pageSize=100&page={page}'
            response = requests.get(url)
            response.raise_for_status()  # raise HTTPError for bad requests
            data = response.json()

            if 'articles' not in data:
                print("No articles found.")
                return []

            all_articles.extend(data['articles'])

            if len(data['articles']) < 100:
                break  # stop if fewer articles returned (end of data)
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching articles:", e)
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
    return all_articles

def main():
    try:
        query = input("Enter the topic you want to search: ").strip()
        if not query:
            raise ValueError("Search query cannot be empty.")

        articles = fetch_articles(query)
        if not articles:
            print("No articles found.")
            return

        print(f"\nHere are top {len(articles)} results from the query:\n")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article.get('title')}")

        title_no = int(input("\nEnter the Title number you want to get a brief description of: "))
        if not (1 <= title_no <= len(articles)):
            raise IndexError("Invalid title number selected.")

        selected = articles[title_no - 1]
        print(f"""
Title: {selected.get('title')}
Description: {selected.get('description')}
Url: {selected.get('url')}
Url To Image: {selected.get('urlToImage')}
Published at: {selected.get('publishedAt')}
Content: {selected.get('content')}
""")
    except ValueError as ve:
        print("Input Error:", ve)
    except IndexError as ie:
        print("Selection Error:", ie)
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
