from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from knowledge_model import Knowledge

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, wikiArticle, rating):
	knowledge_object = Knowledge(
		topic= topic,
		wikiArticle= wikiArticle,
		rating= rating)
	session.add(knowledge_object)
	session.commit()
	add_article("qwer", "fdfa",10 )
	
	


# def query_all_articles():
	

# def query_article_by_topic():
	

# def delete_article_by_topic():
	

# def delete_all_articles():
	

# def edit_article_rating():
	
