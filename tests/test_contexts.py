from zope.interface.verify import verifyObject


def test_actor():
    from example_app.contexts.actor import Actor
    from example_app.interfaces import IActor

    obj = Actor(None, None, None, None, None, None)
    verifyObject(IActor, obj, tentative=True)


def test_timestamp():
    from example_app.contexts.timestamp import Timestamp
    from example_app.interfaces import ITimestamp

    obj = Timestamp(None)
    verifyObject(ITimestamp, obj, tentative=True)
