import body
import req
import requests
import pytest



def test_post_new_order():
    response = req.post_new_order(body.order_body)
    track = response.json()["track"]
    track_report = req.get_track(track)
    assert track_report.status_code == 200
    print("Код ответа", track_report.status_code, "Трек номер", response.json()["track"], track_report.json())
