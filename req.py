import requests
import config
import body


def post_new_courier():
    url = config.URL_SERVICE + config.CREATE_COURIER_PATH
    return requests.post(url, json=body.courier_body)


def post_new_order(order_body):
    url = config.URL_SERVICE + config.CREATE_ORDER_PATH
    return requests.post(url, json=body.order_body)



def get_track(track):
    url = "https://2af890d0-0509-4eb3-9630-b7474ee4ff7f.serverhub.praktikum-services.ru/v1/orders/track?t={track}"
    response = requests.get(url)
    return response