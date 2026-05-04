# Python Anti-Spam & Bot Filter by CleanTalk — No CAPTCHA/reCaptcha Needed
============

Invisible spam protection for your Python apps — no CAPTCHA/reCaptcha, no puzzles, no math.

Spam attacks log - allows to view all filtered requests in the "Log of spam attacks".
The log contains a detailed information about each request for a time period. At any time, you can check the request and make sure that the filtering is correct. A Python API for antispam service cleantalk.org. Invisible protection from spam, no captches, no puzzles, no animals and no math.

## Why CleanTalk?
Tired of distorted images, puzzles with traffic lights, or invisible zebras?
Here’s how CleanTalk compares:

| Feature                         | CAPTCHA                          | CleanTalk                              |
|---------------------------------|----------------------------------|----------------------------------------|
| User Experience                 | Interrupts with puzzles, images  | Completely invisible                    |
| Setup Complexity                | Medium to High                   | Easy integration with Python API       |
| Mobile Usability                | Often frustrating                | Seamless experience                    |
| Accessibility (e.g. screenreaders) | Limited                       | Fully accessible                       |
| Spam Protection Method          | Challenge-based (user solves)    | Behavior-based (bot detection, JS, IP) |
| Requires User Interaction       | ✅ Yes                            | ❌ No                                   |
| Supports Form Relevance Checks | ❌ No                             | ✅ Yes                                  |


## How API works?
CleanTalk uses multiple layers of protection:

- Spam bot signatures
- Blacklist checks (email, IP, domain)
- JavaScript presence
- Submission time analysis
- Comment relevance scoring

If you find this project useful, please consider starring ⭐ it on GitHub — it helps us grow and support development!

## Requirements

- Python 2.6+
- Python 3.x
- CURL support
- CleanTalk account — [Sign up here](https://cleantalk.org/register?product=anti-spam)

### Websites that trust CleanTalk!

![CleanTalk Anti-Spam Rating](https://cleantalk.org/webpack/img/cleantalk_rating.png)

## SPAM test for text comment sample 

```python
from cleantalk import CleanTalk
import json


ct = CleanTalk(auth_key='yourkey')
# ct.set_event_token_enabled(True)  # See Bot-Detector Integration section below
ct_result = ct.request(
                message = 'abc', # Required. Visitor comment
                sender_ip = '196.19.250.114', # Required. Visitor IP address
                sender_email = 'stop_email@example.com', # Required. Visitor email
                sender_nickname = 'spam_bot', # Required. Visitor nickname
                post_info= json.dumps({'post_url': 'https://yoursite.com'}), # Optional. Additional post info in JSON format.
                event_token = 'xxx' # Optional. Fill it with ct_bot_detector_event_token hidden input from your form (auto generate). See Bot-Detector Integration section below
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

## Installing via PyPi
Run the next command in the terminal:

```python
pip install cleantalk-python-antispam
```
Then you can use Cleantalk class import:
```python
from cleantalk_python_antispam.cleantalk import CleanTalk
```

## Bot-Detector Integration
For improved protection, integrate CleanTalk's bot-detector JavaScript on your website:

### 1. Include the bot-detector script
Add this JavaScript to your layout before `</body>` tag:
```html
<script type="text/javascript" src="https://fd.cleantalk.org/ct-bot-detector-wrapper.js"></script>
```

### 2. Set the event_token_enabled flag in Python
When you have integrated the bot-detector JavaScript, inform the API by setting the `event_token_enabled` flag:

```python
ct = CleanTalk(auth_key='yourkey')
ct.set_event_token_enabled(True)  # Tell API that bot-detector is enabled

ct_result = ct.request(
    message = 'user comment',
    sender_ip = '196.19.250.114',
    sender_email = 'user@example.com',
    sender_nickname = 'username',
    event_token = 'xxx'  # Token from bot-detector JavaScript
)
```

If you decide not to use bot-detector:
```python
ct = CleanTalk(auth_key='yourkey')
ct.set_event_token_enabled(False)  # Bot-detector is not enabled

ct_result = ct.request(
    message = 'user comment',
    sender_ip = '196.19.250.114',
    sender_email = 'user@example.com',
    sender_nickname = 'username'
)
```

### event_token_enabled flag values:
  * `True` - bot-detector is integrated and enabled (JavaScript token will be used for advanced bot detection)
  * `False` - bot-detector is not integrated or disabled
  * `None` (default) - no explicit bot-detector status specified

## Changelog
Version 1.3
  * New. Now page URL could be added to the request.
  * Mod. Tests file updated.
  * Mod. Readme updated.
