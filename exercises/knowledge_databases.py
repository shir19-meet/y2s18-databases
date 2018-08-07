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


	
	


def query_all_articles():
	knowledge = session.query(
    Knowledge).all()
	return knowledge
	
 	


def query_article_by_topic(add_article):
	knowledge_object = session.query(Knowledge).filter_by(topic= add_article).first()
 	return(knowledge_object)




def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
    	topic= topic).delete()
   	session.commit()


#add_article("qwer", "fdfa",10 )
#print(query_article_by_topic("qwer"))
delete_article_by_topic("qwer")
print(query_all_articles())



def delete_all_articles():
	session.query(Knowledge).delete()
   	session.commit()

#add_article("qwer", "fdfa",10 )
#print(query_article_by_topic("qwer"))
#delete_article_by_topic("qwer")
print(query_all_articles())
delete_all_articles()
	

# def edit_article_rating():
	
