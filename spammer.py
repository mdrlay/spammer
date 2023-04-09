print("Hello Welcome To spammer")

try:
    input = input("Enter yor Phone: ")
    url = "http://31.25.135.181/mdrlay/spammer.php"
    data = {"phone":input}
    import requests
    requests.post(url,data=data)
except:
    print("Error")