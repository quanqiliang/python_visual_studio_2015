import requests
from bs4 import BeautifulSoup
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=vs%202017%20linux%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7&oq=vstudio%25202017%2520%25E8%2581%2594%25E7%25B3%25BBlinux&rsv_pq=996a4ccb0004a3fd&rsv_t=dc55EJCptE%2FHen5ezjOBRATGK12VCYAurh7vaAdKOswEIHYTcHwRUGKCPks&rqlang=cn&rsv_enter=1&inputT=20171&rsv_sug3=35&rsv_sug1=8&rsv_sug7=000&bs=vstudio%202017%20%E8%81%94%E7%B3%BBlinux'

rs = requests.get(url)
soup = BeautifulSoup(rs.text,'lxml')

print(soup.prettify())

def f():
    print("hello world!")
    for x in range(1, 10):
        lst = []
        for y in range(1, x + 1):
            lst.append(str(y)+'*'+str(x)+'='+str(y*x))
        print(lst)
if __name__ == '__main__':
    f()