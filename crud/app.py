import db_crud as crud
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.88.83', 27017)
    print(crud.get_collections(client, "sample"))
    
    # Find all students have an exam grade higher than 75
    students = crud.get_students_by_grade(client, "sample", 75)
    
    for student in students.limit(10):
        pprint(student)
    
    # Find all documents in the inspections collection have result “Pass” or “Fail”?
    inspections = crud.get_inspections_by_status(client, "sample", ["Pass", "Fail"])
    
    for inspection in inspections.limit(10):
        pprint(inspection)
        
    # Find all digg stories where the topic name is “Television” or the media type is videos 
    # and sort by diggs from highest to lowest.
    stories = crud.get_stories_by_topic_or_media(client, "sample", "Television", "videos")
    
    for story in stories.sort("diggs", -1).limit(10):
        pprint(story)
        
        
    # In the stories collection, write a query to find all stories where the view count is 10000
    stories = crud.get_stories_by_view_count(client, "sample", 10000)
    
    for story in stories.limit(10):
        pprint(story)
        
    # Find all digg stories where the container is Gaming or the topic is Microsoft 
    # and sort by comments from highest to lowest.
    stories = crud.get_stories_by_container_or_topic(client, "sample", "Gaming", "Microsoft")
    
    for story in stories.sort("comments", -1).limit(10):
        pprint(story)
        
    
    # Find all posts either authored by a machine or tagged with either lamb or fold.    # 
    posts = crud.get_stories_by_author_or_tags(client, "sample", "machine", ["lamb", "fold"])
    
    for post in posts.limit(10):
        pprint(post)
        
    # Find all gold customers younger than 40.
    customers = crud.get_customers_by_account_type_and_age(client, "sample", "gold", 40)
    
    for customer in customers:
        pprint(customer)
    
    # Update Queries
    
    # For all inspections that failed, set a fine value of 100.
    print(crud.set_inspection_fine_by_status(client, "sample", "Fail", 100).matched_count) # modified_count gets all actually modified
    
    # Update all inspections done in the city of “ROSEDALE”. For failed inspections, raise the fine by 150
    print(crud.increase_inspection_fine_by_status_and_city(client, "sample", "ROSEDALE", "Fail", 150).matched_count)
    