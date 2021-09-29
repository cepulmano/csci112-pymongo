def get_collections(client, database):
    collections = client[database].list_collection_names()
    return collections

def get_students_by_grade(client, database, grade):
    """
    Find all students based on a given exam score. 
    """

    grades = client[database].grades
    
    results = grades.find({
    	"scores": {
    		"$elemMatch": {
    			"type": "exam",
    			"score": {
    				"$gt": grade
    			}
    		}
    	}
    })
    
    return results

def get_inspections_by_status(client, database, statuses):
    """
    Find all documents in the inspections collection that have 
    based on a list of statuses. e.g. Pass or Fail
    """
    inspections = client[database].inspections
    
    results = inspections.find({
    	"result" : {
    	    "$in" : statuses
    	}
    })
    
    return results
    
def get_stories_by_topic_or_media(client, database, topic_name, media_type):
    """
    Find all digg stories based on a given topic name or the media type. 
    """
    stories = client[database].stories
    
    results = stories.find({
        "$or": [
            {"topic.name": topic_name},
            {"media": media_type}
            ]
    })
    
    return results
    
def get_stories_by_view_count(client, database, view_count):
    """
    Finds all digg stories with view_count greater than the given input.
    """
    stories = client[database].stories
    
    results = stories.find({
    	"shorturl": {
    		"$elemMatch": {
    			"view_count": {
    				"$gt": view_count
    			}
    		}
    	}
    })
    
    return results
    
def get_stories_by_container_or_topic(client, database, container_name, topic_name):
    """
    Find stories with a given container name OR topic name. 
    Topic and container name each take only one argument.
    """
    stories = client[database].stories
    
    results = stories.find({
    	"$or" : [
    	        {"container.name" : container_name},
    	        {"topic.name" : topic_name}
    	    ]
    })
    
    return results
    
def get_stories_by_author_or_tags(client, database, author, tags):
    """
    Find stories based on an author or a list of tags. 
    A story matches if at least one tag in the list matches.
    """
    posts = client[database].posts
    
    results = posts.find({
        "$or" : [
                {"author" : author},
                {"tags" : {
                    "$in" : tags
                }}
            ]
    })
    
    return results
    
def get_customers_by_account_type_and_age(client, database, account_type, age):
    """
    Find customers based on a given account_type and less than a given age
    """
    customers = client[database].customers
    
    results = customers.find({
        "accountType" : account_type,
        "age" : {
            "$lt" : age
        }
    })
    
    return results

# Update functions
def set_inspection_fine_by_status(client, database, inspection_result, fine):
    """
    Set a fine on documents given a status and fine value. Status only
    accepts one string value
    """
    inspections = client[database].inspections
    
    results = inspections.update_many({
    	"result" : inspection_result
    },
    {
        "$set" : {
            "fine" : fine
        }
    })
    
    return results
    
def increase_inspection_fine_by_status_and_city(client, database, city, inspection_result, fine):
    """
    Increase fine on documents given a status, city and fine value. Status and city
    only accept one string value per argument.
    """
    inspections = client[database].inspections
    
    results = inspections.update_many({
    	"$and" : [
    	        {"address.city" : city},
    	        {"result" : inspection_result}
    	    ]
    },
    {
        "$inc" : {
            "fine" : fine
        }
    })
    
    return results
    
    