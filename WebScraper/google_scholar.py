from scholarly import scholarly

def grab_profile_by_publisher_name(publisher_name):
    search_results = scholarly.search_author(publisher_name)
    for author in search_results:
        if 'UNC Charlotte' in author['affiliation'] or author['email_domain'] == '@uncc.edu':
            return f'https://scholar.google.com/citations?hl=en&user={author["scholar_id"]}'
        else:
            return None
