# Seenomaly API 

## Author 
Rebecca Chen & Peter

Let me know if you have any question or find any bug

## End Point 
POST https://wom3x88xak.execute-api.ap-southeast-2.amazonaws.com/Prod/Seenomaly/

## Sample Result 
![image](https://user-images.githubusercontent.com/55317028/118953423-23b67c80-b9a0-11eb-84ef-31d544f64216.png)

## File Requirements 
### File type 
video/mp4
### File size 
< 6MB
A testing video can be found in the ./data folder
### Sample Code for encoding 
```python
with open(TEST_VIDEO, "rb") as open_file:
        byte_content = open_file.read()
    base64_bytes = base64.b64encode(byte_content)
    base64_string = base64_bytes.decode("utf-8")
    raw_data = base64_string

```

## TimeOut
900 seconds





