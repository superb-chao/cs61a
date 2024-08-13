
## Instance attributes are found before class attributes; class attributes are inherited
class Link:
    empty = ()
    def __init__(self, first, rest = empty) -> None:
        assert rest is Link.empty or isinstance(Link)
        self.first = first
        self.rest = rest

def add(s, v):
    assert s is not Link.empty

    if s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        s.rest = add(s.rest, v)
    else:
        s.first, s.rest = v, Link(s.first, s.rest)
        #当 Python 执行类似 a, b = expr1, expr2 的语句时，首先计算 expr1 和 expr2 的值，然后再同时更新 a 和 b。
    
    return s

## Tree

class tree:
    def __init__(self, label, branches) -> None:
        self.label = label
        for branch in branches:
            assert isinstance(branch,tree)
        self.branches = list(branches)



## Memoization
def memo(f):
    cache = {}
    def memoized(n):
        if n>800:
            memoized(n-800)
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
    #注意返回memoize和memoize()的区别；当返回memoize的时候，返回的是函数,而memoize()会直接调用
    """
    >>> y=fib
    >>> x=memo(y)
    >>> x(5)
    为什么这里没有使用缓存?
    当你执行 x(5) 时，虽然 x 是缓存后的 fib 函数，
    但是 fib 函数内部的递归调用仍然是调用的原始 fib 函数，
    而不是缓存后的版本。
    """

@memo
def fib(n):
    if n == 1 or n == 2:
        return 1 
    if n > 2:
        return fib(n - 2) + fib(n - 1)
    
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

## Exponentaion

## Modular Design
### Example:restaurant search
def search(query, ranking=lambda r: -r.stars):
    results = [r for r in Restaurant.all if r.name == query]
    return sorted(results,key = ranking)

def same_rank(self, others):
    return [i for i in others if i.stars == self.stars]

class Restaurant:
    all = []
    def __init__(self, name, stars) -> None:
        self.name = name
        self.stars = stars
        Restaurant.all.append(self)
    
    def similar(self, k=1, similarity = same_rank):
        others = Restaurant.all
        others.remove(self)
        return sorted(similarity(self,others) ,key = lambda x: -x.stars)[:k]
    ##注意这里要加key，对Restaurant的stars进行排序，对实例是不能直接排序的
    
    def __repr__(self) -> str:
        return '<' + self.name + '>'

xiangcai = Restaurant('xiangcai',5)
chuancai = Restaurant('chuancai',5)
ecai = Restaurant('ecai',3)
taicai = Restaurant('taicai',3)
yuecai = Restaurant('yuecai',5)

x=[100,201,393,110,873,891]
last_digit = [i%10 for i in x]
num_dic={p : [q for q in x if q%10 == p] for p in range(0,10) if p in last_digit}

