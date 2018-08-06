from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowladge'
	interest_id = Column(Integer, primary_key = True)
	wikiArticle = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	

	def __repr__(self):
		return ("interest_id: {}\n"
				"wikiArticle: {}\n"
				"topic: {}\n"
				"rating : {}\n").format(
				self.interest_id,
				self.wikiArticle,
				self.topic,
				self.rating)
x = Knowledge(interest_id=1, topic = "Music", wikiArticle = "guitars" , rating = 10)
print(x)

			




	