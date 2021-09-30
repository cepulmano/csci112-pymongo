def get_collections(client, database):
    collections = client[database].list_collection_names()
    return collections

def get_rating_by_genre(client, database):
    """
    Get average rating per movie genre
    """

    movies = client[database].movies
    
    results = movies.aggregate([
    	{
    		"$unwind": "$genres"	
    	},
    	{
    		"$group": {
    			"_id": "$genres",
    			"averageRating": {
    				"$avg": "$imdb.rating"
    			}
    		}
    	},
    	{
    		"$sort": {
    			"averageRating": -1
    		}
    	}
    ])
    
    return results