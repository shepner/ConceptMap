# ConceptMap

index.html
* This is the output presentation script

tbd.py
* generate the json file(s) to be parsed

tbd2.py
* capture and store the data
* 1 json file per node
* use dir structures to create hierarchy
  * the structure should be based on the size of the dir.  If it gets too big, break it up
  * use a dir per node if there are files to go with the json file
  * dir structure example:  for 6cdc1aef-e1c5-42ca-a845-7536323a4c9b
    * ~/e1/42/a8/75/6cdc1aef-e1c5-42ca-a845-7536323a4c9b.json
* stored files should be renamed?
index.html
which points to whatever.png and some/dir/file.txt

this implies that the contents of the webpage can and will be parsed
  * ~/53/4b/88/04/8cd3644c-53de-4b76-88bf-04c4f26953a1.json  #this is the node pointing to the content
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416.html  #was index.html
  * ~/f8/44/87/02/406488f8-f82e-44b8-87a2-02ce183c4028.png   #was whatever.png
  * ~/cc/4b/83/b5/e5b396ae-ccf6-4bcb-839b-b5e826c72240.txt   #was some/dir/file.txt

this requires no changes to the content downloaded
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416.json  #this is the node pointing to the content
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/index.html
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/whatever.png
  * ~/68/47/94/69/9b699b08-684f-47de-940f-69b8767b3416/some/dir/file.txt

* file named should be based on the UUID of that object (ie 915c5d89-3056-4c66-a85d-fa87ee4ff198.json or e973170b-5812-4e0e-b33a-7c03d0a2cdee.png)

<img src="https://imgs.xkcd.com/comics/digital_resource_lifespan_2x.png" align="right" width="500" height="400">



[D3.js API documentation](https://github.com/d3/d3/blob/master/API.md)
