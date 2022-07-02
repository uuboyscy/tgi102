### Step1.
    1. import package
    2. url, header, form data, cookies
### Step2. Extract
    1. request and get Response object (HTML string or JSON)
        - urllib: create Request object -> urlopen to get Response object
        - requests: requests.get() or post() to get Response object
### Step3. Transform
    1. determine tags/attribute you want
    2. BeautifulSoup to get HTML object
    3. select-function or find-function to extract tags object
### Step4. Load
    Internet, DB, files, cloud, HDFS, FTP
