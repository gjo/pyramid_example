from factory.faker import faker


def test(testapp):
    resp1 = testapp.post_json("/accounts/", None)
    assert "token" in resp1.json
    token = resp1.json["token"]
    fake = faker.Faker()
    fake_post = fake.job()
    resp2 = testapp.post_json("/posts/", {"text": fake_post}, headers={"X-Api-Key": token})
    assert "id" in resp2.json
    post_id = resp2.json["id"]
    resp3 = testapp.get("/posts/")
    assert "posts" in resp3.json
    assert post_id in [p["id"] for p in resp3.json["posts"]]
