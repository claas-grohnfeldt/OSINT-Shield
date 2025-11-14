from __future__ import annotations


def test_list_events_returns_data(client):
    response = client.get("/events?limit=5")
    assert response.status_code == 200
    events = response.json()
    assert events, "expected at least one event"
    sample = events[0]
    assert "source" in sample
    assert "relevance_score" in sample


def test_event_detail(client):
    events = client.get("/events?limit=1").json()
    event_id = events[0]["id"]
    detail = client.get(f"/events/{event_id}")
    assert detail.status_code == 200
    payload = detail.json()
    assert payload["id"] == event_id
    assert isinstance(payload.get("entities"), list)
