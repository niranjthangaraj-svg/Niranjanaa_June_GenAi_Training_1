def add_book(catalog, bid, title, author, year):
    catalog[bid] = (title, author, year)

def borrow_book(catalog, borrowed, bid):
    if bid in catalog and bid not in borrowed:
        borrowed.append(bid)

def return_book(borrowed, bid):
    if bid in borrowed:
        borrowed.remove(bid)

def register_member(members, mid):
    members.add(mid)

def show_available(catalog, borrowed):
    print("\nAvailable Books:")
    for bid, (title, author, year) in catalog.items():
        if bid not in borrowed:
            print(bid, title, author, year)

catalog = {}
borrowed = []
members = set()

add_book(catalog, 101, "Python", "John", 2021)
add_book(catalog, 102, "DSA", "Alice", 2020)
add_book(catalog, 103, "ML", "Tom", 2022)
add_book(catalog, 104, "AI", "Sarah", 2023)

register_member(members, 1)
register_member(members, 2)
register_member(members, 3)
register_member(members, 2)

borrow_book(catalog, borrowed, 101)
borrow_book(catalog, borrowed, 103)

return_book(borrowed, 101)

show_available(catalog, borrowed)