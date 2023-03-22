import csv
def main():
    post_contents = []
    with open('post.csv') as post:
        post_contents = list(csv.reader(post))
    original_post_contents = []
    with open('OriginalWebScraperRepo/postComplete.csv') as original_post:
        original_post_contents = list(csv.reader(original_post))     
    og_names = [x[3] for x in original_post_contents]
    new_names = [x[3] for x in post_contents]
    print(len(set(og_names).intersection(set(new_names))))
    print(len(set(og_names)))
    print(len(set(new_names)))
    print([x for x in og_names if og_names.count(x) > 2])


    

if __name__ == '__main__':
    main()