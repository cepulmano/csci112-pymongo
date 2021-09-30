def get_collections(client, database):
    collections = client[database].list_collection_names()
    return collections

def get_cases_by_sex(client, database, sex):
    """
    Find all cases based on a given sex. 
    """

    linelist = client[database].linelist
    
    results = linelist.find({
    	"Sex": sex
    })
    
    return results