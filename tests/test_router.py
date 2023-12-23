import pytest

@pytest.mark.asyncio(scope='session')
async def test_post_good_links(test_client, good_links, good_status):
    response = test_client.post('/visited_links', content=good_links)
    assert response.status_code == 200, 'Неправильный код ответа'
    assert response.json() == good_status, 'Неправильный статус ответа'


@pytest.mark.asyncio(scope='session')
async def test_post_bad_links(test_client, bad_links, good_status):
    response = test_client.post('/visited_links', content=bad_links)
    assert response.status_code == 403, 'Неправильный код ответа'
    assert response.json() != good_status, 'Неправильный статус ответа'


@pytest.mark.asyncio(scope='session')
async def test_post_bad_links_bad_request(test_client, bad_request, good_status):
    response = test_client.post('/visited_links', content=bad_request)
    assert response.status_code == 403, 'Неправильный код ответа'
    assert response.json() != good_status, 'Неправильный статус ответа'


@pytest.mark.asyncio(scope='session')
async def test_get_visited_domains(test_client, good_visited_domains_response):
    response = test_client.get('/visited_domains')
    assert response.status_code == 200, 'Неправильный код ответа'
    resp_domains = set([domain for domain in response.json()['domains']])
    good_domains = set(good_visited_domains_response)
    assert resp_domains == good_domains, 'Неверный ответ'


@pytest.mark.asyncio(scope='session')
async def test_get_visited_domains_bad_request(test_client):
    response = test_client.get('/visited_domains?from=a&to=-20')
    assert response.status_code == 403, 'Неправильный код ответа'
