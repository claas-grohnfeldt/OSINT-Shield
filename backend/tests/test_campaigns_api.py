from __future__ import annotations


def test_list_campaigns(client):
    response = client.get("/campaigns")
    assert response.status_code == 200
    campaigns = response.json()
    assert campaigns, "expected at least one campaign"
    assert "risk_score" in campaigns[0]


def test_get_campaign_detail(client):
    campaign_id = client.get("/campaigns").json()[0]["id"]
    detail = client.get(f"/campaigns/{campaign_id}")
    assert detail.status_code == 200
    payload = detail.json()
    assert payload["id"] == campaign_id
    assert "events" in payload and payload["events"]
