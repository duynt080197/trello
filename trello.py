"""Viết script dùng API tạo 1 Trello board với 2 list "Thứ 3", "Thứ 5",
và tạo 12 card ứng với 12 buổi học của lớp, có set due date ứng với các ngày
học.
Ví dụ kết quả: https://trello.com/b/yEskTV8S/h%E1%BB%8Dc-python-h%C3%A0-n%E1%BB%99i-pymivn-hn2006-timetable
API: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
https://developer.atlassian.com/cloud/trello/rest/#api-boards-post
https://developer.atlassian.com/cloud/trello/rest/#api-lists-post
https://developer.atlassian.com/cloud/trello/rest/#api-cards-post

"""

import requests
import sys
import json


def create_board(key, token, name):
    """ Tạo bảng với tên là 'name'"""

    url = "https://api.trello.com/1/boards/"
    query = {"key": key, "token": token, "name": name}
    response = requests.request("POST", url, params=query)
    print((json.loads(response.text))["url"])
    return json.loads(response.text)["id"]


def create_list(key, token, day, board_id):
    """Tạo list với tên là 'day' và idBoard lấy từ function create_board """
    url = "https://api.trello.com/1/lists"
    query = {"key": key, "token": token, "name": day, "idBoard": board_id}
    response = requests.request("POST", url, params=query)

    return json.loads(response.text)["id"]


def create_card(key, token, name, list_id, date):
    """Tạo card với tên là 'name' và idList lấy từ function create_list """
    url = "https://api.trello.com/1/cards"
    query = {
        "key": key,
        "token": token,
        "name": name,
        "idList": list_id,
        "due": date,
    }
    response = requests.request("POST", url, params=query)

    return response.text


def solve():
    """:param key: nhập vào: keyAPI
    :param token: nhập vào: tokenAPI"""
    key = sys.argv[1]
    token = sys.argv[2]
    name = "PYMI 2101HCM"
    board_id = create_board(key, token, name)
    days = [
        [
            ("Bài 1", "2021/01/12"),
            ("Bài 3", "2021/01/19"),
            ("Bài 5", "2021/01/26"),
            ("Bài 7", "2021/02/02"),
            ("Bài 9", "2021/02/23"),
            ("Bài 11", "2021/03/02"),
        ],
        [
            ("Bài 2", "2021/01/14"),
            ("Bài 4", "2021/01/21"),
            ("Bài 6", "2021/01/28"),
            ("Bài 8", "2021/02/04"),
            ("Bài 10", "2021/02/25"),
            ("Bài 12", "2021/03/04"),
        ],
    ]
    day_learn = ["Tuesday", "Thursday"]
    for day in day_learn:
        list_id = create_list(key, token, day, board_id)
        note = day_learn.index(day)
        for day in days[note]:
            create_card(key, token, day[0], list_id, day[1])
    return create_card


def main():
    print("Link this board: ")
    solve()


if __name__ == "__main__":
    main()
