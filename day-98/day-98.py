#Multi Processing
import multiprocessing
import requests

#multiprocessing is a type of threading which run multiple processes parallely, it is different from thread as thread is a smaller unit

def downloadFile(url, name):
    print(f"Started downloading file {name}")
    response = requests.get(url)
    open(f"files/file_{name}.jpg", "wb").write(response.content)
    print(f"Downloaded file {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    process = []
    for i in range(60):
        p = multiprocessing.Process(target=downloadFile, args=[url,i])
        p.start()
        process.append(p)

    for p in process:
        p.join()

# import concurrent.futures

# if __name__ == '__main__':
#     url = "https://picsum.photos/2000/3000"
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         l1 = [url for i in range(60)]
#         l2 = [i for i in range(60)]
#         results = executor.map(downloadFile, l1, l2)
