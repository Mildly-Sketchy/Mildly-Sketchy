from pyramid import testing

def test_render_search_view(dummy_request):
    """Test search view"""
    from ..views.search import search_view
    response = search_view(dummy_request)
    assert type(response) == dict


def test_search_view_no_keywords(dummy_request):
    """Test search view response when the user does not give any keywords"""
    from ..views.search import search_view
    response = search_view(dummy_request)
    len(response) == 0
    assert type(response) == dict


def test_search_view_with_no_keywords(dummy_request):
    """Test search view with no keywords"""
    from ..views.search import search_view

    dummy_request.method = 'GET'
    response = search_view(dummy_request)
    assert response == {'message': 'You do not have any keywords saved. Add one!'}


def test_search_view_gets_keywords(dummy_request):
    '''Test search view returns keywords with fake authenticated user'''
    from ..views.search import search_view
    from ..models.accounts import Account
    from ..models.keywords import Keyword
    from ..models.association import Association

    config = testing.setUp()

    config.testing_securitypolicy(
        userid='codefellows', permissive=True
    )
    new_account = Account(
        username='codefellows',
        password='password',
        email='myemail@gmail.com'
    )
    dummy_request.dbsession.add(new_account)

    new_keyword = Keyword()
    new_keyword.keyword = 'developer'
    dummy_request.dbsession.add(new_keyword)

    dummy_request.dbsession.commit()

    new_association = Association()
    new_association.user_id = 'codefellows'
    new_association.keyword_id = 'developer'
    dummy_request.dbsession.add(new_association)

    dummy_request.dbsession.commit()

    response = search_view(dummy_request)

    assert response['keywords'][0].keyword == 'developer'


def test_handle_keywords_view_bad_request(dummy_request):
    '''test handle keywords bad request'''
    from ..views.search import handle_keywords
    from pyramid.httpexceptions import HTTPBadRequest

    dummy_request.method = 'POST'
    response = handle_keywords(dummy_request)
    assert response.status_code == 400
    assert isinstance(response, HTTPBadRequest)


def test_handle_keywords_gets_keyword(dummy_request):
    '''test that it gets the key word'''
    from ..views.search import handle_keywords
    from pyramid.httpexceptions import HTTPFound

    dummy_request.POST = {'keyword': 'web developer'}
    dummy_request.method = 'POST'
    response = handle_keywords(dummy_request)
    assert isinstance(response, HTTPFound)


def test_handle_keywords_number_as_a_keyword_throws_error(dummy_request):
    '''test that a number throws the correct error'''
    from ..views.search import handle_keywords

    dummy_request.POST = {'keyword': '4'}
    dummy_request.method = 'POST'
    response = handle_keywords(dummy_request)
    assert response == {'error': 'Search term cannot be a number.'}


def test_delete_keyword_view_bad_request(dummy_request):
    '''test delete keywords bad request'''
    from ..views.search import delete_keyword
    from pyramid.httpexceptions import HTTPBadRequest

    dummy_request.method = 'POST'
    response = delete_keyword(dummy_request)
    assert response.status_code == 400
    assert isinstance(response, HTTPBadRequest)
