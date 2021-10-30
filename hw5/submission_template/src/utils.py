from datetime import datetime
import json
import os.path as osp

def check_title_and_replace(post):
    if "title" in post.keys() or "title_text" in post.keys():
        if "title_text" in post.keys():
            post['title'] = post.pop("title_text")
        return True
    return False

def check_datetime(post):
    if 'createdAt' in post.keys():  # If the post does not have 'createdAt' field, leave it in
        # If the post has 'createdAt' field, but cannot be parsed with ISO datetime standard, then discard it
        try:
            datetime.strptime(post['createdAt'], "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            return False
        else:
            return True
    else:
        return True


def check_author(post):
    if 'author' in post.keys():  # If the post does not have 'author' field, leave it in
        # If the post has 'author' field but is null or N/A, discard it
        author_field = post["author"]
        if author_field is None or author_field.lower() == "n/a" or author_field == "":
            return False
        else:
            return True
    else:
        return True


def check_total_count(post):
    if 'total_count' in post.keys():
        total_count_field = post['total_count']
        # if total_count is not int, float or str, discard
        # for float and str, attempt to convert to int. ex: 22.9 -> 22
        # discard the post if the field cannot be converted.
        type_of_total_count = type(total_count_field)
        if type_of_total_count is int or type_of_total_count is float or \
                type_of_total_count is str:
            try:
                int(total_count_field)
            except ValueError:
                return False
            else:  # else block if no error were raised
                return True
        else:
            return False
    else:
        return True

def check_tags(post):
    if 'tags' in post.keys():
        tags_field = post['tags']
        if tags_field is []:
            return True
        else:
            new_tags = []
            for tag in tags_field:
                split_tags = tag.split()
                if len(split_tags) > 1:
                    for new_tag in split_tags:
                        new_tags.append(new_tag)
                else:
                    new_tags.append(tag)
            post.update({'tags': new_tags})
            return True
    else:
        return True


def write_to_output_file(outputfile_path, json_string):
    output_file = open(outputfile_path, mode='w') # create the output file if it does not exists
    try:
        output_file.write(json_string)
    except:
        print("Output file path is not writable!")

def open_and_loads(Inputfile_path):
    try:
        Input_file = open(Inputfile_path, mode='r')
        posts = []
        for line in Input_file:
            try:
                posts.append(json.loads(line))
            except:
                continue
        Input_file.close()
        return posts #always return posts list
    except Exception as e:
        print(f"Error when opening file: {Inputfile_path}: {e}")
