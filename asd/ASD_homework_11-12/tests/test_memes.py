from endpoints.DELETE_memes import DeleteEnpoints
from endpoints.GET_memes import GetEndpoints
from endpoints.POST_memes import PostEnpoints
from endpoints.PUT_memes import PutEnpoints
import pytest


# @pytest.mark.skip
@pytest.mark.parametrize('repeat', range(10))
@pytest.mark.parametrize('urls_control',
                         ['https://media.tenor.com/Kdw0KeHJMogAAAAd/will-you-please-come-home-randy-marsh.gif'])
def test_create_a_meme(base_url, auth_token, texts, urls, tag, infos, urls_control, repeat):
    create_meme = PostEnpoints(base_url, auth_token, texts, urls, tag, infos)
    assert create_meme.is_response_200(), f"Expected status code 200, but got {create_meme.status_code}"
    assert create_meme.link_is_correct(urls_control), 'Please check your meme data, incl. URL'
    print(create_meme.result_json)


# @pytest.mark.skip
@pytest.mark.parametrize('meme_id', [2, 3])
def test_change_a_meme(base_url, auth_token, meme_id):
    change_meme = PutEnpoints(base_url, auth_token, meme_id)
    assert change_meme.is_response_200(), f"Expected status code 200, but got {change_meme.status_code}"
    get_meme = GetEndpoints(base_url, auth_token, meme_id)
    assert get_meme.result_json == change_meme.result_json, 'Not all memes have been have been changed'
    print(change_meme.result_json)
    print(get_meme.result_json)


@pytest.mark.skip
@pytest.mark.parametrize('tag_c', ['fun'])
def test_get_a_meme_without_id(base_url, auth_token, tag_c):
    get_meme = GetEndpoints(base_url, auth_token, tag_control=tag_c)
    assert get_meme.is_response_200(), f"Expected status code 200, but got {get_meme.status_code}"
    assert tag_c in get_meme.tag_is_correct(tag_c), f"Tag {tag_c} not found in the response"
    print(get_meme.result_text)


# @pytest.mark.skip
@pytest.mark.parametrize('tag_c', ['fun'])
@pytest.mark.parametrize('meme_id', range(4, 8))
def test_get_a_meme_with_id(base_url, auth_token, meme_id, tag_c):
    get_meme = GetEndpoints(base_url, auth_token, meme_id, tag_control=tag_c)
    assert get_meme.is_response_200(), f"Expected status code 200, but got {get_meme.status_code}"
    assert tag_c in get_meme.tag_is_correct(tag_c), f"Tag {tag_c} not found in the response"
    print(get_meme.result_json)


# @pytest.mark.skip
@pytest.mark.parametrize('meme_id', range(2, 22))
def test_delete_a_meme(base_url, auth_token, meme_id):
    delete_meme = DeleteEnpoints(base_url, auth_token, meme_id)
    delete_meme.skip_404()
    assert delete_meme.is_response_200(), f"Expected status code 200, but got {delete_meme.status_code}"
    print(delete_meme.result_text)
