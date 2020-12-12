from zope.interface.verify import verifyObject


def test_post():
    from example_app.db_schemata import Post
    from example_app.interfaces import IPost

    obj = Post()
    verifyObject(IPost, obj, tentative=True)
