

# Tests for your routes go here
"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    response = web_client.get('/wave?name=Dana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


def test_post_sort_names_with_a_list_of_names(web_client):
    response = web_client.post("/sort-names", data={'names' : "Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'


def test_post_sort_names_with_a_list_of_names_with_letter_at_the_end(web_client):
    response = web_client.post("/sort-names", data={'names' : "Aaaaaa,Aaaaz,Aaaaaab"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Aaaaaa,Aaaaaab,Aaaaz"

def test_post_sort_names_with_a_list_of_names_with_letter_at_the_end(web_client):
    response = web_client.post("/sort-names")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "you didn't submit any names"


"""
When: I make a Get request to /name should return names
and: I should get a 200 response with names in list
"""
def test_get_request_returns_names(web_client):
    response = web_client.get("/names")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim"
"""
should return list of name and the added name to the list
and: I should get a 200 response with names in list
"""

def test_add_name_in_list(web_client):
    response = web_client.get("/names?add=Eddie")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Eddie"

def test_add_two_names_in_list(web_client):
    response = web_client.get("/names?add=Eddie, Leo")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Eddie, Leo"

def test_add_three_names_in_list(web_client):
    response = web_client.get("/names?add=Eddie, Leo, Khalifa")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Eddie, Leo, Khalifa"

def test_add_four_names_in_list(web_client):
    response = web_client.get("/names?add=Eddie, Leo, Khalifa, Khalifa")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Eddie, Leo, Khalifa, Khalifa"
"""
when there are no name shoud return an error message 
and  should get a 400 response
"""
