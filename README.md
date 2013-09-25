python-antispam
============

A Python API for antispam service cleantalk.org. Invisible protection from spam, no captches, no puzzles, no animals and no math.

## How API stops spam?
API uses several simple tests to stop spammers.
  * Spam bots signatures.
  * Blacklists checks by Email, IP, web-sites domain names.
  * JavaScript availability.
  * Comment submit time.
  * Relevance test for the comment.

## How API works?
API sends a comment's text and several previous approved comments to the servers. Servers evaluates the relevance of the comment's text on the topic, tests on spam and finaly provides a solution - to publish or put on manual moderation of comments. If a comment is placed on manual moderation, the plugin adds to the text of a comment explaining the reason for the ban server publishing.

## Requirements

   * Python 2.6 and above 

## SPAM test for text comment sample 

```python
from cleantalk import CleanTalk


ct = CleanTalk(auth_key='yourkey')
ct_result = ct.request(
                message = 'abc', # Visitor comment
                sender_ip = '196.19.250.114', # Visitor IP address
                sender_email = 'stop_email@example.com', # Visitor email
                sender_nickname = 'spam_bot', # Visitor nickname
                js_on = 1, # Is visitor has JavaScript
                submit_time = 12 # Seconds from start form filling till the form POST
        )
#Check
if ct_result['allow']:
    print('Comment allowed. Reason ' + ct_result['comment'])
else:
    print('Comment blocked. Reason ' + ct_result['comment'])
```

## API Response description
API returns Python dictionary object, where keys:
  * allow (0|1) - allow to publish or not, in other words spam or ham
  * comment (string) - server comment for requests.
  * id (string MD5 HEX hash) - unique request idenifier.
  * errno (int) - error number. errno == 0 if requests successfull.
  * errtstr (string) - comment for error issue, errstr == null if requests successfull.
  
