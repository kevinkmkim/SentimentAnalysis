def get_dictionary():
    """    
    Description: 
    Function designed to create a dictionary
    of the words from the AFINN-111.txt file.
    
    Parameters:
    No parameter
        
    Returns:
    Returns the dictionary containing the words from the file AFINN-111.txt. 

    """
    filename = 'AFINN-111.txt'
    try: 
        with open(filename, 'r', encoding='utf8') as in_file:
            x = in_file.read()
            lines = x.split('\n')
            dictionary = {}
            for line in lines:
                try:
                    elements = line.split('\t')
                    dictionary[elements[0]] = elements[1]
                except:
                    pass
        return dictionary
                
    except IOError or FileNotFoundError:
        return {} 

def get_text(tweets, dictionary):
    """    
    Description: 
    Function designed to look at the words in the tweets from the search
    and the words in the AFINN-111.txt file to see which ones are in common.
    Those in common are added to a list.
    
    Parameters:
    tweets: The tweets that are gotten from the search query.
    dictionary: The dictionary of words from the AFINN-111.txt file
        
    Returns:
    Returns length which is the length of the tweet list which is the number of tweets.
    Also returns valid_texts which is the list of texts that the tweets and the dictionary have in common with each other.

    """
    valid_texts = []
    tweet_list = tweets["statuses"]
    length = len(tweet_list)
    for i in range(len(tweet_list)):
        lower_cased_text = tweet_list[i]["text"].lower()
        words = lower_cased_text.split()
        for word in words:
            if word in dictionary.keys():
                valid_texts.append(word)
            else:
                pass
    return valid_texts, length

def get_score(text, dictionary, length):
    """    
    Description: 
    Function designed to calculate the sentiment score of a search query
    based on the words found within the tweets that are in common with the dictionary. 
    
    Parameters:
    text: The list of texts that the tweets and the dictionary have in common with each other
    dictionary: The dictionary of words from the AFINN-111.txt file
    length: Length of the tweet list which is the number of tweets
        
    Returns:
    Returns the sentiment score of a certain search query.

    """
     
    sum = 0
    if len(dictionary) > 0:
        for i in text:
            sum += int(dictionary[i])
        if length > 0:
            score = sum / length
        else:
            score = 0
    else:
        score = 0
    
    return score

def analyze_tweets(query):
    """    
    Description: 
    Function designed to look at tweets based on a search query and
    returns the sentiment score by returning the get_score function.
    
    Parameters:
    query: The search term that is inputed in order to calculate the sentiment
    score of the term
        
    Returns:
    Returns the sentiment score based off of the what the get_score
    function parameters are for the search query.
    """
     
    
    tweets = twitter.get_tweets(query)
    dictionary = get_dictionary() 
    text, length = get_text(tweets, dictionary)
    return get_score(text, dictionary, length)

def main():
    """ main function """
    
    query = input()
    print(analyze_tweets(query))
   

    
if __name__ == "__main__":
    main()
