# lib/seed.py

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Game, Review

fake = Faker()

# Setup SQLAlchemy
engine = create_engine('sqlite:///one_to_many.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Seed data
game = Game(title='Breath of the Wild', genre='Action-adventure', platform='Switch', price=60)
session.add(game)
session.commit()

review = Review(score=10, comment='A classic!', game_id=game.id)
session.add(review)
session.commit()

# Add more seed data as needed...
