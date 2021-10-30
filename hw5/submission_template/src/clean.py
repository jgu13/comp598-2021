import json
import argparse

# import os
# import sys
# from pathlib import Path
# sys.path.append(os.path.join(Path(__file__).parents[1],'src'))
import utils

def clean():
    parser = argparse.ArgumentParser(description="Process input and output paths.")
    parser.add_argument("-i", "--Input_file_path", help="Input file")
    parser.add_argument("-o", "--Output_file_path", help="Output file")
    args=parser.parse_args()

    Input_fpath = args.Input_file_path
    Output_fpath = args.Output_file_path

    posts = utils.open_and_loads(Input_fpath) #returns a list a json object
    valid_posts = ""
    for post in posts:
        if type(post) is dict:
            # print(f"After check_dict_type:{post}")
            if utils.check_title_and_replace(post):
                # print(f"After check_title:{post}")
                if utils.check_datetime(post):
                    # print(f"After check_datetime:{post}")
                    if utils.check_author(post):
                        # print(f"After check_author:{post}")
                        if utils.check_total_count(post):
                            # print(f"After check_total_count:{post}")
                            if utils.check_tags(post):
                                # print(f"After check_tags, this is a valid post:{post}")
                                valid_posts += json.dumps(post) + '\n' #extend valid posts
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    utils.write_to_output_file(Output_fpath, valid_posts)

clean()