import pandas as pd
import os

init_dataset = pd.read_csv(os.path.join(os.getcwd(), 'data\\IRAhandle_tweets_1.csv'))
init_dataset = init_dataset[:10000]
# language is English and content contains a '?'
filtered_dataset = init_dataset[
    (init_dataset.language == 'English') & (~(init_dataset.content.str.contains('\?+', regex=True)))]

# add "trump_mention" feature
# must match a single word 'Trump'
trump_mention = list(filtered_dataset.content.str.contains('[\s, \W]+Trump[\s, \W]+'))
c = trump_mention.count(True)
trump_mention = ['T' if v else 'F' for v in trump_mention]
filtered_dataset.loc[:, 'trump_mention'] = trump_mention
# number of tweets that mention Trump
print('Number of tweets that mention Trump: %d' % c)
filtered_dataset.to_csv(path_or_buf=os.path.join(os.getcwd(), 'dataset.tsv'),
                        sep='\t', columns=['tweet_id', 'publish_date', 'content', 'trump_mention'],
                        index=False)

# calculate stats: % of tweets that mention Trump
print('Percentage of tweets that mention trump: %.3f ' % (c * 100 / len(init_dataset)))

#write results
results_dict = {'result':[], 'value':[]}
results_dict['result'].append('frac-trump-mention')
results_dict['value'].append('%.3f' % (c * 100 / len(init_dataset)))
results_df = pd.DataFrame(results_dict)
results_df.to_csv(os.path.join(os.getcwd(), 'results.tsv'), sep='\t', index=False)

