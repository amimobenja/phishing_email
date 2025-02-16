from pathlib import Path
import json

# Path to model
spam_detector_path = Path(r'model/spam_detector.h5')

# Path to tokenizer
tokenizer_path = Path(r'model/tokenizer.pickle')

# Path to user personal information
pers_inf_json = Path(r"data/personal_information.json")

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'



# Path to phishtank data archive .gz
# phishtank_json_gz_path = Path(r"data/phishtank.json.gz")
# PAth to phishtank data json file
# phishtank_json_path = Path(r"data/phishtank.json")
# Path to all save data json file
# phishing_data_feed = Path(r"data/malicious_urls_ips.json")
# ip_regex = "\\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\b"