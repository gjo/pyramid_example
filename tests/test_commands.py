from zope.interface.verify import verifyObject


def test_account_command():
    from example_app.interfaces import IAccountCommand
    from example_app.commands.account_command import AccountCommand

    obj = AccountCommand(None, None, None)
    verifyObject(IAccountCommand, obj, tentative=True)


def test_post_command():
    from example_app.interfaces import IPostCommand
    from example_app.commands.post_command import PostCommand

    obj = PostCommand(None, None)
    verifyObject(IPostCommand, obj, tentative=True)
