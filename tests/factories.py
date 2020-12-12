from factory import Factory, Faker, Sequence
from sqlalchemy.orm import sessionmaker
from example_app.db_schemata import Post


class PostFactory(Factory):
    class Meta:
        model = Post

    id = Sequence(lambda n: n + 1)
    text = Faker("company")


def make_default_data(engine):
    DBSession = sessionmaker()
    DBSession.configure(bind=engine)
    db = DBSession()
    posts = PostFactory.create_batch(50)
    db.bulk_save_objects(posts)
    db.commit()
    db.close()
