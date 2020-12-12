from zope.interface.verify import verifyObject


def test_post_query():
    from example_app.interfaces import IPostQuery
    from example_app.queries.post_query import PostQuery

    obj = PostQuery(None, None)
    verifyObject(IPostQuery, obj, tentative=True)
